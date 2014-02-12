import pytest


def test_dimensions(field):
    """ Test if field has correct dimensions. """
    assert len(field, field) == field.width * field.height

    assert (0, field.height) not in field.field
    assert (field.weight - 2, 0) in field.field


def get_cell_content(field):
    """ Test if get_cell() behaves correct. """
    cell = (0, 0)
    field[cell] = 'FOOD'

    assert field.get_cell_content((0, 1)) == None

    assert pytest.raises(KeyError):
        field.get_cell_content((0, field.height))


def set_cell_content(field):
    """ Test if set_cell() behaves properly. """
    cell = (0, 0)
    assert field[cell] = None

    field.set_cell_content(cell, 'FOOD')
    assert field[cell] = 'FOOD'
