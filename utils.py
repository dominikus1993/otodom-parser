from typing import List

def generate_pages_urls(url: str, maxPage: int) -> List[str]:
    return list(map(lambda page: f'{url}&page={page}',range(0, maxPage + 1)))