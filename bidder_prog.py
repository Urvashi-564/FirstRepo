import os


def find_winner(bidding_information):
    highest_bid=0
    winner=''
    for bidder in bidding_information:
        bid_pricee=bidding_information[bidder]
        if bid_pricee> highest_bid:
            highest_bid=bid_pricee
            winner=bidder
            print(f"Highest bidder is {winner} and his bid amount is {highest_bid}")

bidder_data={}

end_of_bidding=False
while not end_of_bidding:
    name=input("enter bidders name")
    price=int(input("Enter your bid price"))
    bidder_data[name]=price
    more_bidders=input("Do u want to addmore bidders enter yes or no").lower()
    if more_bidders == 'n':
        end_of_bidding=True
        find_winner(bidder_data)

    elif more_bidders == 'y':
        os.system('cls')