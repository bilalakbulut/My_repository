logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


print(logo)
from replit import clear
ch = True
dic = {}

def asd(bidding,):
    highest = 0
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"Winner is {winner} with a bid of ${highest} ")

while ch:
    
    name = input("Type your name:")
    price = int(input("Type your bid? $"))

    dic[name] = price

    
    ch_1 = input("Do you want to bid:").lower()
    if ch_1 == "no":
        ch = False
        asd(dic)
    elif ch_1 == "yes":
        clear()
        
    else:
        print("Please input valid options: ")









