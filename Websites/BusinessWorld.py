from .Website import Website
from selenium.webdriver.common.by import By
from Elements.Button import Button
class BusinessWorld(Website):
    def __init__(self, base_url, website_name):
        super().__init__(base_url, website_name)

    def navigate_to_page(self, value):
        navigation_button = Button(self._driver, f"//li[a[text()='{value}']]//a")
        navigation_button.click()

    def get_articles(self, time_threshold):

        pass



if __name__ == "__main__":
    import time
    base_url = "https://www.bworldonline.com/"
    website_name = "BusinessWorld"
    business_world = BusinessWorld(base_url, website_name)
    business_world.open_website()
    business_world.navigate_to_page("Top Stories")
    time.sleep(20)