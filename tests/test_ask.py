from fastapi.testclient import TestClient
from runbookragas.main import app

client = TestClient(app)


def test_answers_and_refuses():
    hit = client.post("/ask", json={"question": 'How long does database failover take?'}).json()
    assert hit["answered"] is True
    assert hit["citation"] == "runbook.md"
    miss = client.post("/ask", json={"question": 'orbital mechanics homework'}).json()
    assert miss["answered"] is False


def test_empty_is_refused():
    assert client.post("/ask", json={"question": " "}).status_code == 422
