from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverSetup:
    """Handles WebDriver configuration for mobile emulation."""

    @staticmethod
    def get_mobile_chrome_driver():
        """Sets up a Chrome mobile emulator driver."""
        mobile_emulation = {"deviceName": "Pixel 2"}
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        #chrome_options.add_argument("--headless=new")
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver
