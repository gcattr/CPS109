import random

Suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
Ranks = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
Money = 1000

def HandMath(Hand):
    x = 0
    y = 0
    
    for i in Hand:
        if i[0].isdigit():
            x = x + int(i[0])
            y = y + int(i[0])
        elif i[0] != "Ace":
            x = x + 10
            y = y + 10
        else:
            x = x + 1
            y = y + 10
        
    return x,y         

while True:    
    # generate new deck
    Deck = []
    for i in Suits:
        for v in Ranks:
            Deck.append([v,i])
    random.shuffle(Deck)
    
    
    Hand = []
    DealerHand = []
    
    for i in range(0,2): # deal player card
        Index = random.randint(0, len(Deck)-1)
        Hand.append(Deck[Index])
        Deck.pop(Index)
        
    # deal dealer's cards
    Index = random.randint(0, len(Deck)-1)
    DealerHand.append(Deck[Index])
    Deck.pop(Index)
    
    print("==============================================")
    
    print("\nyou have $",Money)
    Wage = int(input("How much would you like to wage?: "))
    Money = Money - Wage
    print("\nYou waged $",Wage,"\nYou now have $",Money)
    
    print("\n--- GAME STARTING ---")
    
    x, y = HandMath(Hand)
    if x == y: 
        print("\nYour hand:", Hand , "\nWorth:", x )
    else:
        print("\nYour hand:", Hand , "\nWorth:", x, " / ", y)
    
    x, y = HandMath(DealerHand)
    if x == y: 
        print("\nDealer's hand:", DealerHand , "\nWorth:", x )
    else:
        print("\nDealer's hand:", DealerHand , "\nWorth:", x, "/", y)
    
    while True:
        UserInput = str(input("\nHit? (y/n): "))
        if UserInput == "y":
            Index = random.randint(0, len(Deck)-1)
            Hand.append(Deck[Index])
            Deck.pop(Index)
            x, y = HandMath(Hand)
            print("\nYour hand:", Hand , "\nWorth:", x )
            
            if x == y: 
                if x == 21 or y == 21:
                    print("\nYou Win!")
                    Money = Wage * 2 + Money
                    break
                elif x > 21 or y > 21:
                    print("\nBust! You Lose!")
                    break     
            elif y > 21:
                if x == 21:
                    print("\nYou Win!")
                    Money = Wage * 2 + Money
                    break
                elif x > 21:
                    print("\nBust! You Lose!")
                    break
        else:
            x, y = HandMath(DealerHand)
            a, b = HandMath(Hand)
            while x < 17: 
                Index = random.randint(0, len(Deck)-1)
                DealerHand.append(Deck[Index])
                Deck.pop(Index)
                x, y = HandMath(DealerHand)
                
            print("\nDealer's hand:", DealerHand , "\nWorth:", x )
            
            if x > 21:
                print("\nYou Win!")
                Money = Wage * 2 + Money
                break
            elif (21 - x) > ((21 - a) or (21 - b)):
                print("\nYou Win!")
                Money = Wage * 2 + Money
                break
            else:
                print("\nTie!")
                break            


