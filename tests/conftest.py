import pytest
from services import players


@pytest.fixture
def client():
    """
    :return: app for testing
    """
    client = players.app.test_client()
    yield client
