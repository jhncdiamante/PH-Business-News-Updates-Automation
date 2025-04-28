from Websites.Elements.Element import Element

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Button(Element):
    def __init__(self, driver, identifier:tuple):
        super().__init__(driver, identifier)
        self._button = self._driver.find_element(*self._identifier)

    def click(self):
        self._button.click()