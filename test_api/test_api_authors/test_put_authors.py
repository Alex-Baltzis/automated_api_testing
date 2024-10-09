from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.author import Author

def test_update_an_existing_author():
    my_api_client = APIClient()
    id_to_update = 44
    book_id_to_update = 55
    updated_author_info = {"id": id_to_update,
                           "idBook": book_id_to_update,
                           "firstName": "updated first name",
                           "lastName": "updated last name"}
    response = my_api_client.put(f"Authors/{id_to_update}", data=updated_author_info)   
    assert response.status_code == 200
    response_book = Author(**response.json())
    expected_book = Author(**updated_author_info)
    assert response_book == expected_book
    
def test_update_a_non_existing_author():
    my_api_client = APIClient()
    id_to_update = 9999
    book_id_to_update = 789
    updated_author_info = {"id": id_to_update,
                           "idBook": book_id_to_update,
                           "firstName": "updated first name",
                           "lastName": "updated last name"}
    response = my_api_client.put(f"Authors/{id_to_update}", data=updated_author_info)   
    assert response.status_code == 200
    response_book = Author(**response.json())
    expected_book = Author(**updated_author_info)
    assert response_book == expected_book
    
def test_update_an_author_with_wrong_id():
    my_api_client = APIClient()
    new_author_info = {"idea": 222,
                       "idBook": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.put("Authors", data=new_author_info)   
    assert response.status_code == 405


def test_update_an_author_with_wrong_idBook():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "ideaBook": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.put("Authors", data=new_author_info)   
    assert response.status_code == 405   
    
def test_update_an_author_with_wrong_firstName():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "idBook": 300,
                       "fName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.put("Authors", data=new_author_info)   
    assert response.status_code == 405


def test_update_an_author_with_wrong_lastName():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "ideaBook": 300,
                       "firstName": "new first name",
                       "lName": "new last name"}
    response = my_api_client.put("Authors", data=new_author_info)   
    assert response.status_code == 405 
    
def test_update_an_author_with_wrong_id_value():
    my_api_client = APIClient()
    new_author_info = {"id": "222",
                       "idBook": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.put("Authors", data=new_author_info)   
    assert response.status_code == 405


def test_update_an_author_with_wrong_idBook_value():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "idBook": "300",
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.put("Authors", data=new_author_info)   
    assert response.status_code == 405   
    
def test_update_an_author_with_wrong_firstName_value():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "idBook": 300,
                       "firstName": 100,
                       "lastName": "new last name"}
    response = my_api_client.put("Authors", data=new_author_info)   
    assert response.status_code == 405


def test_update_an_author_with_wrong_lastName_value():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "ideaBook": 300,
                       "firstName": "new first name",
                       "lastName": 100}
    response = my_api_client.put("Authors", data=new_author_info)   
    assert response.status_code == 405 
    

