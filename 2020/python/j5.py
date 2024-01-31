# CCC 2020 Junior 5: Escape Room (13/15)

# input
rows = int(input())
cols = int(input())
grid = []

# append each row into grid
for i in range(rows):
    grid.append(list(map(int, input().split())))


# returns a list of the pair of factors
def get_factors(num):
    factors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            if (i, num // i) not in factors:
                factors.append((i, num // i))
                factors.append((num // i, i))
    return factors


def escape(num_rows, num_col, arr):
    # queue of row and column
    q = [(0, 0)]
    # set of visited coordinates
    visited = set()

    while q:
        # get first element in queue
        curr = q.pop(0)

        # return yes if current coordinate is equal to coordinate of exit
        if curr == (num_rows, num_col):
            return "yes"

        # get the factors of the value of current coordinate
        factors = get_factors(arr[curr[0]][curr[1]])

        # iterate through each factor
        for i in factors:
            x, y = i[0]-1, i[1]-1
            # check if coordinate has not been visited and x and y are in range
            if (x, y) not in visited and x <= num_rows and y <= num_col:
                # add coordinate pair to visited
                visited.add((x, y))
                # append coordinate pair to queue
                q.append((x, y))

    # return no once queue is empty
    return "no"


# output
print(escape(rows-1, cols-1, grid))
