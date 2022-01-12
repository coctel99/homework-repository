from dataclasses import dataclass


@dataclass
class BaseSite:
    pass


class BusinessInsiderSite(BaseSite):
    url = "https://markets.businessinsider.com"
    snp_url = url + "/index/components/s&p_500"
    number_of_pages = 12
    companies_table_class = "table__tbody"
    table_row = "tr"
    table_data = "td"
    table_data_class = "table__td"
    company_name_class = "price-section__label"
    company_code_class = "price-section__category"
    snapshot_class = "snapshot"
    snapshot_data_item_class = "snapshot__data-item"
    text_pe = "P/E Ratio"
    text_highest = "52 Week High"
    text_lowest = "52 Week Low"
    text_current_price = "Prev. Close"


class CentralBankSite(BaseSite):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    usd_valute_id = "R01235"
