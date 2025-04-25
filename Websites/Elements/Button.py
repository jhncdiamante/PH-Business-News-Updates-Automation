from Element import Element

class Button(Element):
    def __init__(self, driver, identifier:tuple):
        super().__init__(driver, identifier)
        self._button = self.driver.find_element(*self._identifier)

    def click(self):
        self._button.click()