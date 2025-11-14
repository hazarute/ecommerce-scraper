from abc import ABC, abstractmethod


class BaseScraper(ABC):
    """
    Soyut temel scraper sınıfı. Tüm scraperlar bu sınıftan türetilmelidir.
    """

    def __init__(self, url: str, selectors: dict):
        self.url = url
        self.selectors = selectors or {}
        self.last_error = None

    @abstractmethod
    def fetch(self):
        """Veri çekme işlemini başlatır.

        Returns:
            str: HTML içeriği veya None
        """
        raise NotImplementedError()

    @abstractmethod
    def parse(self, content: str):
        """Çekilen içeriği ayrıştırır ve veri döndürür.

        Returns:
            list: Ürün dict'lerinin listesi
        """
        raise NotImplementedError()
