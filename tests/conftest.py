from snake import App
from snake.field import Field
from snake.snake import Snake

import pytest


@pytest.fixture
def field():
    return Field(10, 10)


@pytest.fixture
def snake():
    return Snake()


@pytest.fixture
def app(snake, field):
    return App(field, snake)
