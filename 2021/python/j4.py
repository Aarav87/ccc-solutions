# CCC 2021 Junior 4: Arranging Books

# input
books = input()
# number of large and medium books
num_l = num_m = 0

# iterate through each book
for book in books:
    # increase number of large books if the book is L
    if book == "L":
        num_l += 1
    # increase number of medium books if the book is M
    elif book == "M":
        num_m += 1

# total number of misplaced books
misplaced = 0
# number of medium books in large section and large books in medium section
m_in_l = l_in_m = 0

# iterate through large section
for i in range(num_l):
    # increase misplaced and m_in_l if book size is medium
    if books[i] == "M":
        misplaced += 1
        m_in_l += 1
    # increase misplaced if book size is small
    elif books[i] == "S":
        misplaced += 1

# iterate through medium section
for i in range(num_l, num_l+num_m):
    # increase misplaced and l_in_m if book size is large
    if books[i] == "L":
        misplaced += 1
        l_in_m += 1
    # increase misplaced if book size is small
    elif books[i] == "S":
        misplaced += 1

# output minimum number of swaps
print(misplaced-min(m_in_l, l_in_m))
