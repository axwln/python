from calc import addition,sub,multi,div
while True:
    print("1. ADDITION")
    print("2. SUTRARION")
    print("3. DIVISION")
    print("4. MULTIPLICATION")
    print("5. EXIT")
    choice = int(input("Enter your choice: "))
    if(choice==1):
        print(" ADDITION SELECTED")
        a=int(input("Enter the first number "))
        b=int(input("Enter the second number "))
        addition(a,b)
        print(f"sum of {a} and {b} is {addition(a,b)}")
        
    elif(choice==2):
        print(" SUTRARION SELECTED")
        a=int(input("Enter the first number "))
        b=int(input("Enter the second number "))
        print(f"sudtractig {b} from {a} = {sub(a,b)}")
    elif(choice==3):
        print(" DIVISION SELECTED")
        a=int(input("Enter the first number "))
        b=int(input("Enter the second number "))
        print(div(a,b))
    elif(choice==4):
        print(" MULTIPLICATION SELECTED")
        a=int(input("Enter the first number "))
        b=int(input("Enter the second number "))
        print(multi(a,b))
    elif 5:
        e=input("do you wish to exit (yes/no)")
        if e.lower()=="yes":
            print("Exitig .....")
            break

