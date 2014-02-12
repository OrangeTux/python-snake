import pytest


def test_dimensions(field):
    """ Test if field has correct dimensions. """
    assert len(field.field) == field.width * field.height

    assert (0, field.height) not in field.field
    assert (field.width - 2, 0) in field.field


def test_get_cell_content(field):
    """ Test if get_cell() behaves correct. """
    x = y = 0
    field.field[(x, y)] = 'FOOD'

    assert field.get_cell_content(x, y) is 'FOOD'
    assert field.get_cell_content(x, y + 1) is None

    with pytest.raises(KeyError):
        field.get_cell_content(x, field.height)


def test_set_cell_content(field):
    """ Test if set_cell() behaves properly. """
    x = y = 0
    assert field.field[(x, y)] is None

    field.set_cell_content(x, y, 'FOOD')
    assert field.field[(x, y)] == 'FOOD'

    with pytest.raises(KeyError):
        field.set_cell_content(field.width, 0, 'FOOD')
