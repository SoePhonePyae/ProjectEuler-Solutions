import re

grid = list()
global limit
limit = 4


def horizontal():
    result = 0

    for grid_row in grid:
        for i in range(len(grid_row)-limit+1):
            tmp_result = 1
        
            for j in range(limit):
                tmp_result *= int(grid_row[i+j])
                
            if tmp_result > result:
                result = tmp_result

    return result


def vertical():
    result = 0

    for x in range(len(grid)):
        for y in range(len(grid)-limit+1):
            tmp_result = 1

            for i in range(limit):
                tmp_result *= int(grid[y+i][x])

            if tmp_result > result:
                result = tmp_result

    return result


def diagonal():
    result = 0

    for x in range(len(grid)-limit+1):
        for y in range(len(grid)-limit+1):
            tmp_result = 1

            for i in range(limit):
                tmp_result *= int(grid[x+i][y+i])

            if tmp_result > result:
                result = tmp_result

    return result


def reversed_diagonal():
    result = 0

    for x in range(len(grid)-limit+1):
        for y in range(len(grid)-1, limit-1, -1):
            tmp_result = 1

            for i in range(limit):
                tmp_result *= int(grid[x+i][y-i])

            if tmp_result > result:
                result = tmp_result

    return result
    

'''Reading txt file and turning it into a nested list'''
f = open('grid.txt', 'r')
row = f.readline().strip()
while row:
    grid.append(re.split("\s", row.strip()))
    row = f.readline().strip()
f.close()

print(horizontal())
print(vertical())
print(diagonal())
print(reversed_diagonal())
