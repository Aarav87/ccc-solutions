# CCC 2020 Junior 4: Cyclic Shifts

# input
T = input()
S = input()

ans = "no"
for i in range(len(S)):
    # set ans to yes if S is in T
    if S in T:
        ans = "yes"
        break
    # update S by moving first char to the end
    S = S[1:] + S[0]

# output ans
print(ans)
