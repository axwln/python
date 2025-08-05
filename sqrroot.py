def squareroot():
    num = int(input("Enter a number: "))
    if num < 0:
        print("Cannot compute square root of a negative number.")
    else:     
        r = num ** 0.5
    print(f"Square root of{num}is {r}")
squareroot()

