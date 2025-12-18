from fastapi.testclient import TestClient
from app.main import app

# Create a new TestClient for each test
def test_get_banks():
    client = TestClient(app)
    response = client.get("/banks/")
    assert response.status_code == 200

def test_get_branches_for_nonexistent_bank():
    client = TestClient(app)
    response = client.get("/banks/999999/branches")
    assert response.status_code == 404

def test_get_branch_by_invalid_ifsc():
    client = TestClient(app)
    response = client.get("/branches/INVALIDIFSC")
    assert response.status_code == 404
