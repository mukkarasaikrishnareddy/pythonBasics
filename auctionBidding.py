
def find_highest_bidder(bidding_dictnary):
    highest_bid = 0
    for bidder in bidding_dictnary:
        bid_amount = bidding_dictnary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"the winner is {winner} with a bid of ${highest_bid}")
            bids = {}
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $ "))
    bids[name] = price
    should_continue = input("are there any other bidders? (yes/no):\n ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
        bids = {}
    elif should_continue == "yes":
        print("\n"*20)