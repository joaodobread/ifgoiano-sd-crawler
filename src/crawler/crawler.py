import os
from threading import Thread
from requests import get
from bs4 import BeautifulSoup
from .utils_page_metadata import UtilsPageMetadata
from src.referrer.referrer import Referrer
import uuid


class Crawler(Thread):
    def __init__(self, deep_factor: int, actual_link: str, actual_domain: str):
        super().__init__()
        self.instance_id = str(uuid.uuid4())
        self.deep_factor = deep_factor
        self.actual_link = actual_link
        self.page_links = []
        self.parsed_document = None
        self.actual_domain = actual_domain
        self.refer = Referrer.get_instance()

    def make_request(self) -> str:
        """
        Raises:
            Exception: When something get wrong with request will be raised an error
            with the attributes

        Returns:
            str: When success will be return all content of returned from server as a string
        """
        response = get(self.actual_link)
        if not response.ok:
            raise Exception({
                "status": response.status_code,
                "message": response.reason,
                "at": self.actual_link
            })

        return response.text

    def parse_html(self, text: str):
        """
        Args:
            text (str): The content of page in text to parse to BS4 object

        Returns:
            BeautifulSoup: the html string to BS4 object
        """
        self.parsed_document = BeautifulSoup(text, 'html.parser')
        return self.parsed_document

    def extract_links(self):
        ancher_tags = self.parsed_document.find_all('a')
        self.page_links = [link.get('href') for link in ancher_tags if str(
            link.get('href')).__contains__(self.actual_domain)]

        return self.page_links

    def go_deeper(self):
        if self.deep_factor >= int(os.getenv('DEEP_FACTOR_LIMIT')):
            return False

        for link in self.page_links:
            crawler = Crawler(self.deep_factor + 1, link, self.actual_domain)
            crawler.setDaemon(True)
            crawler.start()
            crawler.join()

    def run(self):
        page_text = self.make_request()
        self.parse_html(page_text)
        links = self.extract_links()
        for link in links:
            self.refer.add_link(self.actual_link, link)

        self.go_deeper()
