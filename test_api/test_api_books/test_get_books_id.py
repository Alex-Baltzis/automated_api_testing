from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.book import Book
from datetime import datetime


def test_get_book_by_id():
    my_api_client = APIClient()
    book_id = 1
    response = my_api_client.get(f"Books/{book_id}")
    assert response.status_code == 200
    book_response = Book(**response.json())
    expected_book = Book(id=book_id, 
                         title="Book 1",
                         description="Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\n",
                         pageCount=100,
                         excerpt=5*"Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\n",
                         publishDate=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"))
    assert book_response == expected_book
    
def test_get_non_existing_book():
    my_api_client = APIClient()
    non_existing_book_id = 10000
    response = my_api_client.get(f"Books/{non_existing_book_id}")
    assert response.status_code == 404
    
    
def test_get_book_by_id_invalid_id():
    my_api_client = APIClient()
    book_id = "jk"
    response = my_api_client.get(f"Books/{book_id}")
    assert response.status_code == 400
    
    
def test_get_book_by_id_zero_id():
    my_api_client = APIClient()
    book_id = 0
    response = my_api_client.get(f"Books/{book_id}")
    assert response.status_code == 404
    
    
def test_get_book_by_id_negative_id():
    my_api_client = APIClient()
    book_id = -2
    response = my_api_client.get(f"Books/{book_id}")
    assert response.status_code == 404
    