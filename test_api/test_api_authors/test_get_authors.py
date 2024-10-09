from automated_api_testing.utils.api_client import APIClient
from automated_api_testing.utils.author import Author

def test_get_all_authors():
    my_api_client = APIClient()
    response = my_api_client.get("Authors")   
    assert response.status_code == 200
    # Cannot check for authors. Total number always changes.

