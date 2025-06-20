from flask_main import main

def test_home():
    tester = main.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello from GitHub Actions!" in response.data
