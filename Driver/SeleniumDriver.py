
import undetected_chromedriver as uc

from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait



class Driver:
    def __init__(self):
        self._driver = None
        self._chrome_options = Options()
        self._chrome_args = [
            "--disable-gpu",
            "--ignore-certificate-errors",
            "--ignore-ssl-errors=yes",
            "--disable-web-security",
            "--allow-running-insecure-content",
            "--log-level=3",
            "--no-sandbox",
            "--enable-unsafe-swiftshader",
            "--disable-dev-shm-usage",
            "--window-size=1920,1080",
            "--disable-browser-side-navigation",
            "--disable-features=VizDisplayCompositor",
            "--disable-blink-features=AutomationControlled",
            "--disable-extensions",
            "--disable-infobars",
            # "--headless=new",  # Uncomment if needed
        ]
        self._ua = UserAgent()
        self.start()
        self.wait = WebDriverWait(self.driver, 30, poll_frequency=0.5)

    def start(self):
        self._chrome_options.add_extension(r"D:\PythonProjects\PH-Business-News-Updates-Automation\adblocker.crx")
        for arg in self._chrome_args:
            self._chrome_options.add_argument(arg)

        # Initialize the WebDriver
        self.driver = uc.Chrome(
            version_main=135, options=self._chrome_options, use_subprocess=True
        )
        self.driver.execute_cdp_cmd(
            "Network.setUserAgentOverride",
            {"userAgent": self._ua.random},  # Pass the User-Agent as a dictionary
        )

        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        self.driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            """
            },
        )
