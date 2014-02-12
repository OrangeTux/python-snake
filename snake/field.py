class Field:
    """ A field keeps track of all positions on a field and the content of
    these posisions.

    :param length:  Length of the field.
    :param height:  The height of the field.

    """
    def __init__(self, length=10, height=10):
        self.length = 10
        self.height = 10

        self.field = create_field()

    def create_field(self):
        """ Creates a field based on the dimensions.

        :return:    Dict filled with (x, y) tuples as keys.

        """
        return {(x, y): None for x in range(self.length)
                for y in range(self.width)}

    def set_cell_content(self, x, y, content):
        """ Set content of a cell.

        :param x:       The x coordinate of the cell.
        :param y:       The y coordinate of the cell.
        :param content: The content for the cell.

        :raises: KeyError when coordinates are invalid.

        """
        cell = (x, y)
        if cell not in self.field:
            raise KeyError

        self.field[cell] = content

    def get_cell_content(self, x, y):
        """ Return content of a cell.

        :param x:   The x coordinate of the cell.
        :param y:   The y coordinate of the cell.

        :raises:    KeyError when coordinates are invalid.

        """
        return self.field[(x, y)]
