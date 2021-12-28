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
import json
import time
from typing import Union

import aiohttp
from bs4 import BeautifulSoup, NavigableString, ResultSet
from tqdm import tqdm

WEB_URL = "https://markets.businessinsider.com"
SNP_URL = WEB_URL + "/index/components/s&p_500?p="
CBR_URL = "http://www.cbr.ru/scripts/XML_daily.asp"
USD_VALUTE_ID = "R01235"
SLEEP_DELAY = 2
TOP_N = 10


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


async def get_exchange_rate() -> float:
    """
    Get dollar to rubble exchange rate from central bank
    :return: Current exchange rate
    """
    page = await parse_page(CBR_URL)
    valute_tag = page.find(id=USD_VALUTE_ID)
    rate = valute_tag.find("value").text
    rate = float(rate.replace(",", "."))
    return rate


async def parse_page(url: str, delay=None) -> BeautifulSoup:
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


def find_value_by_text(comp_snapshot_tag: Union[NavigableString,
                                                BeautifulSoup],
                       text: str) -> None or float:
    """
    Get value by tags' text
    :param comp_snapshot_tag:
    :param text: Tags' text
    :return: Float value if tag if found, else None
    """
    if comp_snapshot_tag is None:
        return None
    tag = comp_snapshot_tag.find(text=text)
    if tag is None:
        return None
    tag = tag.find_parent(
        class_="snapshot__data-item")
    val = tag.contents[0]
    val = _str_to_float(val)
    return val


async def get_comp_data(row: ResultSet, exchange_rate=None) -> object:
    """
    Get company info

    Take company link from the first column and parse this company page
    to get its name, code and P/E Ratio. Then take yearly price change
    in percents from the last column.
    :param exchange_rate: Current usd to rub exchange rate from central bank
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
            comp.pe = find_value_by_text(comp_snapshot_tag,
                                         "P/E Ratio")
            comp.val_highest = find_value_by_text(comp_snapshot_tag,
                                                  "52 Week High")
            comp.val_lowest = find_value_by_text(comp_snapshot_tag,
                                                 "52 Week Low")
            comp.current_price = find_value_by_text(comp_snapshot_tag,
                                                    "Prev. Close")
            if exchange_rate:
                comp.current_price *= exchange_rate
        if i == 7:
            comp_year_change = col.find_all("span")[1]
            comp_year_change = _str_to_float(comp_year_change.text)
            comp.year_change = comp_year_change
        pass

    return comp


async def get_market_data(url) -> ResultSet:
    """
    Parse market S&P 500 page to get data table
    :param url: URL address to check
    :return: Data table body
    """
    snp500_page = await parse_page(url)
    table = snp500_page.find(class_="table__tbody")
    table_body = table.find_all("tr")
    return table_body


async def get_companies_list() -> list:
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
    exchange_rate = await get_exchange_rate()

    companies_list = []
    for page in tqdm(table_pages):
        row_tasks = [asyncio.create_task(get_comp_data(row, exchange_rate))
                     for row in page]
        await asyncio.gather(*row_tasks)
        companies = [row_task.result() for row_task in row_tasks]
        companies_list.extend(companies)
        pass

    return companies_list


def _serialize_objects(cls_list: list, filename: str):
    """
    Write attributes of list of objects to a json file
    :param cls_list: List of objects
    :param filename: Name of the json file
    """
    data = [cls.__dict__ for cls in cls_list]
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def get_top_n(companies_list: list, sort: str, top_n=TOP_N, serialize=False):
    """
    Get Top-N companies with highest current price
    :param companies_list: List of Company objects
    :param sort: Parameter to sort: "current_price", "lowest_pe",
    "highest_growth", "most_profitable"
    :param top_n: Number of companies from the top to take
    :param serialize: Write objects to file if True
    :return: Top-N companies with highest current price
    """
    acceptable_params = [
        "current_price",
        "lowest_pe",
        "highest_growth",
        "most_profitable"
    ]
    if sort not in acceptable_params:
        raise AttributeError(f"Unknown sort parameter: {sort}")
    if sort == "current_price":
        top = sorted(companies_list,
                     key=lambda x: (x.current_price is None, x.current_price),
                     reverse=True)
    if sort == "lowest_pe":
        top = sorted(companies_list, key=lambda x: (x.pe is None, x.pe))
    if sort == "highest_growth":
        top = sorted(companies_list,
                     key=lambda x: (x.year_change is None, x.year_change),
                     reverse=True)
    if sort == "most_profitable":
        top = sorted(companies_list,
                     key=lambda x: (x.val_highest is not None
                                    and x.val_lowest is not None,
                                    x.val_highest - x.val_lowest
                                    if x.val_highest is not None
                                    and x.val_lowest is not None
                                    else None
                                    ), reverse=True)
    top = top[:top_n]
    if serialize:
        _serialize_objects(top, f"Top_{top_n}_current_price.json")
    return top


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

    get_top_n(companies_list, "current_price", serialize=True)
    get_top_n(companies_list, "lowest_pe", serialize=True)
    get_top_n(companies_list, "highest_growth", serialize=True)
    get_top_n(companies_list, "most_profitable", serialize=True)
