import pytest
import requests
import allure
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
POETRYDB_URL = os.getenv("POETRYDB_URL")

@pytest.mark.parametrize('endpoint, expected_key', [
    ('/title/Ozymandias', 'title'),
    ('/author/Shakespeare', 'author')
])
@allure.feature('API Testing')
def test_poetrydb_api(endpoint, expected_key):
    """Tests the PoetryDB API by verifying expected keys in the response."""
    
    url = f'{POETRYDB_URL}{endpoint}'
    response = requests.get(url)

    # Validate API response
    assert response.status_code == 200, "Expected status code 200"
    assert expected_key in response.json()[0], f"Expected key '{expected_key}' not found in response"
