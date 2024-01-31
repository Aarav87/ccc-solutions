# CCC 2021 Junior 5: Modern Art

# input
num_rows = int(input())
num_cols = int(input())
num_choices = int(input())

# boolean lists that indicate which row/column will be brushed
rows = [False] * num_rows
cols = [False] * num_cols
# create canvas using 2D boolean list
canvas = [[False] * num_cols for i in range(num_rows)]

# iterate through each choice the artist made
for i in range(num_choices):
    # index of row/column being brushed
    choice = input().split()
    idx = int(choice[1])-1
    # change colour of row if choice is R
    if choice[0] == "R":
        rows[idx] = not rows[idx]
    # change colour of column if choice is C
    else:
        cols[idx] = not cols[idx]

# iterate through each row
for i in range(num_rows):
    # check if row is brushed
    if rows[i]:
        # iterate through each col
        for j in range(num_cols):
            # brush canvas at that cell
            canvas[i][j] = not canvas[i][j]

# iterate through each col
for i in range(num_cols):
    # check if row is brushed
    if cols[i]:
        # iterate through each row
        for j in range(num_rows):
            # brush canvas at that cell
            canvas[j][i] = not canvas[j][i]

# num of cells that are gold
gold = 0
# iterate through each row
for i in range(num_rows):
    # iterate through each col
    for j in range(num_cols):
        # increase gold if cell is brushed
        if canvas[i][j]:
            gold += 1

# output number of cells that are gold
print(gold)
