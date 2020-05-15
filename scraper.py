from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Scraper:
    """Handles all scraping logic"""

    def __init__(self):
        chrome_config = Options()
        chrome_config.add_argument("--disable-gpu")
        chrome_config.add_argument("--disable-extensions")
        chrome_config.add_argument('--no-sandbox')
        chrome_config.add_argument('disable-infobars')
        chrome_config.add_argument('start-maximized')

        self.driver = webdriver.Chrome(
            options=chrome_config,
            executable_path='./chromedriver'
        )

        self.driver.get("https://www.imdb.com/chart/top/")
        self.parser = BeautifulSoup(self.driver.page_source, 'html.parser')

    def getData(self) -> dict:
        """
        Scrapes the Top 100 movies of the IMDB page and returns
        a dictionary containing the data
        """
        pass

