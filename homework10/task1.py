"""
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500
с данного сайта: https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

• Текущая стоимость в рублях (конвертацию производить по текущему курсу,
взятому с сайта центробанка РФ)
• Код компании (справа от названия компании на странице компании)
P/E компании (информация находится справа от графика на странице компании)
• Годовой рост/падение компании в процентах (основная таблица)
• Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они
были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа
от графика на странице компании)

Сохранить итоговую информацию в 4 JSON файла:

1.Топ 10 компаний с самими дорогими акциями в рублях.
2.Топ 10 компаний с самым низким показателем P/E.
3.Топ 10 компаний, которые показали самый высокий рост за последний год
4.Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были
куплены на самом минимуме и проданы на самом максимуме за последний год.
Пример формата:
[
    {
        "code": "MMM",
        "name": "3M CO.",
        "price" | "P/E" | "growth" | "potential profit" : value,
    },
    ...
]
For scrapping you cans use beautifulsoup4
For requesting aiohttp
"""
import asyncio
from typing import List

from bs4 import ResultSet, Tag
from tqdm import tqdm

from homework10.company import Company
from homework10.parsers import BeautifulSoupParser
from homework10.sites import BusinessInsiderSite, CentralBankSite
from homework10.top import get_top_n


def main():
    """
    Parse data from Market Insider resource and create 4 JSON files

    1-st: Top-10 companies with highest current price
    2-nd: Top-10 companies with lowest P/E ratio
    3-rd: Top-10 companies with highest yearly price growth percent
    4-th: Top-10 companies providing highest income if bought on minimum
    and sold on maximum for the last year
    """
    parser = BeautifulSoupParser()
    cbr_site = CentralBankSite()
    bi_site = BusinessInsiderSite()

    valute = asyncio.run(parser.parse_page(cbr_site.url))
    dollar_rate = parser.get_exchange_rate(valute, cbr_site.usd_valute_id)

    urls = get_pages_urls(bi_site.snp_url, bi_site.number_of_pages)
    pages = [asyncio.run(parser.parse_page(url)) for url in urls]

    companies = asyncio.run(get_companies_list(bi_site, parser,
                                               pages, dollar_rate))

    get_top_n(companies, "current_price", serialize=True)
    get_top_n(companies, "lowest_pe", serialize=True)
    get_top_n(companies, "highest_growth", serialize=True)
    get_top_n(companies, "most_profitable", serialize=True)


async def get_companies_list(site: type(BusinessInsiderSite),
                             parser: type(BeautifulSoupParser),
                             pages: List,
                             exchange_rate: float) -> list:
    """
    Parse pages and get companies list
    :param site: Object of BusinessInsiderSite
    :param parser: Object of BeautifulSoupParser
    :param pages: List of pages to parse
    :param exchange_rate: Currency exchange rate
    :return: List of companies of S&P500
    :rtype: List
    """
    companies_list = []
    for page in tqdm(pages):
        table = page.find(class_=site.companies_table_class)
        rows = table.find_all(site.table_row)
        rows = [row.find_all(class_=site.table_data_class) for row in rows]
        page_tasks = [asyncio.create_task(get_company_data(
            site, parser, row, exchange_rate)) for row in rows]
        await asyncio.gather(*page_tasks)
        page_companies = [page_task.result() for page_task in page_tasks]
        companies_list.extend(page_companies)
    return companies_list


async def get_company_data(site: BusinessInsiderSite,
                           parser: BeautifulSoupParser,
                           row: ResultSet, exchange_rate=None) -> object:
    """
    Get company info

    Take company link from the first column and parse this company page
    to get its name, code and P/E Ratio. Then take yearly price change
    in percents from the last column.
    :param site: BusinessInsiderSite object
    :param parser: BeautifulSoupParser object
    :param exchange_rate: Current usd to rub exchange rate from central bank
    :param row: Row of S&P500 table
    :return: Company object with parsed attributes
    """
    comp = Company()

    name_col, year_change_col = row[0], row[-1]

    comp_url = site.url + name_col.find("a").get('href')
    comp_page = await parser.parse_page(comp_url)

    comp_name_tag = comp_page.find(class_=site.company_name_class)
    comp_name = comp_name_tag.text.strip()
    comp.name = comp_name

    comp_code_tag = comp_page.find(class_=site.company_code_class)
    comp_code_tag = comp_code_tag.find("span")
    comp_code = comp_code_tag.text.split(", ")[1]
    comp.code = comp_code

    comp_snapshot_tag = comp_page.find(class_=site.snapshot_class)

    comp.pe = find_comp_value_by_text(site, parser, comp_snapshot_tag,
                                      site.text_pe)
    comp.val_highest = find_comp_value_by_text(site, parser,
                                               comp_snapshot_tag,
                                               site.text_highest)
    comp.val_lowest = find_comp_value_by_text(site, parser,
                                              comp_snapshot_tag,
                                              site.text_lowest)
    comp.current_price = find_comp_value_by_text(site, parser,
                                                 comp_snapshot_tag,
                                                 site.text_current_price)
    if exchange_rate:
        comp.current_price *= exchange_rate

    comp_year_change = year_change_col.find_all("span")[1]
    comp_year_change = _str_to_float(comp_year_change.text)
    comp.year_change = comp_year_change

    return comp


def get_pages_urls(snp_url: str, num_of_pages: int) -> List:
    """
    Add number of page urls
    :param snp_url: Link to S&P500 page
    :param num_of_pages: Number of pages to process
    :return: List of page urls
    """
    urls = []
    for i in range(1, num_of_pages + 1):
        urls.append(f"{snp_url}?p={str(i)}")
    return urls


def find_comp_value_by_text(site: BusinessInsiderSite,
                            parser: BeautifulSoupParser,
                            tag: Tag,
                            text: str) -> None or float:
    """
    Get value by tags' text
    :param site: Object of BusinessInsiderSite
    :param parser: Object of BeautifulSoupParser
    :param tag: Child tag with text
    :param text: Tags' text
    :return: Float value if tag if found, else None
    """
    child_tag = parser.get_tag_by_contents(tag, text)
    if child_tag is None:
        return None
    parent_tag = parser.get_parent_tag_by_class(child_tag,
                                                site.snapshot_data_item_class)
    val = parent_tag.contents[0]
    val = _str_to_float(val)
    return val


def _str_to_float(val: str) -> float:
    """
    Removes special symbols and converts a string to a float
    :param val: String to convert
    :return: Float number of string
    """
    val = val.strip()
    # Remove comma and percent chars
    val = val.replace(",", "").replace("%", "")
    float_val = float(val)
    return float_val


if __name__ == "__main__":
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    main()
