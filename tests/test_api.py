from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_banks():
    response = client.get("/banks/")
    assert response.status_code == 200


def test_get_branches_for_nonexistent_bank():
    response = client.get("/banks/999999/branches")
    assert response.status_code == 404


def test_get_branch_by_invalid_ifsc():
    response = client.get("/branches/INVALIDIFSC")
    assert response.status_code == 404
