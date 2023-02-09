# CCC 2020 Senior 1: Surmising a Sprinter’s Speed

n = int(input())

x = []
for i in range(n):
    x.append(list(map(int, input().split())))

x.sort()

speed = -1
for i in range(1, n):
    dist = abs(x[i][1] - x[i-1][1])
    time = x[i][0] - x[i - 1][0]
    cur = dist / time

    if cur > speed:
        speed = cur

print(speed)
