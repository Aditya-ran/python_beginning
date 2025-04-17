import random
guesses = 0
permission = input("Do you want to  play? (y/n)")
while(permission =="y"):
    
    randNo = random.randint(1,10)
    nigga = int(input("Enter your guess: "))
    guesses +=1
    if(nigga == randNo):
        print("your guess was correct!",randNo)
        break
    
    else:
        if nigga >randNo:
            print("try a smaller number")
        else: 
            print("try a bigger number")
    
else:
    print("Thanks for playing! ")
print(f"you took {guesses} number of guesses")