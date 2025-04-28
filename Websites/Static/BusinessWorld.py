
import requests
from ..Website import StaticWebsite
from bs4 import BeautifulSoup
from .ArticleScraper import BusinessWorldArticleScraper

class BusinessWorldStatic(StaticWebsite):
    def __init__(self, base_url, website_name):
        super().__init__(base_url, website_name)

    def get_categories(self, soup:BeautifulSoup) -> list[str]:
        categories = []
        container = soup.find("ul", id="menu-header-menu-1")
        if not container:
            print("Could not find the menu container.")
            return categories
        category_elements = container.find_all("li", class_="menu-item", recursive=False)
       
        for category in category_elements:
            category_name = category.find("a", ).text.strip()
            if category_name.lower() == 'markets':
                continue
            categories.append(category_name)
            print(f"Category: {category_name}")

        print(f"Total categories found: {len(categories)}")
        return categories
    
    def open_category_page(self, category_name: str) -> BeautifulSoup:
        try:
            category_url = f"{self._base_url}{category_name.lower().replace(' ', '-')}/"
            request = requests.get(category_url)
            if request.status_code == 200:
                soup = BeautifulSoup(request.content, 'html.parser')
                return soup
            else:
                raise Exception(f"Failed to retrieve the page. Status code: {request.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while making the request: {e}")
        
    def get_articles(self, soup:BeautifulSoup) -> list[str]:
        articles = []
        article_elements = soup.find_all("div", class_="td-module-thumb")
        for article in article_elements:
            article_link = article.find("a")["href"]
            articles.append(article_link)
        return articles
    
    def open_next_page(self, soup:BeautifulSoup) -> BeautifulSoup:
        next_page_element = soup.find("div", class_="page-nav td-pb-padding-side")
        if next_page_element:
            next_page_link = next_page_element.find_all("a")[-1]['href']
            request = requests.get(next_page_link)
            if request.status_code == 200:
                soup = BeautifulSoup(request.content, 'html.parser')
                return soup
            else:
                raise Exception(f"Failed to retrieve the page. Status code: {request.status_code}")
        

















if __name__ == "__main__":
    bw_static = BusinessWorldStatic("https://www.bworldonline.com/", "BusinessWorld")
    page = bw_static.open_category_page("corporate")
    bw_static.get_categories(page)
    for article in bw_static.get_articles(page):
        article_obj = BusinessWorldArticleScraper(article)()
    
        print(article_obj._title + "\n" + article_obj._date + "\n")
        print("========================================")
   