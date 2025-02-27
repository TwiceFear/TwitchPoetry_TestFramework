from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Scroller:
    """Provides scrolling functionality for mobile emulation in Selenium."""

    @staticmethod
    def scroll_down(driver, times=1):
        """Scrolls down a specified number of times."""
        for _ in range(times):
            ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
