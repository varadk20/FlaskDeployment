from app import app

def test_home():
    response = app.test_client().get('/')

    assert response.status_code == 200
    # checks if the response data matches the expected output
    assert response.data == b"Deployment of flask web app using Docker and Github Actions"