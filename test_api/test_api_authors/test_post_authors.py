from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.author import Author

def test_create_an_author():
    """
    Tests that the API creates an author with valid data
    """
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
    """
    Tests that the API does not create an author with a wrong id
    """
    my_api_client = APIClient()
    new_author_info = {"idea": 222,
                       "idBook": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400


def test_create_an_author_with_wrong_idBook():
    """
    Tests that the API does not create an author with a wrong idBook
    """
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "ideaBook": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400   
    
def test_create_an_author_with_wrong_firstName():
    """
    Tests that the API does not create an author with a wrong firstName
    """
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "idBook": 300,
                       "fName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400


def test_create_an_author_with_wrong_lastName():
    """
    Tests that the API does not create an author with a wrong lastName
    """
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "ideaBook": 300,
                       "firstName": "new first name",
                       "lName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400 
    
def test_create_an_author_with_wrong_id_value():
    """
    Tests that the API does not create an author with a wrong id value
    """
    my_api_client = APIClient()
    new_author_info = {"id": "haha",
                       "idBook": 300,
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400


def test_create_an_author_with_wrong_idBook_value():
    """
    Tests that the API does not create an author with a wrong idBook value
    """
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "idBook": "hihi",
                       "firstName": "new first name",
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400   
    
def test_create_an_author_with_wrong_firstName_value():
    """
    Tests that the API does not create an author with a wrong firstName value
    """
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "idBook": 300,
                       "firstName": 100,
                       "lastName": "new last name"}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400


def test_create_an_author_with_wrong_lastName_value():
    """
    Tests that the API does not create an author with a wrong lastName value
    """
    my_api_client = APIClient()
    new_author_info = {"id": 222,
                       "ideaBook": 300,
                       "firstName": "new first name",
                       "lastName": 100}
    response = my_api_client.post("Authors", data=new_author_info)   
    assert response.status_code == 400 


def test_create_an_author_with_no_id_value():
    """
    Tests that the API creates an author with no id value
    """
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
    """
    Tests that the API creates an author with no idBook value
    """
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
    """
    Tests that the API creates an author with no firstName value
    """
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
    """
    Tests that the API creates an author with no lastName value
    """
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
