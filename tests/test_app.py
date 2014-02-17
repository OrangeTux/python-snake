import pytest

from snake.exceptions import SnakeIsDeadError
from snake import EAST, WEST, SNAKE, FOOD


def test_spawn_food(app):
    app.field.set_cell_content(0, 0, FOOD)
    location = app.spawn_food(0, 0)
    assert app.field.get_cell_content(location[0], location[1]) == FOOD


def test_spawn_snake(app):
    x, y = app.spawn_snake()
    assert app.field.get_cell_content(x, y) == SNAKE
    assert app.snake.get_location_head() == (x, y)


def calculate_location_snake_head(app):
    app.direction = app.EAST
    app.spawn_snake(0, 0)
    assert app.calculate_location_snake_head() == (0, 1)


def test_move_without_grow(app):
    app.spawn_snake(0, 0)
    app.direction = EAST

    app.move()
    assert app.field.get_cell_content(0, 0) is None
    assert app.field.get_cell_content(0, 1) is SNAKE
    assert app.snake.get_location_head() == (0, 1)
    assert app.snake.get_location_tail() == (0, 1)


def test_move_with_grow(app):
    app.spawn_snake(0, 0)
    app.spawn_food(0, 1)
    app.direction = EAST

    app.move()
    assert app.field.get_cell_content(0, 0) is SNAKE
    assert app.field.get_cell_content(0, 1) is SNAKE
    assert app.snake.get_location_head() == (0, 1)
    assert app.snake.get_location_tail() == (0, 0)


def test_invalid_move(app):
    app.spawn_snake(0, 0)
    app.direction = WEST

    with pytest.raises(SnakeIsDeadError):
        app.move()

    app.direction = EAST
    app.field.set_cell_content(0, 1, SNAKE)
    with pytest.raises(SnakeIsDeadError):
        app.move()
