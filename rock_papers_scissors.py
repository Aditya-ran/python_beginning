import random

user_wins = 0
computer_wins = 0
guess = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if (user_input == "q"):
        print("thanks for playing")
        print(f"you won {user_wins} times")
        print(f"computer won {computer_wins} times")
   
        break
    if user_input not in guess:
        continue
    random_guess = random.randint(0,2)
    computer_guess = guess[random_guess]
    
        
    
    
    
    if (computer_guess == user_input):
        print("it's a draw!")
        
    
    
    elif( user_input == "paper" and computer_guess == "rock" ):
        print("user wins!")
        user_wins +=1
    
    elif( user_input == "rock"and computer_guess == "scissors"):
        print("user wins!")
        user_wins +=1
    
    
    
    
    elif ( user_input == "scissors" and computer_guess == "paper"):
        print("user wins!")
        user_wins +=1
    
    else:
        print("you lose")
        computer_wins +=1
