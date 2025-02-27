import allure
from utils.screenshot import ScreenshotHandler
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def wait_for_streamer_page_and_screenshot(driver, streamer_page, search_term, timeout=30):
    """Waits for the streamer page to fully load, ensures video is playing, and captures a screenshot."""
    handle_initial_page_load(driver, streamer_page, timeout)
    ensure_video_is_playing(driver, timeout)
    capture_screenshot(driver, search_term)

def handle_initial_page_load(driver, streamer_page, timeout):
    """Handles initial page load and waits for the video player to be visible."""
    streamer_page.handle_popups()
    streamer_page.wait_for_page_to_load()
    video_player_xpath = "//*[@id='channel-live-overlay']/div/div/div[1]/div/div[1]/div/div[2]/div/div/div[2]"
    
    try:
        print("Waiting for the video player to load...")
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, video_player_xpath))
        )
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, video_player_xpath))
        )
        print("Video player is visible.")
    except Exception as e:
        raise Exception("Video did not load in time.") from e

def ensure_video_is_playing(driver, timeout):
    """Ensures the video is playing and not showing a black screen."""
    video_player_xpath = "//*[@id='channel-live-overlay']/div/div/div[1]/div/div[1]/div/div[2]/div/div/div[2]"
    
    try:
        print("Ensuring the video is playing (not blank)...")
        video_element = driver.find_element(By.XPATH, video_player_xpath)
        
        def has_rendered_frames():
            """Checks if the video has played at least a few frames."""
            return driver.execute_script(
                "return arguments[0].currentTime > 1;", video_element
            )
        
        WebDriverWait(driver, 5).until(lambda d: has_rendered_frames())
        print("Frames have rendered. Capturing screenshot now.")
    except Exception as e:
        print("Warning: Video might still be initializing, but proceeding with the screenshot.")

def capture_screenshot(driver, search_term):
    """Captures a screenshot and attaches it to the Allure report."""
    screenshot_path = f"twitch_streamer_{search_term}.png"
    ScreenshotHandler.take_screenshot(driver, screenshot_path)
    allure.attach.file(screenshot_path, name="Streamer Screenshot", attachment_type=allure.attachment_type.PNG)
    print(f"Screenshot saved: {screenshot_path}")  # Debugging log
