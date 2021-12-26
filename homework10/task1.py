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
from bs4 import BeautifulSoup, ResultSet
from tqdm import tqdm

WEB_URL = "https://markets.businessinsider.com"
SNP_URL = WEB_URL + "/index/components/s&p_500?p="


class Company:
    def __init__(self, name=None, code=None, current_price=None,
                 pe=None, year_change=None):
        self.name = name
        self.code = code
        self.current_price = current_price
        self.pe = pe
        self.year_change = year_change

    # async def set_name(self, name):
    #     self.name = name
    #
    # async def set_code(self, code):
    #     self.code = code
    #
    # async def set_pe(self, pe):
    #     self.pe = pe


async def parse_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # time.sleep(1)
            data = await response.read()
    return BeautifulSoup(data, "html.parser")


async def get_comp_data(row: ResultSet):
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

            comp_snapshot_tag = comp_page.find(class_="snapshot")
            comp_pe_tag = comp_snapshot_tag.find(text="P/E Ratio")
            if comp_pe_tag:
                comp_pe_tag = comp_pe_tag.find_parent(
                    class_="snapshot__data-item")
                comp_pe = comp_pe_tag.contents[0].strip()
            else:
                comp_pe = None
            comp.pe = comp_pe

        if i == 7:
            comp_year_change = col.find_all("span")[1]
            comp_year_change = comp_year_change.text
            comp.year_change = comp_year_change
        pass

    return comp


async def get_market_data(url):
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


async def get_data_from_urls():
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
    companies_names = [cmp.name for cmp in companies_list]
    return companies_names


if __name__ == '__main__':
    time1 = time.time()
    print(asyncio.run(get_data_from_urls()))
    time2 = time.time()
    print(time2 - time1)
