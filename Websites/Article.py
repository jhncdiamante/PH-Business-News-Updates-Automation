from datetime import datetime
from typing import Optional, Union

class Article:
    def __init__(self, title: str, date: datetime, category: str, content: Optional[str] = None):
        self._title = title
        self._date = date
        self._content = content
        self._category = category

    @property
    def title(self) -> str:
        return self._title
    
    @property
    def date(self) -> datetime:
        return self._date


    @title.setter
    def title(self, title: str):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        self._title = title

    @date.setter
    def date(self, date: object):
        if not isinstance(date, (str, datetime)):
            raise ValueError("Date must be a string or a datetime object")
        self._date = date

class BusinessWorldArticle(Article):
    def __init__(self, source: str, title: str, date: object, content: str):
        super().__init__(source, title, date, content)
        self._source = "BusinessWorld"
        self._article_tags: Optional[list] = None

   