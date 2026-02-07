
import random

computer = random.randint(1, 100)
a = 0

print("\n\n\nWelcome to 'Perfect Number Guess' game..... You have 10 attempts to guess your number between 1 to 100. ")



while True:
    try:
        player = int(input("\nEnter your guess : "))
    except ValueError:
        print("please enter number only")
        continue
    if(player<1 or player>100):
        print("please enter a number between 1 to 100")
        continue

    a+=1

    if(a<=10):
        if (player>computer):
            print(f"your number is too high !!   (attempts left : {10-a})")
        elif(computer>player):
            print(f"Your number is too low !!   (attempts left : {10-a})")
        elif(computer==player):
            print(f"\nCongrats!! You have guessed the correct number in {a} attempt(s)")
            break
        else:
            print("\nDeveloper, something went wrong")
            break
    else:
        print(f'''\nYour attempts are over!! You lose..........
Correct number was {computer}''')
        break

    
    
    



