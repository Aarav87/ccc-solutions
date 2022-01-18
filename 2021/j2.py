# CCC 2021 Junior 2: Silent Auction

# num of bids
N = int(input())
# name of the highest bidder and their bid
winner = None
highest_bid = 0

for _ in range(N):
    # input consisting of name and bid
    name = input()
    bid = int(input())
    # check if current bid is greater than highest bid
    if bid > highest_bid:
        # set highest bid and name of winner
        highest_bid = bid
        winner = name

# output name of highest bidder
print(winner)
