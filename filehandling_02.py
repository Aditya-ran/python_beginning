import os


master_pwd = input("Enter your master password:")
if master_pwd =="delete":
    os.remove("password.txt")
def add():
    username = input("Enter your username:")
    pwd = input("Enter password to store:")

    with open("password.txt","a") as f:
        data =f.write(username + "|"+ pwd + "\n")


def view():
    with open("password.txt","r") as g:
        sigma = g.read()
    print(sigma)

def delete():
    pass


while master_pwd == "gigganigga":

    mode =input("Do you wanna add , view or quit?:")
    if mode == "q":
        break
    elif mode== "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Enter valid input!!")



    
