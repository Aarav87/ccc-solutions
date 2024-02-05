# CCC 2023 Senior 1: Trianglane

C = int(input())
R = [list(map(int, input().split())), list(map(int, input().split()))]

tiles = 0

for i in range(C):
    if R[0][i] == 1:
        tiles += 3

        if i + 1 <= C - 1 and R[0][i+1] == 1:
            tiles -= 2

        if i % 2 == 0:
            if R[1][i] == 1:
                tiles -= 2

    if R[1][i] == 1:
        tiles += 3

        if i + 1 <= C - 1 and R[1][i+1] == 1:
            tiles -= 2

print(tiles)
