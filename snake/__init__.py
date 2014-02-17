from random import randint

from snake.exceptions import SnakeIsDeadError


SNAKE = '1'
FOOD = '2'

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)


class App():
    """ The controller for the game. """
    def __init__(self, field, snake):
        self.field = field
        self.snake = snake
        self.direction = WEST

    def spawn_food(self, x=None, y=None):
        """ Spawn food in the field.

        :return:    A tuple with the coordinates of the spawn point.

        """
        x = randint(0, self.field.width - 1) if x is None else x
        y = randint(0, self.field.height - 1) if y is None else y

        if self.field.get_cell_content(x, y) is None:
            self.field.set_cell_content(x, y, FOOD)
            return x, y

        return self.spawn_food()

    def spawn_snake(self, x=None, y=None):
        """ Spawn the snake in the field.

        :return:    A tuple with coordinates of spawn point.

        """
        x = int((self.field.width - 1) / 2) if x is None else x
        y = int((self.field.height - 1) / 2) if y is None else y

        self.field.set_cell_content(x, y, SNAKE)
        self.snake.segments = [(x, y)]

        return x, y

    def calculate_location_snake_head(self):
        """ Return the new location of the snake head when snake moves 1 cell
        in self.direction. """
        location = self.snake.get_location_head()
        new_x = location[0] + self.direction[0]
        new_y = location[1] + self.direction[1]

        return new_x, new_y

    def move(self):
        """ Do one move. """
        x, y = self.calculate_location_snake_head()

        # When the snake hits a wall, he is dead.
        try:
            content = self.field.get_cell_content(x, y)
        except KeyError:
            raise SnakeIsDeadError()

        grow = False
        # When the snake bites its self, he is dead.
        if content == SNAKE:
            raise SnakeIsDeadError()

        if content == FOOD:
            grow = True

        # When the snakes tail doesn't grow, the tail has to be removed from
        # the field.
        if grow is False:
            tail_x, tail_y = self.snake.get_location_tail()
            self.field.set_cell_content(tail_x, tail_y, None)

        self.field.set_cell_content(x, y, SNAKE)
        self.snake.move(x, y, grow=grow)
        self.spawn_food()
