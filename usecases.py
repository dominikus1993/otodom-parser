import multiprocessing
from services import Parser, OffersStorage
from utils import generate_pages_urls
from multiprocessing import Pool
import itertools
import logging

class GetOffersUseCase:

    __offerParser: Parser
    __storage: OffersStorage
    __logger: logging.Logger

    def __init__(self, parser: Parser, storage: OffersStorage, logger: logging.Logger) -> None:
        self.__offerParser = parser
        self.__storage = storage
        self.__logger = logger


    def load_offers(self, url: str, cityName: str, pages: int) -> None: 
        pages_urls = generate_pages_urls(url, pages)
        process_count = multiprocessing.cpu_count()
        self.__logger.debug("Start parsing offers with process", extra={"process_count": process_count}) 
        with Pool(process_count) as p:
            self.__logger.info("Start parsing offers") 
            w = p.starmap_async(self.__offerParser.parse, map(lambda url: (url, cityName), pages_urls))
            w.wait() 
            offers = list(itertools.chain(*w.get()))
            self.__logger.info("Offers parsed")   
            self.__storage.save(offers=offers)
            self.__logger.info("Offers saved")  
