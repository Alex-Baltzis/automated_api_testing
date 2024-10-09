from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.author import Author

    
def test_get_author_by_id():
    my_api_client = APIClient()
    id_to_get = 1
    response = my_api_client.get(f"Authors/{id_to_get}")
    assert response.status_code == 200
    author_response = Author(**response.json())
    expected_author_info = {"id": 1,
                            "idBook": 1,
                            "firstName": "First Name 1",
                            "lastName": "Last Name 1"}
    expected_author = Author(**expected_author_info)
    assert author_response == expected_author
    
    
def test_get_non_existing_author():
    my_api_client = APIClient()
    non_existing_author_id = 10000
    response = my_api_client.get(f"Authors/{non_existing_author_id}")
    assert response.status_code == 404
    
    
def test_get_author_by_id_invalid_id():
    my_api_client = APIClient()
    author_id = "jk"
    response = my_api_client.get(f"Authors/{author_id}")
    assert response.status_code == 400
    
    
def test_get_author_by_id_zero_id():
    my_api_client = APIClient()
    author_id = 0
    response = my_api_client.get(f"Authors/{author_id}")
    assert response.status_code == 404
    
    
def test_get_author_by_id_negative_id():
    my_api_client = APIClient()
    author_id = -2
    response = my_api_client.get(f"Authors/{author_id}")
    assert response.status_code == 404    

