from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.book import Book
from datetime import datetime

def test_update_an_existing_book():
    """
    Tests that the API updates an existing book by given id
    """
    my_api_client = APIClient()
    id_to_update = 22
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    updated_book_info = {"id": id_to_update,
                             "title": "updated_book",
                             "description": "desc",
                             "pageCount": 33,
                             "excerpt": "excerpt string",
                             "publishDate": current_time}
    response = my_api_client.put(f"Books/{id_to_update}", data=updated_book_info)   
    assert response.status_code == 200
    response_book = Book(**response.json())
    expected_book = Book(**updated_book_info)
    assert response_book == expected_book
    
    
def test_update_a_book_with_wrong_id_body():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"idea": 222,
                         "title": "updated_book",
                         "description": "desc",
                         "pageCount": 33,
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405


def test_update_a_book_with_wrong_title_body():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "tit": "updated_book",
                         "description": "desc",
                         "pageCount": 33,
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405   
    
    
def test_update_a_book_with_wrong_description_body():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "desc": "desc",
                         "pageCount": 33,
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405


def test_update_a_book_with_wrong_pageCount_body():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "description": "desc",
                         "pc": 33,
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405
    
    
def test_update_a_book_with_wrong_excerpt_body():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "description": "desc",
                         "pageCount": 33,
                         "exc": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405 
    
    
def test_update_a_book_with_wrong_publishDate_body():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "description": "desc",
                         "pageCount": 33,
                         "excerpt": "excerpt string",
                         "pub": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405 
    
    
def test_update_a_book_with_negative_id_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": -1,
                         "title": "updated_book",
                         "description": "desc",
                         "pageCount": 33,
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405
    
    
def test_update_a_book_with_no_id_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"title": "updated_book",
                         "description": "desc",
                         "pageCount": 33,
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405


def test_update_a_book_with_wrong_title_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": 464,
                         "description": "desc",
                         "pageCount": 33,
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405   
    
    
def test_update_a_book_with_no_title_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 56,
                         "description": "desc",
                         "pageCount": 33,
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405
    
def test_update_a_book_with_wrong_description_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "description": 466,
                         "pageCount": 33,
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405
    
    
def test_update_a_book_with_no_description_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "pageCount": 33,
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405
    
    
def test_update_a_book_with_negative_pagecount_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "description": 466,
                         "pageCount": -33,
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405
    
    
def test_update_a_book_with_no_pagecount_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "description": "desc",
                         "excerpt": "excerpt string",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405
    
    
def test_update_a_book_with_wrong_excerpt_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "description": "desc",
                         "pageCount": 33,
                         "excerpt": 654,
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405
    
    
def test_update_a_book_with_no_excerpt_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "pageCount": 33,
                         "description": "desc",
                         "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405
    
    
def test_update_a_book_with_wrong_publishdate_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "description": "desc",
                         "pageCount": 33,
                         "excerpt": "excerpt",
                         "publishDate": 123}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405
    
    
def test_update_a_book_with_no_publishdate_value():
    """
    Tests that the API returns 405 if the body is wrong
    """
    my_api_client = APIClient()
    updated_book_info = {"id": 222,
                         "title": "updated_book",
                         "pageCount": 33,
                         "description": "desc",
                         "excerpt": "excerpt"}
    response = my_api_client.put("Books", data=updated_book_info)   
    assert response.status_code == 405
    