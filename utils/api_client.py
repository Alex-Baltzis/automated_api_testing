import requests
from automated_api_testing.config.settings import BASE_URL

class APIClient:
    """
    A class to encapsulate the API client for the base_url parameter. The class
    methods are wrappers for the requests library methods.
    """

    def __init__(self, base_url=BASE_URL):
        """
        Initialize the API client with the base_url parameter.

        Args:
            base_url (str): the base URL for the API to be tested.
        """
        self.base_url = base_url

    def get(self, endpoint, params=None):
        """
        Perform a GET request to the given endpoint.

        Args:
            endpoint (str): the endpoint to be used for the GET request.
            params (dict): the parameters to be included in the request.

        Returns:
            requests.Response: the response from the GET request.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        return response

    def post(self, endpoint, data=None):
        """
        Perform a POST request to the given endpoint.

        Args:
            endpoint (str): the endpoint to be used for the POST request.
            data (dict): the data to be included in the request body.

        Returns:
            requests.Response: the response from the POST request.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data)
        return response

    def put(self, endpoint, data=None):
        """
        Perform a PUT request to the given endpoint.

        Args:
            endpoint (str): the endpoint to be used for the PUT request.
            data (dict): the data to be included in the request body.

        Returns:
            requests.Response: the response from the PUT request.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=data)
        return response

    def delete(self, endpoint):
        """
        Perform a DELETE request to the given endpoint.

        Args:
            endpoint (str): the endpoint to be used for the DELETE request.

        Returns:
            requests.Response: the response from the DELETE request.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url)
        return response
