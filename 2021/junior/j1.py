# CCC 2021 Junior 1: Boiling Water

# input
temperature = int(input())

# calculate pressure
pressure = 5 * temperature - 400
print(pressure)

# find the sea level using the pressure
if pressure > 100:
    print(-1)  # below sea level
elif pressure < 100:
    print(1)  # above sea level
else:
    print(0)  # at sea level
