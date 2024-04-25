from fastapi.testclient import TestClient
from fastapi_todo.main import app



def test_root_path():
    client=TestClient(app=app)
    response=client.get("/")
    assert response.status_code==200
    assert response.json()== {"Hello":"World"}



def test_piaic_description():
    client=TestClient(app=app)
    response=client.get("/piaic/")
    assert response.status_code==200
    assert response.json()=={"Organization":"PIAIC"}

