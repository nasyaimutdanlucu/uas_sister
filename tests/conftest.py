import os

os.environ["TESTING"] = "1"

import pytest
from fastapi.testclient import TestClient
from aggregator.main import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c