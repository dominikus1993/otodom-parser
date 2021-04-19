import datetime
from model import Offer
from utils import generate_pages_urls, distinct_by
import unittest

class TestProjectEuler(unittest.TestCase):

    def test_upper(self):
        subject = generate_pages_urls("https://www.otodom.pl/sprzedaz/mieszkanie/lodz/?search%5Bregion_id%5D=5&search%5Bsubregion_id%5D=127&search%5Bcity_id%5D=1004&search%5Border%5D=created_at_first%3Adesc", 10)
        self.assertEqual(len(subject), 11)
        self.assertEqual(subject[0], "https://www.otodom.pl/sprzedaz/mieszkanie/lodz/?search%5Bregion_id%5D=5&search%5Bsubregion_id%5D=127&search%5Bcity_id%5D=1004&search%5Border%5D=created_at_first%3Adesc&page=0")
        self.assertEqual(subject[-1], "https://www.otodom.pl/sprzedaz/mieszkanie/lodz/?search%5Bregion_id%5D=5&search%5Bsubregion_id%5D=127&search%5Bcity_id%5D=1004&search%5Border%5D=created_at_first%3Adesc&page=10")


    def test_distinct_by(self):
        subject = distinct_by(["a", "a", "b", "c"], lambda x: x)
        self.assertEqual(subject, ["a", "b", "c"])

    def test_distinct_by_field(self):
        offer1 = Offer(1, "", "", "a", 12, 1221, "", datetime.datetime.today())
        offer2 = Offer(1, "", "", "b", 12, 1221, "", datetime.datetime.today())
        
        subject = distinct_by([offer1, offer1, offer2, offer2], lambda x: x.href)
        self.assertEqual(len(subject), 2)
        self.assertEqual(subject, [offer1, offer2])


    def test_distinct_by_field_when_offers_has_duplicates(self):
        offer1 = Offer(1, "", "", "a", 12, 1221, "", datetime.datetime.today())
        offer2 = Offer(1, "", "", "b", 12, 1221, "", datetime.datetime.today())
        offer3 = Offer(1, "", "", "https://www.otodom.pl/pl/oferta/przytulne-m-3-na-dabrowie-ID4b6cA.html", 12, 1221, "", datetime.datetime.today())
        offer4 = Offer(1, "", "", "https://www.otodom.pl/pl/oferta/przytulne-m-3-na-dabrowie-ID4b6cA.html", 12, 1221, "", datetime.datetime.today())
        subject = distinct_by([offer1, offer2, offer3, offer4], lambda x: x.href)
        self.assertEqual(len(subject), 3)
        self.assertEqual(subject, [offer1, offer2, offer3])

if __name__ == '__main__':
    unittest.main()