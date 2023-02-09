# CCC 2020 Senior 2: Escape Room (13/15)

from math import *
from collections import deque

rows = int(input())
cols = int(input())

grid = []
for _ in range(rows):
    grid.append(list(map(int, input().split())))

q = deque()
q.append((0, 0))
escape = False
visited = [(0, 0)]
factors = {}

while len(q) > 0:
    r, c = q.popleft()
    x = grid[r][c]

    if r == rows - 1 and c == cols - 1:
        escape = True
        break

    if x in factors:
        for i in factors[x]:
            a, b = i[0], i[1]
            if (a, b) not in visited:
                visited.append((a, b))
                q.append((a, b))
    else:
        factors[x] = []
        for i in range(1, ceil(sqrt(x)) + 1):
            if x % i == 0:
                a, b = i - 1, x // i - 1

                if a <= rows - 1 and b <= cols - 1 and (a, b) not in visited:
                    factors[x].append((a, b))
                    visited.append((a, b))
                    q.append((a, b))

                if b <= rows - 1 and a <= cols - 1 and (b, a) not in visited:
                    factors[x].append((b, a))
                    visited.append((b, a))
                    q.append((b, a))

if escape:
    print("yes")
else:
    print("no")
