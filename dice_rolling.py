import random
nigga = input("do you wanna play?")
while True:
    permission = input("do you wanna role a dice? " ).lower()
    if permission == "yes":
        random_num_1 = random.randint(1,6)
        random_num_2 = random.randint(1,6)
        print(f"you rolld a {random_num_1} and {random_num_2}")
        
    elif permission == "no":
        print("no probs")
        break
    else:
        print("Enter valid input!")