from abc import ABC, abstractmethod

class BaseScraper(ABC):
    """
    Soyut temel scraper sınıfı. Tüm scraperlar bu sınıftan türetilmelidir.
    """
    def __init__(self, url, selectors):
        self.url = url
        self.selectors = selectors

    @abstractmethod
    def fetch(self):
        """Veri çekme işlemini başlatır."""
        pass

    @abstractmethod
    def parse(self, content):
        """Çekilen içeriği ayrıştırır ve veri döndürür."""
        pass
