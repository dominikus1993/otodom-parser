from abc import ABC, abstractmethod
from typing import List
from model import Offer

class Parser(ABC):

    @abstractmethod
    def parse(self, url: str, city: str) -> List[Offer]:
        pass