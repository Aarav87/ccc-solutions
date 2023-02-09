# CCC 2018 Junior 4: Sunflowers

N = int(input())

grid = []
for i in range(N):
    grid.append(list(map(int, input().split())))

min_height = grid[0][0]
row = col = 0

if grid[0][-1] < min_height:
    min_height = grid[0][-1]
    col = len(grid[0])-1
if grid[-1][0] < min_height:
    min_height = grid[-1][0]
    row = len(grid)-1
if grid[-1][-1] < min_height:
    min_height = grid[-1][-1]
    row = len(grid)-1
    col = len(grid[0])-1

if row == 0 and col == 0:
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end=" ")
        print()
elif row == 0 and col > 0:
    for j in reversed(range(N)):
        for i in range(N):
            print(grid[i][j], end=" ")
        print()
elif row > 0 and col == 0:
    for j in range(N):
        for i in reversed(range(N)):
            print(grid[i][j], end=" ")
        print()
else:
    for i in reversed(range(N)):
        for j in reversed(range(N)):
            print(grid[i][j], end=" ")
        print()