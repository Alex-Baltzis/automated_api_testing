from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.author import Author

def test_create_an_author():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "idBook": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 200
    response_author = Author(**response.json())
    expected_author = Author(**new_author_info)
    assert response_author == expected_author
    
def test_create_an_author_with_wrong_id():
    my_api_client = APIClient()
    new_author_info = {"idea": 222,
                       "idBook": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400


def test_create_an_author_with_wrong_idBook():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "ideaBook": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400   
    
def test_create_an_author_with_wrong_firstName():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "idBook": 300,
                       "fName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400


def test_create_an_author_with_wrong_lastName():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "ideaBook": 300,
                       "firstName": "new first name",
                       "lName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400 
    
def test_create_an_author_with_wrong_id_value():
    my_api_client = APIClient()
    new_author_info = {"id": "haha",
                       "idBook": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400


def test_create_an_author_with_wrong_idBook_value():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "idBook": "hihi",
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400   
    
def test_create_an_author_with_wrong_firstName_value():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "idBook": 300,
                       "firstName": 100,
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400


def test_create_an_author_with_wrong_lastName_value():
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "ideaBook": 300,
                       "firstName": "new first name",
                       "lastName": 100}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400 


def test_create_an_author_with_no_id_value():
    my_api_client = APIClient()
    new_author_info = {"idBook": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 200
    new_author_info["id"] = 0
    new_author = Author(**new_author_info)
    response_author = Author(**response.json())
    assert response_author == new_author
    
    
def test_create_an_author_with_no_idbook_value():
    my_api_client = APIClient()
    new_author_info = {"id": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 200
    new_author_info["idBook"] = 0
    new_author = Author(**new_author_info)
    response_author = Author(**response.json())
    assert response_author == new_author
    
    
def test_create_an_author_with_no_firstName_value():
    my_api_client = APIClient()
    new_author_info = {"id": 300,
                       "idBook": 300,
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 200
    new_author_info["firstName"] = None
    new_author = Author(**new_author_info)
    response_author = Author(**response.json())
    assert response_author == new_author
    
    
def test_create_an_author_with_no_lastName_value():
    my_api_client = APIClient()
    new_author_info = {"id": 300,
                       "idBook": 300,
                       "firstName": "new first name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 200
    new_author_info["lastName"] = None
    new_author = Author(**new_author_info)
    response_author = Author(**response.json())
    assert response_author == new_author
