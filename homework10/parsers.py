from abc import abstractmethod

import aiohttp
from bs4 import BeautifulSoup, Tag


class BaseParser:
    @staticmethod
    @abstractmethod
    def get_contents_by_tag(tag):
        raise NotImplementedError()


class BeautifulSoupParser(BaseParser):
    @staticmethod
    async def parse_page(url: str) -> BeautifulSoup:
        """
        Get html from url and asynchronously parse it with BeautifulSoup
        :param delay: Amount of seconds to wait before reading the data
        :param url: URL address to check
        :return: BeautifulSoup parser object
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.read()
        return BeautifulSoup(data, "html.parser")

    @staticmethod
    def get_contents_by_tag(tag: Tag):
        if tag is None:
            return None
        contents = tag.contents
        return contents

    @staticmethod
    def get_tag_by_contents(tag: Tag, contents: str):
        if tag is None:
            return None
        current_tag = tag.find(text=contents)
        return current_tag

    @staticmethod
    def get_parent_tag_by_class(tag: Tag, cls: str):
        if tag is None:
            return None
        parent_tag = tag.find_parent(class_=cls)
        return parent_tag

    @staticmethod
    def get_exchange_rate(tag: Tag, valute_id: int):
        valute_tag = tag.find(id=valute_id)
        rate = valute_tag.find("value").text
        rate = float(rate.replace(",", "."))
        return rate
