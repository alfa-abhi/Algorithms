def change_direction(dx, dy):
    if abs(dx+dy) != 1:
        raise ValueError
    if dy == 0:
        return dy, dx
    if dx == 0:
        return -dy, dx


def print_spiral(N, M):
    if N <= 0 or M <= 0:
        return None
    dx, dy = 1, 0
    x, y = 0, 0
    start = 1
    max_digits = len(str(N*M-1))
    left_bound, right_bound = 0, N-1
    upper_bound, bottom_bound = 1, M-1
    matrix = [[0 for i in range(N)] for j in range(M)]
    for not_use in range(N*M):
        matrix[y][x] = start
        if dx > 0 and x >= right_bound:
            dx, dy = change_direction(dx, dy)
            right_bound -= 1
        if dx < 0 and x <= left_bound:
            dx, dy = change_direction(dx, dy)
            left_bound += 1
        if dy > 0 and y >= bottom_bound:
            dx, dy = change_direction(dx, dy)
            bottom_bound -= 1
        if dy < 0 and y <= upper_bound:
            dx, dy = change_direction(dx, dy)
            upper_bound += 1
        x += dx
        y += dy
        start += 1
    print('\n'.join([' '.join(['{:0{pad}d}'.format(val, pad=max_digits) for val in row]) for row in matrix]))

size = map(int, raw_input().split())
print_spiral(size[0], size[1])
