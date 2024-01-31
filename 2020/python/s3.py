# CCC 2020 Senior 3: Searching for Strings (7/15)

N = input()
H = input()
visited = set()
i = 0
res = 0

while i <= len(H) - len(N):
    sub = H[i:i + len(N)]

    if sub not in visited:
        count = 0

        visited.add(sub)
        z = list(N)
        for l in sub:
            if l in z:
                z.remove(l)
                count += 1

        if count == len(N):
            res += 1

    i += 1

print(res)