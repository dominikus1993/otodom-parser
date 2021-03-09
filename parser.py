from utils import get_csv_filename
from infrastructure import FakeStorage, HtmlParser
from usecases import GetOffersUseCase
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger("otodom.parser")
logger.setLevel(logging.DEBUG)
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logHandler.setLevel(logging.DEBUG)

logger.addHandler(logHandler)

OTODOM_URL = "https://www.otodom.pl/sprzedaz/mieszkanie/lodz/?search%5Bregion_id%5D=5&search%5Bsubregion_id%5D=127&search%5Bcity_id%5D=1004&search%5Border%5D=created_at_first%3Adesc"

parser = HtmlParser(logger)
storage = FakeStorage(f'./data/{get_csv_filename()}', logger)
usecase = GetOffersUseCase(parser, storage, logger)

usecase.load_offers(OTODOM_URL, "Łódź", 72)


logger.info("Finish")