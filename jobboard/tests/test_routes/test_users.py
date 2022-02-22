import json


def test_create_user(client):
    data = {
        "username": "test",
        "email": "abc@test.com",
        "password": "1234567",
    }

    response = client.post("/user/",
                           json.dumps(data))

    assert response.status_code == 200
    assert response.json()["email"] == data.get("email")
    assert response.json()["is_active"] == True
    
