from utils import get_csv_filename
from infrastructure import CsvStorage, HtmlParser
from usecases import GetOffersUseCase
import log

logger = log.get_logger()

OTODOM_URL = "https://www.otodom.pl/sprzedaz/mieszkanie/lodz/?search%5Bfilter_enum_market%5D=secondary&search%5Bfilter_float_build_year%3Ato%5D=2019&search%5Border%5D=created_at_first%3Adesc&search%5Bregion_id%5D=5&search%5Bsubregion_id%5D=127&search%5Bcity_id%5D=1004"

parser = HtmlParser(logger)
storage = CsvStorage(f'./data/{get_csv_filename()}', logger)
usecase = GetOffersUseCase(parser, storage, logger)

usecase.load_offers(OTODOM_URL, "Łódź", 56)


logger.info("Finish")