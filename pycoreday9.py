#sum of numbers
sum=0
for i in range(1,11):
    sum += i
    print("sum is ",sum)


#even numbers from 
n = [1, 2, 3, 4, 5, 6]
for num in n:
    if (num%2==0):
        print(num)

#Use nested loops to create a multiplication table for numbers 1 to 5.
n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        print(f"{i} x {j} = {i*j}")
    print()  