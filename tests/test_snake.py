from snake.snake import Snake


def test_amount_of_segments():
    """ Test amount of segments of snake. """
    s = Snake(length=3)
    assert len(s.segments) is 3


def test_move_head(snake):
    """ Test move_head(). """
    x = 0
    y = 3
    old_segments = snake.segments

    snake.move_head(x, y)
    assert snake.segments is len(old_segments) + 1
    assert snake.segements[0] is (x, y)


def test_move_tail(snake):
    """ Test move_tail(). """
    old_segments = snake.segments

    snake.move_tail()
    assert old_segments.pop() not in snake.segments
    assert old_segments in snake.segments
    assert len(snake.segments) is 2


def test_move_with_grow(snake):
    """ Test if snake moves correctly. """
    old_segments = snake.segments
    snake.move(0, 3, grow=True)

    # Snake hasn't grew, so body is same size.
    assert len(snake.segments) + 1 is len(old_segments)
    # Head is now placed on te new location.
    assert snake.segments[0] is (0, 3)
    # Previous head is now second segment.
    assert old_segments[1] is snake.segments[0]
    # The tail is not on same location.
    assert old_segments.pop() in snake.segments
