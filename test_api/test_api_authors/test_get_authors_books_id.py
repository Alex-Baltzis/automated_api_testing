from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.author import Author


def test_get_author_books():
    my_api_client = APIClient()
    book_id_to_get = 22
    response = my_api_client.get(f"Authors/authors/books/{book_id_to_get}")
    assert response.status_code == 200
    # I would also like to check the list of authors returned
    # But they are constantly changing, so I can only assure that this is list 
    # is compromised of dictionaries describing authors by creating an Author object for every dict in response.json()
    author_response_list  = [Author(**info) for info in response.json()]
    

def test_get_author_books_non_existing_book():
    my_api_client = APIClient()
    non_existing_book_id = 10000
    response = my_api_client.get(f"Authors/authors/books/{non_existing_book_id}")
    assert response.status_code == 200
    assert not response.json()
    
    
def test_get_author_books_with_invalid_id():
    my_api_client = APIClient()
    book_id = "jk"
    response = my_api_client.get(f"Authors/authors/books/{book_id}")
    assert response.status_code == 400
    
    
def test_get_author_books_zero_id():
    my_api_client = APIClient()
    book_id = 0
    response = my_api_client.get(f"Authors/authors/books/{book_id}")
    assert response.status_code == 200
    assert not response.json()
    
    
def test_get_author_books_negative_id():
    my_api_client = APIClient()
    book_id = -2
    response = my_api_client.get(f"Authors/authors/books/{book_id}")
    assert response.status_code == 200
    assert not response.json()
