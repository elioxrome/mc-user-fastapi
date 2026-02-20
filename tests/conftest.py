from pathlib import Path
import sys

import pytest
from fastapi.testclient import TestClient

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import app.dependencies as dependencies
from app.infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from app.main import app


@pytest.fixture(autouse=True)
def reset_in_memory_repository() -> None:
    dependencies.user_repository = InMemoryUserRepository()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
