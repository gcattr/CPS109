import random
yourNumber = int(input("enter a number from 1 and 10: "))
randomNumber = random.randint(1, 10)

if yourNumber == randomNumber:
    print("you win!!!!!!")
else:
    print("you lose! the correct number was " + str(randomNumber))
