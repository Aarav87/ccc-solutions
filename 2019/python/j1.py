# CCC 2019 Junior 1: Winning Score

# input for team Apples
A3 = int(input())
A2 = int(input())
A1 = int(input())

# input for team Bananas
B3 = int(input())
B2 = int(input())
B1 = int(input())

# calculate score for each team
AScore = (A3 * 3) + (A2 * 2) + A1
BScore = (B3 * 3) + (B2 * 2) + B1

# output A if AScore had higher score
if AScore > BScore:
    print("A")
# output B if BScore had higher score
elif AScore < BScore:
    print("B")
# output T if there was a tie
else:
    print("T")
