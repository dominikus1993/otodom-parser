

import datetime
import multiprocessing
from model import Offer
from typing import List
from services import Parser

class FakeParser(Parser): 
    def parse(self, url: str, city: str) -> List[Offer]:
        print(f'Parser {multiprocessing.current_process()}')
        return [Offer(1.2, ",", "", "", 12.12, 12.2, "", datetime.date(2008, 6, 24))];