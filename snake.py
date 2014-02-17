#!/usr/bin/env python
from snake import App
from snake.field import Field
from snake.snake import Snake


if __name__ == '__main__':
    field = Field()
    snake = Snake()

    app = App(field, snake)
    app.spawn_snake()
    app.spawn_food()
    app.run()
