from datetime import datetime

import time
from Websites.Article import BusinessWorldArticle
from .Website import DynamicWebsite
from selenium.webdriver.common.by import By
from Websites.Elements.Button import Button

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class BusinessWorldDynamic(DynamicWebsite):
    def __init__(self, base_url, website_name):
        super().__init__(base_url, website_name)
        self.current_page = None

    def navigate_to_page(self, page_name):
        navigation_button = Button(self._driver, (By.LINK_TEXT, page_name))
        # Hold CTRL and click
    
        navigation_button.click()
        self.current_page = page_name


    def get_articles(self, time_threshold) -> list[BusinessWorldArticle]:
        articles = []
        time.sleep(30)
        self._driver.refresh()
        article_elements = self._wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "td-module-thumb")))
       
           
        for article_element in article_elements:
                        # Hold CTRL and click
            ActionChains(self._driver)\
                .key_down(Keys.CONTROL)\
                .click(article_element)\
                .key_up(Keys.CONTROL)\
                .perform()
            self._driver.switch_to.window(self._driver.window_handles[-1])
            time.sleep(5)

            article_title = self._driver.find_element(By.CLASS_NAME, "entry-title").text
            date = self._driver.find_element(By.TAG_NAME, "time").get_attribute("datetime")
            date = datetime.fromisoformat(date).replace(tzinfo=None)
            if date <= time_threshold:
                break
            article_tags = self._driver.find_elements(By.CLASS_NAME, "entry-category")
            article_tags = [tag.text for tag in article_tags]

            bworldarticle = BusinessWorldArticle(
                title=article_title,
                date=date,
                content=None,
                source=self._website_name,
                article_tags=article_tags,
                category=self.current_page
            )
            articles.append(bworldarticle)
            self._driver.close()
            self._driver.switch_to.window(self._driver.window_handles[0])
            print(f"Title: {article_title}\n------------------------------\n")
            time.sleep(3)
        return articles
    
    def remove_popup(self):
        try:
            self._driver.find_element(By.XPATH, "//div[@class='td-ss-main-content']//div[@class='td-block-title']").click()
        except Exception as e:
            print(f"Error removing popup: {e}")
            


if __name__ == "__main__":
    base_url = "https://www.bworldonline.com/"
    website_name = "BusinessWorld"
    business_world = BusinessWorld(base_url, website_name)
    business_world.open_website()
    business_world.navigate_to_page("Corporate")
    business_world.get_articles(datetime(2025, 4, 25, 3, 23)) # 2025-04-25T00:03:23+08:00
    time.sleep(20)