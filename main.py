def move(snake_pos, dx=0, dy=0):
    del snake_pos[-1]
    head = snake_pos[0]
    new_head = (head[0] + dx, head[1] + dy)
    snake_pos.insert(0, new_head)
    return snake_pos


def snake(board_size, snake_len, steps):
    snake = list(reversed([(0, i) for i in range(0, snake_len)]))
    current = 'right'
    for step in steps:
        current = step or current
        if current == "left":
            snake = move(snake, dy=-1)
        if current == "right":
            snake = move(snake, dy=1)
        if current == "up":
            snake = move(snake, dx=1)
        if current == "down":
            snake = move(snake, dx=-1)
    return snake
