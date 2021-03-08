from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass
class Offer:
    area: float
    description: str
    district: str
    href: str
    price: float
    price_per_meter: float
    rooms: str
    date: date

    def format_csv(self) -> List[str]: 
        return  [self.description, self.district, str(self.rooms), str(self.price), str(self.area), str(self.price_per_meter), str(self.date), self.href]