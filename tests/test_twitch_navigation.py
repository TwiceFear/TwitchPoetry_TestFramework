import time
import pytest
import allure
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_streamer_page import TwitchStreamerPage
from utils.scroller import Scroller
from utils.screenshot import ScreenshotHandler
from dotenv import load_dotenv
import os

from utils.test_helpers import wait_for_streamer_page_and_screenshot

# Load environment variables
load_dotenv()
TWITCH_URL = os.getenv("TWITCH_URL")

@pytest.mark.parametrize('search_term', ['StarCraft II'])
@allure.feature('Twitch Navigation')
@allure.story('Search and open streamer page')
def test_twitch_navigation(driver, search_term):
    """Tests Twitch navigation from Browse to streamer page, ensuring UI elements are functional."""

    home_page = TwitchHomePage(driver, TWITCH_URL)
    streamer_page = TwitchStreamerPage(driver)

    # Step 1: Open Twitch and Click Browse
    home_page.open()
    home_page.click_browse()

    # Step 2: Click the Search Icon
    home_page.click_search_icon()

    # Step 3: Input Search Term
    home_page.search_game(search_term)

    # Slowing down drive for debugging purposes to confirm that scrolling is working
    #time.sleep(3)

    # Step 4: Scroll Down Twice
    Scroller.scroll_down(driver, 4)

    # Slowing down drive for debugging purposes to confirm selection of streamer after scrolling
    #time.sleep(3)

    # Step 5: Select First Streamer
    home_page.select_first_streamer()

    # Step 6: Wait for Streamer Page to Fully Load and Take Screenshot
    wait_for_streamer_page_and_screenshot(driver, streamer_page, search_term)
