from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.book import Book

def test_create_a_book():
    """
    Tests that the API creates a book with valid data
    """
    my_api_client = APIClient()
    book_info = {"id": 222,
                 "title": "new_post_book",
                 "description": "desc",
                 "pageCount": 33,
                 "excerpt": "excerpt string",
                 "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=book_info)   
    assert response.status_code == 200
    response_book = Book(**response.json())
    expected_book = Book(**book_info)
    assert response_book == expected_book
    
def test_create_a_book_with_wrong_id_body():
    """
    Tests that the API returns 400 if the body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"idea": 222,
                     "title": "new_post_book",
                     "description": "desc",
                     "pageCount": 33,
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400


def test_create_a_book_with_wrong_title_body():
    """
    Tests that the API returns 400 if the body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "tit": "new_post_book",
                     "description": "desc",
                     "pageCount": 33,
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400   
    
    
def test_create_a_book_with_wrong_description_body():
    """
    Tests that the API returns 400 if the body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "desc": "desc",
                     "pageCount": 33,
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400


def test_create_a_book_with_wrong_pageCount_body():
    """
    Tests that the API returns 400 if the body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "description": "desc",
                     "pc": 33,
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400 
    
    
def test_create_a_book_with_wrong_excerpt_body():
    """
    Tests that the API returns 400 if the body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "description": "desc",
                     "pc": 33,
                     "exc": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400 
    
    
def test_create_a_book_with_wrong_publishDate_body():
    """
    Tests that the API returns 400 if the body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "description": "desc",
                     "pc": 33,
                     "excerpt": "excerpt string",
                     "pub": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400 
    
    
def test_create_a_book_with_negative_id_value():
    """
    Tests that the API returns 400 if the body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"id": -1,
                     "title": "new_post_book",
                     "description": "desc",
                     "pageCount": 33,
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400
    
    
def test_create_a_book_with_no_id_value():
    """
    Tests that the API creates a book with valid data
    """
    my_api_client = APIClient()
    new_book_info = {"title": "new_post_book",
                     "description": "desc",
                     "pageCount": 33,
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 200
    new_book_info["id"] = 0
    new_book = Book(**new_book_info)
    response_book = Book(**response.json())
    assert response_book == new_book


def test_create_a_book_with_wrong_title_value():
    """
    Tests that the API returns 400 if the body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": 464,
                     "description": "desc",
                     "pageCount": 33,
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400   
    
    
def test_create_a_book_with_no_title_value():
    """
    Tests that the API creates a book with valid data
    """
    my_api_client = APIClient()
    new_book_info = {"id": 56,
                     "description": "desc",
                     "pageCount": 33,
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 200
    new_book_info["title"] = None
    new_book = Book(**new_book_info)
    response_book = Book(**response.json())
    assert response_book == new_book
    
def test_create_a_book_with_wrong_description_value():
    """
    Tests that the API returns 400 if the body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "description": 466,
                     "pageCount": 33,
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400
    
    
def test_create_a_book_with_no_description_value():
    """
    Tests that the API creates a book with valid data
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "pageCount": 33,
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 200
    new_book_info["description"] = None
    new_book = Book(**new_book_info)
    response_book = Book(**response.json())
    assert response_book == new_book
    
    
def test_create_a_book_with_negative_pagecount_value():
    """
    Tests that the API returns 400 if the body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "description": "desc",
                     "pageCount": -33,
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400
    
    
def test_create_a_book_with_no_pagecount_value():
    """
    Tests that the API creates a book with valid data
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "description": "desc",
                     "excerpt": "excerpt string",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 200
    new_book_info["pageCount"] = 0
    new_book = Book(**new_book_info)
    response_book = Book(**response.json())
    assert response_book == new_book
    
    
def test_create_a_book_with_wrong_excerpt_value():
    """
    Tests that the API returns 400 if the excerpt body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "description": "desc",
                     "pageCount": 33,
                     "excerpt": 654,
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400
    
    
def test_create_a_book_with_no_excerpt_value():
    """
    Tests that the API creates a book when excerpt is missing
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "pageCount": 33,
                     "description": "desc",
                     "publishDate": "2024-10-09T09:31:42.330000"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 200
    new_book_info["excerpt"] = None
    new_book = Book(**new_book_info)
    response_book = Book(**response.json())
    assert response_book == new_book
    
    
def test_create_a_book_with_wrong_publishdate_value():
    """
    Tests that the API returns 400 if the publishDate body is wrong
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "description": "desc",
                     "pageCount": 33,
                     "excerpt": "excerpt",
                     "publishDate": 123}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 400
    
    
def test_create_a_book_with_no_publishdate_value():
    """
    Tests that the API creates a book when publishDate is missing
    """
    my_api_client = APIClient()
    new_book_info = {"id": 222,
                     "title": "new_post_book",
                     "pageCount": 33,
                     "description": "desc",
                     "excerpt": "excerpt"}
    response = my_api_client.post("Books", data=new_book_info)   
    assert response.status_code == 200
    new_book_info["publishDate"] = "0001-01-01T00:00:00"
    assert new_book_info == response.json()
