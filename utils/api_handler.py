import requests

class APIHandler:
    """
    Handles API requests and response validation.
    """

    @staticmethod
    def get_request(url):
        """
        Sends a GET request to the given URL and returns the JSON response.

        :param url: API endpoint URL
        :return: JSON response
        """
        response = requests.get(url)
        
        # Ensure valid response
        if response.status_code != 200:
            raise ValueError(f"Error: Received status code {response.status_code}")

        return response.json()
