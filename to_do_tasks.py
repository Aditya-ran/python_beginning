import os


def write_tasks():
    tasks = input("Enter your tasks:")
        
    with open("tasks.txt","a") as f:
        data = f.write(tasks+"\n")
        
        

def read_tasks():
    
    with open("tasks.txt","r") as f:
            data = [x.strip() for x in f.readlines()]
            for j in range(len(data)):
                print(f"{j+1}.{data[j]}")
            
            
    
       
answer = input("Run your mighty creation?(y/n):").lower()
while answer == "y":
    choice = int(input("What do you wanna do?(1 for write, 2 for read,3 to erase existing tasks,4 to quit):"))
    if choice == 1:
        write_tasks()
            
    elif choice == 2:
        read_tasks()
    elif choice == 3:
        precaution = input("do you wanna delete the file?:")
        if precaution == "y":
            os.remove("tasks.txt")
            print("file removed!")
        else:
            pass
    elif choice == 4:
        break
    else:
        print("Enter valid input!!")
answer = input("do you wanna continue(y/n)").lower()

               