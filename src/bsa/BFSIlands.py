from collections import deque
import random

w = int(input('Введите ширину массива:'))
h = int(input('Введите длину массива:'))
arr_islands = [[0 for y in range(h)] for x in range(w)]


def Islands_arr(arr):
    for i in range(w):
        for j in range(h):
            arr[i][j] = random.randint(0, 4)
            if arr[i][j] != 1:
                arr[i][j] = 0
    for row in arr_islands:
        print(' '.join(map(str, row)))

Islands_arr(arr_islands)

def BFS(matrix, vis, x, y):
    sides = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    queue = deque([(x, y)])
    vis.add((x, y))

    while queue:
        current = queue.popleft()
        _x, _y = current

        for side in sides:
            new_x, new_y = _x + side[0], _y + side[1]
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] == 1 and (new_x, new_y) not in vis:
                queue.append((new_x, new_y))
                vis.add((new_x, new_y))

def Islands_count_print(island):
    x, y = len(island),len(island[0])
    vis = set()
    count_islands = 0
    for i in range(x):
        for j in range(y):
            if island[i][j] == 1 and (i, j) not in vis:
                BFS(island, vis, i, j)
                count_islands += 1


    print('Количесво обнаруженных остравов: ', count_islands)


Islands_count_print(arr_islands)
