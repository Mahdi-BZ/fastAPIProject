from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)



def test_create_task_with_valid_input():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK