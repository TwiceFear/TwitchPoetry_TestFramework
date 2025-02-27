import pytest
from utils.webdriver_setup import WebDriverSetup
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='session')
def driver():
    """Fixture to initialize and quit the WebDriver session."""
    driver = WebDriverSetup.get_mobile_chrome_driver()
    yield driver
    driver.quit()
