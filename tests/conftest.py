import copy

from fastapi.testclient import TestClient
import pytest

from src.app import app, activities


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(copy.deepcopy(original_activities))


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def sample_activity():
    return "Chess Club"


@pytest.fixture
def sample_email():
    return "test.student@mergington.edu"
