from snake.field import Field

import pytest


@pytest.fixture
def field():
    return Field(10, 10)
