class ScreenshotHandler:
    """Handles taking screenshots for tests."""

    @staticmethod
    def take_screenshot(driver, filename):
        """Takes a screenshot and saves it."""
        driver.save_screenshot(filename)

