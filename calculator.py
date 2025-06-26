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
        c=a+b
        print("sum is: ",c)
    elif(choice==2):
        print(" SUTRARION SELECTED")
        a=int(input("Enter the first number "))
        b=int(input("Enter the second number "))
        c=a-b
        print(c)
    elif(choice==3):
        print(" DIVISION SELECTED")
        a=int(input("Enter the first number "))
        b=int(input("Enter the second number "))
        if(b!=0):
            c=a/b
            print(c)
        else:
            print("undefined")
    elif(choice==4):
        print(" MULTIPLICATION SELECTED")
        a=int(input("Enter the first number "))
        b=int(input("Enter the second number "))
        c=a*b
        print(c)
    elif 5:
        print("Exitig .....")
        break