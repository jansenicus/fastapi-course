import json


def test_create_user(client):
    data = {
        "username": "testusername",
        "email": "abc@test.com",
        "password": "1234567",
    }

    response = client.post("/users/",
                           json.dumps(data))

    assert response.status_code == 200, "something is not right"
    
