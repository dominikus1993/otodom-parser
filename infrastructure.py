import datetime
import logging
import multiprocessing
from model import Offer
from typing import List
from services import OffersStorage, Parser
from bs4 import BeautifulSoup
import requests

class HtmlParser(Parser):
    __logger: logging.Logger

    def __init__(self, logger: logging.Logger) -> None:
        self.__logger = logger

    def parse(self, url: str, city: str) -> List[Offer]:
        self.__logger.debug('Start Parsing', extra={"url": url, "process_id": multiprocessing.current_process()})
        html = requests.get(url);
        soup = BeautifulSoup(html.content, "html.parser")
        offers = soup.find_all('article')
        return [Offer(1.2, ",", "", "", 12.12, 12.2, "", datetime.date(2008, 6, 24))]


class FakeStorage(OffersStorage):
    __logger: logging.Logger

    def __init__(self, logger: logging.Logger) -> None:
        self.__logger = logger

    def save(self, offers: List[Offer]):
        self.__logger.info("Saved")