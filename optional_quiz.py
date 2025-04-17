print("welcome to our quiz game! " )
user_permission = input("do you want to play our game ? ")
score = 0
if user_permission == "yes":
    print("okay let's playy!")

    first_question = input("What is the capital of india?\n1.New Delhi\n2.mumbai\n4.niggapur\n4.dhanbad\n>>").lower()
    if first_question =="1" or"new delhi":
        print("you're correct")
        score +=1
    else:
        print("you're wrong")

    second_question = input("What is my name?\n1.nigga\n2.kallu\n3.Aditya\n4.khushi\n>>").lower()
    if second_question =="3" or "aditya":
        print("you're correct")
        score += 1
    else:
        print("you're wrong!")

    third_question = input("Who's the worst footballer ever?\n1.gavi\n2.pedri\n3.puyol\n4.xavi\n>>").lower()
    if third_question =="1" or "gavi":
        print("you're right!")
        score +=1
    else:
        print("you're wrong!")
    print(f"your score is {score}!")
else:
    print("no probs")