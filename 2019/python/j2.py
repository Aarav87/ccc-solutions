# CCC 2019 Junior 2: Time to Decompress

# input for number of lines of data
L = int(input())

# iterate through each line
for i in range(L):
    # input
    N, sym = input().split()
    # output N amount of the symbol
    print(sym * int(N))
