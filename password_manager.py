import os


# if we dont insert the correct master password , the code will not work.
master_pwd = input("Enter your master password:")

    
def add():
    username = input("Enter your username:")
    pwd = input("Enter password to store:")

    with open("password.txt","a") as f:
        data =f.write(username + "|"+ pwd + "\n")


def view():
    with open("password.txt","r") as g:
        sigma = g.readlines()
        for lines in sigma:
            print(lines.strip())
    

def delete():
    os.remove("password.txt")


while master_pwd == "gigganigga":

    mode =input("Do you wanna add , view or quit?:")
    if mode == "q":
        break
    elif mode== "add":
        add()
    elif mode == "view":
        view()
    elif mode == "delete": #if we enter delete the file with passwords will be delete it'll not be mentioned in the options but as the owner i only know about it (muehehehe)
        delete()
    else:
        print("Enter valid input!!")



    
