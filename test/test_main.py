from main import snake, up


def test_snake():
    assert snake(8, 2, [0, "up", 0, "right", 0, "up", "left"]) == [(3, 3), (3, 4)]
    assert snake(8, 3, ["right", "right", "right", "up", "up"]) == [(2, 5), (1, 5), (0, 5)]


def test_up():
    assert up([(0, 2), (0, 1), (0, 0)]) == [(1, 2), (0, 2), (0, 1)]
    assert up([(5, 4), (5, 5), (5, 6), (6, 6), (7, 6)]) == [(6, 4), (5, 4), (5, 5), (5, 6), (6, 6)]
