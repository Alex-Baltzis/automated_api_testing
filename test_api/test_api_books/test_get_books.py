from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.book import Book
from datetime import datetime

def test_get_all_books():
    my_api_client = APIClient()
    response = my_api_client.get("Books")   
    assert response.status_code == 200
    total_books = len(response.json())
    assert total_books == 200
    