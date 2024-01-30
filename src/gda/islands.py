def DFS(island, x, y):
    if x < 0 or x >= len(island) or y < 0 or y >= len(island) or island[x][y] == 0:
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
def count_islands(islands):
    count = 0
    for i in range(len(islands)):
        for j in range(len(islands[i])):
            if islands[i][j] == 1:
                count += 1
                DFS(islands, i, j)
    print('Количество островов:', count)
height = int(input('Введите высоту матрицы:'))
width = int(input('Введите ширину матрицы:'))
matrix_island = [[0] * width for i in range(height)]
for i in range(height):
    matrix_row = input(f'{i + 1} строка:').split(',')
    for j in range(width):
        matrix_island[i][j] = int(matrix_row[j])
count_islands(matrix_island)
