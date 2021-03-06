from dataclasses import dataclass
from datetime import date

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