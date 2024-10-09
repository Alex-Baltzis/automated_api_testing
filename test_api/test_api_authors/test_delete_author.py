from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.author import Author

def test_delete_an_existing_author():
    my_api_client = APIClient()
    id_to_delete = 33
    response = my_api_client.delete(f"Authors/{id_to_delete}")   
    assert response.status_code == 200

def test_delete_non_existing_author():
    my_api_client = APIClient()
    non_existing_author_id = 10000
    response = my_api_client.delete(f"Authors/{non_existing_author_id}")
    assert response.status_code == 404
    
    
def test_delete_author_by_id_invalid_id():
    my_api_client = APIClient()
    author_id = "jk"
    response = my_api_client.delete(f"Authors/{author_id}")
    assert response.status_code == 400
    
    
def test_delete_author_by_id_zero_id():
    my_api_client = APIClient()
    author_id = 0
    response = my_api_client.delete(f"Authors/{author_id}")
    assert response.status_code == 404
    
    
def test_delete_author_by_id_negative_id():
    my_api_client = APIClient()
    author_id = -2
    response = my_api_client.delete(f"Authors/{author_id}")
    assert response.status_code == 404  

