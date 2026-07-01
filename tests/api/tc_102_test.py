import requests

BASE_URL = "<API_BASE_URL_PLACEHOLDER>"
REQUEST_TIMEOUT = 30
BEARER_TOKEN = "<VALID_BEARER_TOKEN_PLACEHOLDER>"

def test_e350_001_create_customer():
    """Create a new customer via POST API"""
    # Traceability: TC-102 | KAN-350 | 

    # Step 1: Send a POST request to /api/v1/customers with JSON body: {"first_name": "John", "last_name": "Doe", "email": "john.doe@test.com"} and Authorization header with Bearer token.
    url = f"{BASE_URL}/api/v1/customers"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@test.com"
    }
    response = requests.post(url, json=payload, headers=headers, timeout=REQUEST_TIMEOUT)

    # Expected: Response status code is 201. Response body contains "id" field with a non-null value and "email" field matching "john.doe@test.com".
    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data and response_data["id"] is not None
    assert response_data["email"] == "john.doe@test.com"

    # Step 2: Send a GET request to /api/v1/customers/{id} using the id from Step 1 response, with the same Authorization header.
    customer_id = response_data["id"]
    url = f"{BASE_URL}/api/v1/customers/{customer_id}"
    response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)

    # Expected: Response status code is 200. Response body "first_name" is "John" and "last_name" is "Doe".
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["first_name"] == "John"
    assert response_data["last_name"] == "Doe"