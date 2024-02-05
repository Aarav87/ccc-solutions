# CCC 2018 Junior 5:  Choose your own path

pages = int(input())
reachable = dict()

for i in range(1, pages+1):
    reachable[i] = list(map(int, input().split()))[1:]

q = [(1, 0)]
path_ans = []
pages_visited = set()
shortest_path = 0
flag = False

while len(q) > 0:
    cur, path = q.pop(0)

    if cur not in pages_visited:
        pages_visited.add(cur)
        path += 1

        if not reachable[cur] and not flag:
            shortest_path = path
            flag = True

        for page in reachable[cur]:
            q.append((page, path))

if len(pages_visited) == pages:
    print("Y")
else:
    print("N")
print(shortest_path)
