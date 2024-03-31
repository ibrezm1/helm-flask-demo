import os
import pytest
import requests
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    # Make a GET request to the '/' route
    response = client.get('/')

    # Check that the response status code is 200 OK
    assert response.status_code == 200

    # Check that the response body contains the expected message
    assert response.data.decode('utf-8') == "Hello from our Kubernetes demo app with Flask!"

def test_env_variables_route(client):
    # Set up environment variables
    os.environ['PUBLIC_VARIABLE'] = 'PublicValue'
    os.environ['SECRET_VARIABLE'] = 'SecretValue'

    # Make a GET request to the '/env_variables' route
    response = client.get('/env_variables')

    # Check that the response status code is 200 OK
    assert response.status_code == 200

    # Check that the response body contains the expected environment variables
    expected_response = "Public variable: PublicValue\nSecret variable: SecretValue"
    assert response.data.decode('utf-8') == expected_response

    # Clean up environment variables
    del os.environ['PUBLIC_VARIABLE']
    del os.environ['SECRET_VARIABLE']
