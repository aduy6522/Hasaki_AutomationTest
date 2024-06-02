import pytest

@pytest.fixture(scope="module")
def search_data():
    return [
        ("skincare"),
        ("makeup")
    ]