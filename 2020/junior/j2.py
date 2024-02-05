# CCC 2020 Junior 2: Epidemiology

# input
target = int(input())
initial = int(input())
spread = int(input())

# num of people infected
total_infected = initial
# num of days
days = 0

while total_infected <= target:
    # increase num of days
    days += 1
    # increase the num of people infected
    total_infected += (spread ** days) * initial

# output days
print(days)
