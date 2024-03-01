from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bid_dict = {}
bidding_finised = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while bidding_finised == False:
  name= input("What is your name?: ")
  bid= int(input("What is your bid?: $"))
  bid_dict[name] = bid 
  any_more= input("Are there any other bidders? Type 'yes' or 'no'.")
  if any_more == "no":
   bidding_finised = True
  elif any_more == "yes":
   clear()
find_highest_bidder(bid_dict)
