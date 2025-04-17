print("welcome to my computer quiz!")
marks = 0
playing =  input("Do you want to play? ")

if(playing.lower() != "yes"):
    quit()
print("Okay! let's play:)")

answer = input("What does cpu stand for? ")
if (answer.lower() == "central processing unit"):
    print("correct!" )
    marks +=1 
else:
    print("incorrect!")

answer = input("Who created computer? ")
if (answer.lower() == "charles babbage"):
    print("correct!" )
    marks +=1
else:
    print("incorrect!")

answer = input("What does gpu stand for? ")
if (answer.lower() == "graphics processing unit"):
    print("correct!")
    marks +=1
else:
    print("incorrect!")


answer = input("What does psu stand for? ")
if (answer.lower() == "power supply unit"):
    print("correct!" )
    marks +=1
else:
    print("incorrect!")

print(f"you got {marks} questions correct")
print(f"You got {marks/4*100}% questions correct")