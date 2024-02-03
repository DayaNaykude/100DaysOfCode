from art import logo
import os
# show logo
print(logo)
bids = {}
bidding_finished = True

def find_highest_bidder(bidder_record):
    highest_bid = 0
    bid_winner = ""
    for name in bidder_record:
        if bidder_record[name] > highest_bid:
            highest_bid = bidder_record[name]
            bid_winner = name
    print(f"The winner is {bid_winner} with a bid of {highest_bid}")
    

while bidding_finished:
    # ask name and bid value
    name = input("What is your name ? : ")
    bid_value = int(input("what is your bid value?: $"))
    bids[name] = bid_value

    bidder_wants_to_bid = input("Are there any bidder?  type 'yes' or 'no' : ").lower()
    os.system("cls")
    if bidder_wants_to_bid == "no":
        bidding_finished = False
        find_highest_bidder(bids)


