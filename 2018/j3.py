# CCC 2018 Junior 3: Are we there yet?

distances = list(map(int, input().split()))

table = [0, 0, 0, 0, 0]
for i in range(1, 5):
    table[i] = table[i-1] + distances[i-1]

for i in range(5):
    for j in range(5):
        print(abs(table[j]-table[i]), end=" ")
    print()