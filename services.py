from abc import ABC, abstractmethod
from typing import List, Union
from model import Offer

class Parser(ABC):

    @abstractmethod
    def parse(self, url: str, city: str) -> List[Offer]:
        pass


class OffersStorage(ABC): 
    @abstractmethod
    def save(self, offers: List[Offer]) -> None:
        pass