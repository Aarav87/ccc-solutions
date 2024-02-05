# CCC 2019 Junior 3: Cold Compress

# input for number of lines of data
N = int(input())

# iterate through each line
for i in range(N):
    # input
    line = input()
    # num of times a symbol appears consecutively
    counter = 1
    # iterate through each char in the line
    for x in range(len(line)):
        # check if char is not the last
        if x != len(line)-1:
            # check if current char is not equal to next char
            if line[x] != line[x+1]:
                # output the num of times the symbol appeared
                print(counter, line[x], end=" ")
                # reset counter
                counter = 1
            else:
                # increase counter if current char is equal to next char
                counter += 1
        else:
            # output the num of times the symbol appeared
            print(counter, line[x])
