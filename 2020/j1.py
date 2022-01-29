# CCC 2020 Junior 1: Dog Treats

# input
S = int(input())
M = int(input())
L = int(input())

# calculate score based on happiness formula
score = 1 * S + 2 * M + 3 * L

# output happy or sad depending on score
if score > 9:
    print("happy")
else:
    print("sad")
