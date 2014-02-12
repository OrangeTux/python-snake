from snake.snake import Snake
from copy import copy


def test_amount_of_segments():
    """ Test amount of segments of snake. """
    s = Snake(size=3)
    assert len(s.segments) is 3


def test_move_head(snake):
    """ Test move_head(). """
    x = 0
    y = 3
    old_segments = copy(snake.segments)

    snake.move_head(x, y)
    assert len(snake.segments) is len(old_segments) + 1
    assert snake.segments[0] == (x, y)


def test_move_tail(snake):
    """ Test move_tail(). """
    old_segments = copy(snake.segments)

    snake.move_tail()
    assert old_segments.pop() not in snake.segments
    assert old_segments == snake.segments
    assert len(snake.segments) is 2


def test_move_with_grow(snake):
    """ Test if snake moves correctly. """
    old_segments = copy(snake.segments)
    snake.move(0, 3, grow=True)

    # Snake hasn't grew, so body is same size.
    assert len(snake.segments) is len(old_segments) + 1
    # Head is now placed on te new location.
    assert snake.segments[0] == (0, 3)
    # Previous head is now second segment.
    assert old_segments[0] is snake.segments[1]
    # The tail is not on same location.
    assert old_segments.pop() in snake.segments

def test_move_without_grow(snake):
    """ Test if snake moves correctly. """
    old_segments = copy(snake.segments)
    snake.move(0, 3, grow=False)

    # Snake hasn't grew, so body is same size.
    assert len(snake.segments) is len(old_segments)
    # Head is now placed on te new location.
    assert snake.segments[0] == (0, 3)
    # Previous head is now second segment.
    assert old_segments[0] is snake.segments[1]
    # The tail is not on same location.
    assert old_segments.pop() not in snake.segments
