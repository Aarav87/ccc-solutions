# CCC 2018 Junior 1: Telemarketer or not?

# input
d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())

# output ignore if the 1st and 4th digits are 8 or 9 and the 2nd and 3rd digits are equal
if 7 < d1 < 10 and 7 < d4 < 10 and d2 == d3:
    print("ignore")
# output answer otherwise
else:
    print("answer")
