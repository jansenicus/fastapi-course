import json

def test_create_job(client):
    data = {
        "title": "Software Development Engineer I Yahoo",
        "company": "Testhoo",
        "company_url": "www.sumthin.com",
        "location": "New York",
        "description":"testing",
        "date_posted" : "2022-02-22"
    }

    response = client.post("/job/create-job", json.dumps(data))

    assert response.status_code == 200


def test_retrieve_job_by_id(client):
    data = {
        "title": "Software Development Engineer I Yahoo",
        "company": "Testhoo",
        "company_url": "www.sumthin.com",
        "location": "New York",
        "description":"testing",
        "date_posted" : "2022-02-22"
    }

    client.post("/job/create-job", json.dumps(data))
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json(), "No JSON Response"
    assert response.json()["title"] == data.get('title')
