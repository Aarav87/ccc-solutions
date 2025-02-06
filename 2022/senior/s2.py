# CCC 2022 Senior 2: Good Groups

X = int(input())
sameGroup = dict()

for i in range(X):
    p1, p2 = input().split()

    if p1 in sameGroup:
        sameGroup[p1].add(p2)
    else:
        sameGroup[p1] = {p2}

Y = int(input())
diffGroup = dict()

for i in range(Y):
    p1, p2 = input().split()

    if p1 in diffGroup:
        diffGroup[p1].add(p2)
    else:
        diffGroup[p1] = {p2}

G = int(input())
violations = 0

for i in range(G):
    group = set(input().split())

    for member in group:
        if member in sameGroup:
            intersect = group.intersection(sameGroup[member])
            if intersect != sameGroup[member]:
                violations += (len(sameGroup[member]) - len(intersect))

        if member in diffGroup:
            intersect = group.intersection(diffGroup[member])
            if intersect:
                violations += len(intersect)

print(violations)
