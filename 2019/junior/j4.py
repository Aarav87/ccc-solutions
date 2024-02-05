# CCC 2019 Junior 4: Flipper

# input
sequence = input()

# 2D array of nums
nums = [[1, 2], [3, 4]]

# iterate through each char in sequence
for x in sequence:
    # flip nums horizontally if char is H
    if x == "H":
        nums[0], nums[1] = nums[1], nums[0]
    # flip nums vertically if char is V
    else:
        nums[0][0], nums[0][1] = nums[0][1], nums[0][0]
        nums[1][0], nums[1][1] = nums[1][1], nums[1][0]

# output
print(nums[0][0], nums[0][1])
print(nums[1][0], nums[1][1])
