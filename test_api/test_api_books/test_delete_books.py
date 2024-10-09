from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.book import Book

def test_delete_an_existing_book():

    my_api_client = APIClient()
    id_to_delete = 22
    response = my_api_client.delete(f"Books/{id_to_delete}")   
    assert response.status_code == 200
    
    
def test_delete_non_existing_book():
    my_api_client = APIClient()
    non_existing_book_id = 10000
    response = my_api_client.delete(f"Books/{non_existing_book_id}")
    assert response.status_code == 404
    
    
def test_delete_book_by_id_invalid_id():
    my_api_client = APIClient()
    book_id = "jk"
    response = my_api_client.delete(f"Books/{book_id}")
    assert response.status_code == 400
    
    
def test_delete_book_by_id_zero_id():
    my_api_client = APIClient()
    book_id = 0
    response = my_api_client.delete(f"Books/{book_id}")
    assert response.status_code == 404
    
    
def test_delete_book_by_id_negative_id():
    my_api_client = APIClient()
    book_id = -2
    response = my_api_client.delete(f"Books/{book_id}")
    assert response.status_code == 400

    

