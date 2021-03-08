import datetime
import logging
import multiprocessing
from utils import format_price
from model import Offer
from typing import Any, List
from services import OffersStorage, Parser
from bs4 import BeautifulSoup
import requests

def trim_word(txt: str, word: str) -> str: 
    return txt.replace(word, "")

class HtmlParser(Parser):
    __logger: logging.Logger

    def __init__(self, logger: logging.Logger) -> None:
        self.__logger = logger
        
    def __get_href(self, offer: Any) -> str:
        href = offer.find('a').attrs['href']
        print(href)
        return href

    def __clean_offer(self, txt: str) -> str:
        data = str(txt).strip()
        data = trim_word(data, " zł/m²")
        data = trim_word(data, " zł")
        data = trim_word(data, " m²")
        data = trim_word(data, " pokoje")
        data = trim_word(data, " pokój")
        return data
    
    def __is_valid_offer(self, offer: List[str]): 
        return not ("Zapytaj o cenę" in offer or "Obsługa zdalna" in offer)

    def parse(self, url: str, city: str) -> List[Offer]:
        self.__logger.debug('Start Parsing', extra={"url": url, "process_id": multiprocessing.current_process()})
        html = requests.get(url);
        soup = BeautifulSoup(html.content, "html.parser")
        offers = soup.find_all('article')
        result = []
        for offer in offers:
            details = offer.find_all("div", class_="offer-item-details")[0]
            href = self.__get_href(offer)
            data = [self.__clean_offer(e) for e in details.text.split('\n') if e and e.strip()]
            if self.__is_valid_offer(data):
                result.append(Offer(format_price(data[0]), data[1], data[2], href, format_price(data[4]), format_price(data[6]), data[3], datetime.date(2008, 6, 24)))
        return result


class FakeStorage(OffersStorage):
    __logger: logging.Logger

    def __init__(self, logger: logging.Logger) -> None:
        self.__logger = logger

    def save(self, offers: List[Offer]):
        self.__logger.info("Saved")