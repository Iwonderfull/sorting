import random

def printIslands(islands):
    for i in range(len(islands)):
        for j in range(len(islands[i])):
            print(islands[i][j], end=" ")
        print()

def island_area():
    print("type height of the matrix")
    height = int(input())
    print("type weight of the matrix")
    width = int(input())
    matrix_island = [[0] * width for i in range(height)]

    print("Type 1 to fill at random, type 2 to fill yourself")
    inpt = int(input())
    if inpt == 1:
        for i in range(height):
            for j in range(width):
                random_number = random.randint(1, 3)
                if random_number == 1:
                    matrix_island[i][j] = 1
    else:
        for i in range(height):
            print(i + 1, "row:")
            matrix_row = input().split()
            for j in range(width):
                matrix_island[i][j] = int(matrix_row[j])
    printIslands(matrix_island)
    countIslandsDFS(matrix_island)


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


def countIslandsDFS(island):
    count_islands = 0
    for i in range(len(island)):
        for j in range(len(island[i])):
            if island[i][j] == 1:
                count_islands += 1
                DFS(island, i, j)

    print(count_islands)

island_area()