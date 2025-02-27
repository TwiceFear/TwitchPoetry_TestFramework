from utils.waits import Waits

class TwitchStreamerPage:
    """Represents the streamer page after selecting a Twitch streamer."""

    def __init__(self, driver):
        self.driver = driver

    def handle_popups(self):
        """Handles any popups that may appear when opening a stream."""
        try:
            popup_close_button = Waits.wait_for_clickable(self.driver, ('XPATH', '//button[contains(@aria-label, "Close")]'), timeout=5)
            popup_close_button.click()
        except Exception:
            pass  # No popups detected

    def wait_for_page_to_load(self):
        """Waits for the streamer page to fully load."""
        Waits.wait_for_page_to_load(self.driver)
