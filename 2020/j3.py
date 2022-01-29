# CCC 2020 Junior 3: Art

# input
N = int(input())

minX = minY = 100
maxX = maxY = -100

# iterate through each coordinate
for i in range(N):
    x, y = input().split(",")
    # set minX to x if x is less than minX
    if int(x) < minX:
        minX = int(x)
    # set minY to y if y is less than minY
    if int(y) < minY:
        minY = int(y)
    # set maxX to x if x is greater than maxX
    if int(x) > maxX:
        maxX = int(x)
    # set maxY to y if y is greater than maxY
    if int(y) > maxY:
        maxY = int(y)

# output minX, minY and maxX, maxY
print(str(minX-1) + "," + str(minY-1))
print(str(maxX+1) + "," + str(maxY+1))
