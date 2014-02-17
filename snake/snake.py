class Snake:
    """ Model for snake. It can move its head, tail and can grow.

    :param size:    The begin size of the snake.

    """
    def __init__(self, size=3):
        self.segments = list()
        for y in range(size - 1, -1, -1):
            self.segments.append((0, y))

    def get_location_head(self):
        """ Return the location of the head as a tuple.

        :return:    Tuple with x and y coordinate.

        """
        return self.segments[0]

    def get_location_tail(self):
        """ Return the location of the tail as a tuple.

        :return:    Tuple with x and y coordinate.

        """
        return self.segments[len(self.segments) - 1]

    def move_head(self, x, y):
        """ Move head to the snake to location.

        :param x:   The x coordinate of new location.
        :param y:   The y coordinate of the new location.

        """
        self.segments.insert(0, (x, y))

    def move_tail(self):
        """ Remove last segment of snake. """
        self.segments.pop()

    def move(self, x, y, grow=False):
        """ Move head and tail of snake.

        :param x:       The x coordinate of new location of the head.
        :param y:       The y coordinate of the new location of the head.
        :param grow:    If snake has to grow or not.

        """
        if not grow:
            self.move_tail()

        self.move_head(x, y)
