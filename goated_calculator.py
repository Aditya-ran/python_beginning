def sum(x,y):
        bruv = x+y
        print(f"The sum is: {bruv}")

def subtraction(x,y):
        bruv = x-y
        print(f"The difference is: {bruv}")

def multiplication(x,y):
        bruv = x*y
        print(f"The product is: {bruv}")
        

def division(x,y):
        bruv = x/y
        print(f"The division is: {bruv}")
        
lad = input("Do you want use calculator? (y/n)")
while(lad == 'y'):

    

    print("Welcome to our calculaotr")
    x = int(input("Enter your  1st number: "))
    y = int(input("Enter your 2nd nubmer: "))

    operation = input("Enter what you want to do with the number(sum,sub,multi,div): "  )

    match operation:
        case "sum":
            sum(x,y)
        
        case "sub":
            subtraction(x,y)
        
        case "multi":
            multiplication(x,y)
        case "div":
            division(x,y)
    
    lad = input("do you want to continue (y/n): ")
else:
      print("thanks for using")
        
