n1 = int(input("Enter first number: "))
n2 = int(input("Enter first number: "))
if(n1>n2):
    print("first is the greatest")
    n1 += 10
    print("updated value of number 1 :",n1)
else:
    print("second number is the largest ")
    n2 -= 5
    print("updated value of second number : ",n2)