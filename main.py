def up(snake_pos):
    del snake_pos[-1]
    head = snake_pos[0]
    new_head = (head[0] + 1, head[1])
    snake_pos.insert(0, new_head)
    return snake_pos


def down(snake_pos):
    del snake_pos[-1]
    head = snake_pos[0]
    new_head = (head[0] - 1, head[1])
    snake_pos.insert(0, new_head)
    return snake_pos


def right(snake_pos):
    del snake_pos[-1]
    head = snake_pos[0]
    new_head = (head[0], head[1] + 1)
    snake_pos.insert(0, new_head)
    return snake_pos


def left(snake_pos):
    del snake_pos[-1]
    head = snake_pos[0]
    new_head = (head[0], head[1] - 1)
    snake_pos.insert(0, new_head)
    return snake_pos


def snake(board_size, snake_len, steps):
    snake = list(reversed([(0, i) for i in range(0, snake_len)]))
    current = 'right'
    for step in steps:
        current = step or current
        if current == "left":
            snake = left(snake)
        if current == "right":
            snake = right(snake)
        if current == "up":
            snake = up(snake)
        if current == "down":
            snake = down(snake)
    return snake



