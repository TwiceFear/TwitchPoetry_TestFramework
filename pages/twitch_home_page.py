import time
from selenium.webdriver.common.by import By
from utils.waits import Waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class TwitchHomePage:
    """Represents the Twitch home page and its interactions."""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """Opens the Twitch mobile site."""
        self.driver.get(self.url)

    def click_browse(self):
        """Clicks the Browse button on the Twitch homepage."""
        self._wait_and_click((By.LINK_TEXT, 'Browse'))

    def click_search_icon(self):
        """Clicks the search icon."""
        self._wait_and_click((By.XPATH, '//input[@placeholder="Search"]'))

    def search_game(self, search_term):
        """Searches for a game in the search bar and selects the first result."""
        search_box = Waits.wait_for_element(self.driver, (By.XPATH, '//input[@placeholder="Search"]'))
        search_box.clear()
        search_box.send_keys(search_term)
        time.sleep(2)
        self._wait_and_click((By.XPATH, '//*[@id="page-main-content-wrapper"]/div/ul/li[1]'))

    def select_first_streamer(self):
        """Selects the first visible streamer after scrolling stops."""
        streamer_list_xpath = '//*[@id="page-main-content-wrapper"]/div[3]/div/div/div'
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, streamer_list_xpath))
        )

        retries = 3  # Retry 3 times in case of stale elements
        for _ in range(retries):
            try:
                streamers = self.driver.find_elements(By.XPATH, f"{streamer_list_xpath}/*")
                self._select_visible_streamer(streamers, streamer_list_xpath)
                return
            except StaleElementReferenceException:
                print("Detected stale element, retrying...")
                continue  # Retry if the list updates

        raise Exception("No visible streamer found on the screen.")

    def _select_visible_streamer(self, streamers, streamer_list_xpath):
        """Helper method to select the first visible streamer."""
        for streamer in streamers:
            streamer_xpath = f"{streamer_list_xpath}[{streamers.index(streamer) + 1}]/div/article/button/div/div[1]/img"
            streamer_element = self.driver.find_element(By.XPATH, streamer_xpath)

            if streamer_element.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", streamer_element)
                Waits.wait_for_clickable(self.driver, streamer_element).click()
                return

    def _wait_and_click(self, locator):
        """Waits for an element to be clickable and then clicks it."""
        Waits.wait_for_clickable(self.driver, locator).click()
