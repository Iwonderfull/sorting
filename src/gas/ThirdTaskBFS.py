from collections import deque
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
    countIslandsBFS(matrix_island)

def countIslandsBFS(matrix):

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    island_count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and (i, j) not in visited:
                BFS(matrix, visited, i, j)
                island_count += 1

    print(island_count)


def BFS(matrix, visited, start_row, start_col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    queue = deque([(start_row, start_col)])
    visited.add((start_row, start_col))

    while queue:
        current = queue.popleft()
        row, col = current

        for direction in directions:
            new_row, new_col = row + direction[0], col + direction[1]
            if (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] == 1 and (new_row, new_col) not in visited):
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))



island_area()
input("Press Enter to exit")
