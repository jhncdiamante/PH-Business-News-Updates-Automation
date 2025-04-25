from Element import Element
from abc import abstractmethod

class Menu(Element):
    def __init__(self, driver, identifier:tuple):
        super().__init__(driver, identifier)
        self._menu_bar = self.driver.find_element(*self._identifier)
        self._page_buttons = None
        self._search = None

    @abstractmethod
    def head_to_menu(self):
        pass

class BusinessWorldMenuBar(Menu):
    def __init__(self, driver, identifier:tuple):
        super().__init__(driver, identifier)

    def get_navigation_buttons(self):
        