import os

print("********************WELCOME TO SILENT AUCTION***************************")
name = input("Enter your name")
bid_price = int(input("enter your bid price"))
bidders = {}


def add_to_bid(name, bid_price):
    bidders[name] = name
    bidders[name] = bid_price
    os.system("cls")


add_to_bid(name, bid_price)
add_bidders = input("do you want to add more bidders y/n ")
# if add_bidders == 'y':
#     clear = lambda: os.system('cls')
#     clear()
#     name = input("Enter your name")
#     bid_price = int(input("enter your bid price"))
#     add_to_bid(name, bid_price)
#     add_bidders = input("do you want to add more bidders y/n ")
# elif add_bidders == 'n':
#     print(f"Name of highest bidder is {bidders[name]} and maximum bid amount is"), max(bidders[bid_price])

while (add_bidders != 'n'):
    name = input("Enter your name")
    bid_price = int(input("enter your bid price"))
    add_to_bid(name, bid_price)
    add_bidders = input("do you want to add more bidders y/n ")


else:
    # maximum_bid=bidders[name].max()
    print("Name of highest bidder is maximum bid amount is",max(bidders.values()))