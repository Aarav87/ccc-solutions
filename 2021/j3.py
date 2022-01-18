# CCC 2021 Junior 3: Secret Instructions

import sys

# get input
nums = sys.stdin.readlines()
# list of directions for output
ans = []

# iterate through each num
for num in nums[:-1]:
    # get sum of first 2 digits
    sum = int(num[0]) + int(num[1])
    # append previous direction to ans if sum is 0
    if sum == 0:
        ans.append(ans[-1].split(" ")[0] + " {}".format(num[2:]))
    # append right to ans if sum is even
    elif sum % 2 == 0:
        ans.append('right ' + num[2:])
    # append left to ans if sum is odd
    else:
        ans.append('left ' + num[2:])

# print each line in ans
for x in ans:
    print(x)
