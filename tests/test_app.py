from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
SECRETS = ROOT / "config" / "secrets.yml"


@pytest.fixture(scope="session")
def client():
    created = False
    if not SECRETS.exists():
        # ponytail: plain mongodb:// URI so MongoClient stays lazy (no SRV lookup at import)
        SECRETS.write_text(
            "mongodb:\n"
            "  host: localhost\n"
            "  port: 27017\n"
            "  database: bms_test\n"
            "  connection_string: mongodb://localhost:27017/bms_test\n"
        )
        created = True
    from main import app

    yield TestClient(app)
    if created:
        SECRETS.unlink()


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
