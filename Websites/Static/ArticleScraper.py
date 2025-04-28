from datetime import datetime
from bs4 import BeautifulSoup
import requests
from abc import ABC, abstractmethod
from ..Article import Article


class ArticlePageScraper(ABC):
    def __init__(self, article_url):
        self._article_url = article_url

    @abstractmethod
    def __call__(self):
        pass

    @abstractmethod
    def get_article_title(self) -> str:
        pass

    @abstractmethod
    def get_article_upload_time(self) -> str:
        pass

    @abstractmethod
    def get_article_content(self) -> str:
        pass

class BusinessWorldArticleScraper(ArticlePageScraper):
    def __init__(self, article_url):
        super().__init__(article_url)
        self._soup = None

    def __call__(self):
        request = requests.get(self._article_url)
        self._soup = BeautifulSoup(request.content, 'html.parser')
        return Article(
            title=self.get_article_title(),
            date=self.get_article_upload_time(),
            category="BusinessWorld",
            content=None
        )

    def get_article_title(self) -> str:
        title_element = self._soup.find("h1", class_="entry-title")
        return title_element.text.strip() if title_element else ""

    def get_article_upload_time(self) -> str:
        time_element = self._soup.find("time", class_="entry-date updated td-module-date")
        date = time_element["datetime"]
        date = datetime.fromisoformat(date).replace(tzinfo=None)
        return date.strftime("%Y-%m-%d %H:%M:%S") if date else ""

    def get_article_content(self) -> str:
        content_element = self._soup.find("article",)
        return "\n".join([p.text.strip() for p in content_element.find_all("p")]) if content_element else ""
