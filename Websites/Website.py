from abc import ABC, abstractmethod
from Driver.SeleniumDriver import Driver
from selenium.common.exceptions import TimeoutException, SessionNotCreatedException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException

class Website(ABC):
    def __init__(self, base_url, website_name):
        self._base_url = base_url
        self._website_name = website_name
        self._crawler = Driver()
        self._driver = self._crawler.driver
        self._wait = self._crawler.wait
    
    def open_website(self):
        try:
            self._driver.get(self._base_url)
            self._driver.maximize_window()
        except (TimeoutException, SessionNotCreatedException) as e:
            pass

''' @abstractmethod
    def open_page(self):
        pass

'''