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


def DFS(island, x, y):
    xLength = len(island)
    yLength = len(island[0])

    if (x < 0 or y < 0 or x >= xLength or y >= yLength or island[x][y] == 0):
        return

    island[x][y] = 0

    DFS(island, x + 1, y)
    DFS(island, x - 1, y)
    DFS(island, x, y + 1)
    DFS(island, x, y - 1)
    DFS(island, x + 1, y + 1)
    DFS(island, x - 1, y - 1)
    DFS(island, x + 1, y - 1)
    DFS(island, x - 1, y + 1)


def IslandsDFS(island):
    count_islands = 0
    for i in range(len(island)):
        for j in range(len(island[i])):
            if island[i][j] == 1:
                count_islands += 1
                DFS(island, i, j)

    print('Количесво обнаруженных остравов: ', count_islands)


IslandsDFS(arr_islands)
