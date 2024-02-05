# CCC 2018 Junior 2: Occupy parking

# input
N = int(input())
yesterday = input()
today = input()

# number of parking spots occupied both today and yesterday
occupied = 0
for i in range(N):
    # increase occupied if parking spot was occupied on both days
    if yesterday[i] == "C" and today[i] == "C":
        occupied += 1

# output
print(occupied)
