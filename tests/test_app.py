import pytest

from app.exceptions import SnakeIsDeadError


def test_spawn_food(app):
    location = app.spawn_food()
    assert app.field.get_cell_content(location[0], location[1]) == app.FOOD


def test_spawn_snake(app):
    location = app.spawn_snake()
    assert app.field.get_cell_content(location[0], location[1]) == app.SNAKE
    assert app.snake.get_head() == location


def calculate_location_snake_head(app):
    app.direction = app.EAST
    app.spawn_snake(0, 0)
    assert app.calculate_location_snake_head() == (0, 1)


def test_move_without_grow(app):
    app.spawn_snake(0, 0)
    app.direction = app.EAST

    app.move()
    assert app.field.get_cell_content(0, 0) is None
    assert app.field.get_cell_content(0, 1) is app.SNAKE
    assert app.snake.get_location_head() == (0, 1)
    assert app.snake.get_location_tail() == (0, 1)


def test_move_with_grow(app):
    app.spawn_snake(0, 0)
    app.spawn_food(0, 1)
    app.direction = app.EAST

    app.move()
    assert app.field.get_cell_content(0, 0) is app.SNAKE
    assert app.field.get_cell_content(0, 1) is app.SNAKE
    assert app.snake.get_location_head() == (0, 1)
    assert app.snake.get_location_tail() == (0, 0)


def test_invalid_move(app):
    app.spawn_snake(0, 0)
    app.direction = app.WEST

    with pytest.raises(SnakeIsDeadError):
        app.move()
