from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple

class Waits:
    """
    Provides explicit wait methods for Selenium interactions.
    """

    @staticmethod
    def wait_for_element(driver: WebDriver, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        """
        Waits for an element to be present in the DOM.

        :param driver: WebDriver instance
        :param locator: Tuple (By.XPATH, 'xpath_value')
        :param timeout: Time to wait before throwing TimeoutException
        :return: WebElement
        """
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

    @staticmethod
    def wait_for_clickable(driver: WebDriver, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        """
        Waits for an element to be clickable.

        :param driver: WebDriver instance
        :param locator: Tuple (By.XPATH, 'xpath_value')
        :param timeout: Time to wait before throwing TimeoutException
        :return: WebElement
        """
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

    @staticmethod
    def wait_for_page_to_load(driver: WebDriver, timeout: int = 10) -> None:
        """
        Waits until the page is fully loaded by checking for 'document.readyState'.

        :param driver: WebDriver instance
        :param timeout: Time to wait before throwing TimeoutException
        """
        WebDriverWait(driver, timeout).until(lambda d: d.execute_script("return document.readyState") == "complete")
