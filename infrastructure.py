import datetime
import logging
import multiprocessing
from os import write
from utils import format_price, get_district_name
from model import Offer
from typing import Any, List
from services import OffersStorage, Parser
from bs4 import BeautifulSoup
import requests
import csv

def trim_word(txt: str, word: str) -> str: 
    return txt.replace(word, "")


class HtmlParser(Parser):
    __logger: logging.Logger

    def __init__(self, logger: logging.Logger) -> None:
        self.__logger = logger
        
    def __get_href(self, offer: Any) -> str:
        return offer.find('a').attrs['href']

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
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        offers = soup.find_all('article')
        result = []
        for offer in offers:
            details = offer.find_all("div", class_="offer-item-details")[0]
            href = self.__get_href(offer)
            data = [self.__clean_offer(e) for e in details.text.split('\n') if e and e.strip()]
            if self.__is_valid_offer(data):
                result.append(Offer(format_price(data[0]), data[1], get_district_name(data[2], city), href, format_price(data[4]), format_price(data[6]), data[3], datetime.date.today()))
        return result


class FakeStorage(OffersStorage):
    __logger: logging.Logger
    __path: str

    def __init__(self, path: str, logger: logging.Logger) -> None:
        self.__logger = logger
        self.__path = path

    def save(self, offers: List[Offer]):
        colums = ["Opis","Dzielnica","Ilość pokoi","Cena","Powierzchnia","Cena za m2","Data","Link do ogłoszenia"]
        data = list(map(lambda x: x.format_csv(),  offers))
        with open(self.__path, "w") as f:
            write = csv.writer(f)
            write.writerow(colums)
            write.writerows(data)
            self.__logger.info("Saved")