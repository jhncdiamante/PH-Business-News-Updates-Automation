from abc import ABC, abstractmethod

import requests
from Driver.SeleniumDriver import Driver
from selenium.common.exceptions import TimeoutException, SessionNotCreatedException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException
from bs4 import BeautifulSoup




class Website(ABC):
    def __init__(self, base_url, website_name):
        self._base_url = base_url
        self._website_name = website_name
        self._current_page = None
    
    @abstractmethod
    def open_website(self):
        raise NotImplementedError("Subclasses should implement this!")

class DynamicWebsite(Website):
    def __init__(self, base_url, website_name):
        super().__init__(base_url, website_name)
        self._current_page = None
        self._crawler = Driver()
        self._driver = self._crawler.driver
        self._wait = self._crawler.wait
        

    def open_website(self):
        try:
            self._driver.get(self._base_url)
            self._driver.maximize_window()
        except (TimeoutException, SessionNotCreatedException) as e:
            pass

class StaticWebsite(Website):
    def __init__(self, base_url, website_name):
        super().__init__(base_url, website_name)

    @staticmethod
    def open_page(self) -> BeautifulSoup:
        try:
            request = requests.get(self._base_url)
            if request.status_code == 200:
                soup = BeautifulSoup(request.content, 'html.parser')
                return soup
            else:
                raise Exception(f"Failed to retrieve the page. Status code: {request.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while making the request: {e}")
        
    def open_website(self):
        return super().open_website()