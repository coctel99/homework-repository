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
import time
import aiohttp
from bs4 import BeautifulSoup, ResultSet, NavigableString
from typing import Union
from tqdm import tqdm

WEB_URL = "https://markets.businessinsider.com"
SNP_URL = WEB_URL + "/index/components/s&p_500?p="
SLEEP_DELAY = 2
TOP_N = 10


# async def get_current_rate():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             # time.sleep(1)
#             data = await response.read()
#     return data


class Company:
    def __init__(self, name=None, code=None, current_price=None,
                 pe=None, year_change=None, val_lowest=None, val_highest=None):
        self.name = name
        self.code = code
        self.current_price = current_price
        self.pe = pe
        self.year_change = year_change
        self.val_lowest = val_lowest
        self.val_highest = val_highest

    # async def set_name(self, name):
    #     self.name = name
    #
    # async def set_code(self, code):
    #     self.code = code
    #
    # async def set_pe(self, pe):
    #     self.pe = pe


async def parse_page(url: str, delay=None):
    """
    Get html from url and asynchronously parse it with BeautifulSoup
    :param delay: Amount of seconds to wait before reading the data
    :param url: URL address to check
    :return: BeautifulSoup parser object
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if delay:
                await asyncio.sleep(delay)
            data = await response.read()
    return BeautifulSoup(data, "html.parser")


def _str_to_float(val: str):
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


def find_value_by_text(comp_snapshot_tag: Union[NavigableString,
                                                BeautifulSoup], text: str):
    """
    Get value by tags' text
    :param comp_snapshot_tag:
    :param text: Tags' text
    :return: Float value if tag if found, else None
    """
    tag = comp_snapshot_tag.find(text=text)
    if not tag:
        return None
    tag = tag.find_parent(
        class_="snapshot__data-item")
    val = tag.contents[0]
    val = _str_to_float(val)
    return val


async def get_comp_data(row: ResultSet):
    """
    Get company info

    Take company link from the first column and parse this company page
    to get its name, code and P/E Ratio. Then take yearly price change
    in percents from the last column.
    :param row: Row of data table
    :return: Company object with parsed attributes
    """
    comp = Company()
    for i, col in enumerate(row.find_all("td")):
        if i == 0:
            comp_url = WEB_URL + col.find("a").get('href')
            comp_page = await parse_page(comp_url)

            comp_name_tag = comp_page.find(class_="price-section__label")
            comp_name = comp_name_tag.text.strip()
            comp.name = comp_name

            comp_code_tag = comp_page.find(class_="price-section__category")
            comp_code_tag = comp_code_tag.find("span")
            comp_code = comp_code_tag.text.split(", ")[1]
            comp.code = comp_code

            # Sometimes we read HTML faster, that snapshot class is created
            comp_snapshot_tag = comp_page.find(class_="snapshot")
            if not comp_snapshot_tag:
                # Second attempt to get the snapshot class tag with delay
                comp_page = await parse_page(comp_url, SLEEP_DELAY)
                print("SECOND TRY: ", comp_name)
                comp_snapshot_tag = comp_page.find(class_="snapshot")
            # comp_pe_tag = comp_snapshot_tag.find(text="P/E Ratio")
            # Set pe to None if there are no P/E Ratio for this company
            # if comp_pe_tag:
            #     comp_pe_tag = comp_pe_tag.find_parent(
            #         class_="snapshot__data-item")
            #     comp_pe = _str_to_float(comp_pe_tag.contents[0])
            # else:
            #     comp_pe = None
            comp.pe = find_value_by_text(comp_snapshot_tag,
                                         "P/E Ratio")

            # comp_val_highest_tag = comp_snapshot_tag.find(text="52 Week High")
            # comp_val_highest_tag = comp_val_highest_tag.find_parent(
            #     class_="snapshot__data-item")
            # comp_val_highest = _str_to_float(comp_val_highest_tag.contents[0])
            # comp.val_highest = comp_val_highest
            comp.val_highest = find_value_by_text(comp_snapshot_tag,
                                                  "52 Week High")

            comp.val_lowest = find_value_by_text(comp_snapshot_tag,
                                                 "52 Week Low")

            comp.current_price = find_value_by_text(comp_snapshot_tag,
                                                    "Prev. Close")
        if i == 7:
            comp_year_change = col.find_all("span")[1]
            comp_year_change = _str_to_float(comp_year_change.text)
            comp.year_change = comp_year_change
        pass

    return comp


async def get_market_data(url):
    """
    Parse market S&P 500 page to get data table
    :param url: URL address to check
    :return: Data table body
    """
    snp500_page = await parse_page(url)
    table = snp500_page.find(class_="table__tbody")
    table_body = table.find_all("tr")
    return table_body

    # for row in table:
    #     company = Company()
    #     comp_name = None
    #     comp_code = None
    #     comp_pe = None
    #     comp_year_change = None
    #     for i, col in enumerate(row.find_all("td")):
    #         Taking company name from the first column
    #         if i == 0:
    #             comp_url = WEB_URL + col.find("a").get('href')
    #             comp_page = await parse_page(comp_url)
    #
    #             comp_name_tag = comp_page.find(class_="price-section__label")
    #             comp_code_tag = comp_page.find(
    #                 class_="price-section__category")
    #             comp_code_tag = comp_code_tag.find("span")
    #             comp_snapshot_tag = comp_page.find(class_="snapshot")
    #             comp_pe_tag = comp_snapshot_tag.find(text="P/E Ratio")
    #             if comp_pe_tag:
    #                 comp_pe_tag = comp_pe_tag.find_parent(
    #                     class_="snapshot__data-item")
    #
    #             comp_name = comp_name_tag.text.strip()
    #             names.append(comp_name)
    #             comp_code = comp_code_tag.text.split(", ")[1]
    #             if comp_pe_tag:
    #                 comp_pe = comp_pe_tag.contents[0].strip()
    #             else:
    #                 comp_pe = None
    #
    #             await company.set_name(comp_name)
    #             await company.set_code(comp_code)
    #             await company.set_pe(comp_pe)
    #             pass
    #         Taking company stocks rise or fall from the las column
    #         if i == 7:
    #             # WE need change in percent which is the second tag
    #             comp_year_change = col.find_all("span")[1]
    #             comp_year_change = comp_year_change.text
    #             company.year_change = comp_year_change
    #
    #             companies.append(Company(name=comp_name, code=comp_code,
    #                                      pe=comp_pe,
    #                                      year_change=comp_year_change))
    #             pass
    #         pass
    #     pass
    # return companies_list


async def get_companies_list():
    """
    Get all Market Insider companies data
    :return:
    """
    urls = []
    # Add all 11 url pages
    for i in range(1, 12):
        urls.append(SNP_URL + str(i))

    page_tasks = [asyncio.create_task(get_market_data(url)) for url in urls]
    await asyncio.gather(*page_tasks)

    table_pages = [page_task.result() for page_task in page_tasks]

    companies_list = []
    for page in tqdm(table_pages):
        row_tasks = [asyncio.create_task(get_comp_data(row)) for row in page]
        await asyncio.gather(*row_tasks)
        companies = [row_task.result() for row_task in row_tasks]
        companies_list.extend(companies)
        pass

    # for url, task in zip(urls, tasks):
    #     print(f"Url: {url}\nResponse: {task.result()}")
    # companies_names = [comp.name for comp in companies_list]
    return companies_list


def scrap_market_insider_data():
    """
    Parse data from Market Insider resource and create 4 JSON files

    1-st: Top-10 companies with highest current price
    2-nd: Top-10 companies with lowest P/E ratio
    3-rd: Top-10 companies with highest yearly price growth percent
    4-th: Top-10 companies providing highest income if bought on minimum
    and sold on maximum for the last year
    """
    companies_list = asyncio.run(get_companies_list())
    # Top-10 companies with highest current price
    top_n_current_price = sorted(companies_list, key=lambda x: x.current_price,
                                 reverse=True)
    top_n_current_price = top_n_current_price[:TOP_N]
    top_n_current_price_readable = [(comp.name, comp.current_price)
                                    for comp in top_n_current_price]

    # Top-10 companies with lowest P/E ratio
    top_n_lowest_pe = sorted(companies_list,
                             key=lambda x: (x.pe is None, x.pe))
    top_n_lowest_pe = top_n_lowest_pe[:TOP_N]
    top_n_lowest_pe_readable = [(comp.name, comp.pe)
                                for comp in top_n_lowest_pe]

    # Top-10 companies with highest yearly price growth percent
    top_n_highest_growth = sorted(companies_list, key=lambda x: x.year_change,
                                  reverse=True)
    top_n_highest_growth = top_n_highest_growth[:TOP_N]
    top_n_highest_growth_readable = [(comp.name, comp.year_change)
                                     for comp in top_n_highest_growth]

    # Top-10 companies for highest possible income
    top_n_for_income = sorted(companies_list,
                              key=lambda x: (
                                  x.val_highest is not None
                                  and x.val_lowest is not None,
                                  x.val_highest - x.val_lowest
                                  if x.val_highest is not None
                                  and x.val_lowest is not None
                                  else None
                              ),
                              reverse=True)
    top_n_for_income = top_n_for_income[:TOP_N]
    top_n_for_income_readable = [(comp.name,
                                  comp.val_highest - comp.val_lowest
                                  if comp.val_highest is not None
                                  and comp.val_lowest is not None
                                  else None) for comp in top_n_for_income]

    return top_n_for_income_readable


if __name__ == '__main__':
    time1 = time.time()
    print(scrap_market_insider_data())
    time2 = time.time()
    print(time2 - time1)
