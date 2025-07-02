#reg , log , exit 
#name , age , address 
#extra = phone no , age must be 18+

# while True:
#     print("1. REGISTER")
#     print("2. LOGIN")
#     print("3. EXIT")
#     choice="enter your choice"
#     if(choice==1):
#         name=input("Enter the Name")
#         phone=int(input("Enter your age"))
#         a=len(phone)
#         if(a!=10):
#             print("enter a valid phone number")
            
#         age=int(input("Enter your age"))
#         if(age<18):
#             print("Eligible ")
#         else:
#             print("not eligble for reggistration.....")
#             exit()
#         address=input("Enter your address")
#         username=input("Enter your username")
#         password=input("enter your password")
#     elif(choice==2):
#         userlog=input("Enter your username")
#         userpass=input("enter your password")
#     elif 5:
#         print("Exiting.........")
        
               
# Simple database to store user information (in a real app, use a proper database)
users = {}

while True:
    print("\n1. REGISTER")
    print("2. LOGIN")
    print("3. EXIT")
    
    try:
        choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("Please enter a valid number!")
        continue
        
    if choice == 1:
        print("\n--- REGISTRATION ---")
        name = input("Enter your name: ")
        
        # Phone number validation
        while True:
            phone = input("Enter your phone number: ")
            if len(phone) == 10 and phone.isdigit():
                break
            print("Please enter a valid 10-digit phone number")
            
        # Age validation
        while True:
            try:
                age = int(input("Enter your age: "))
                if age >= 18:
                    print("Registration successful!")
                    break
                else:
                    print("You must be at least 18 years old to register.")
                    print("Returning to main menu...")
                    break
            except ValueError:
                print("Please enter a valid age (number)")
                
        if age < 18:
            continue
            
        address = input("Enter your address: ")
        
        # Username validation (check if already exists)
        while True:
            username = input("Enter your username: ")
            if username in users:
                print("Username already exists. Please choose another.")
            else:
                break
                
        password = input("Enter your password: ")
        
        # Store user data
        users[username] = {
            'name': name,
            'phone': phone,
            'age': age,
            'address': address,
            'password': password
        }
        
        print("Registration completed successfully!")
        print("You can now login with your credentials.")
        
    elif choice == 2:
        print("\n--- LOGIN ---")
        if not users:
            print("No users registered yet. Please register first.")
            continue
            
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if username in users and users[username]['password'] == password:
            print(f"\nLogin successful! Welcome, {users[username]['name']}!")
            print("\nUser Details:")
            print(f"Name: {users[username]['name']}")
            print(f"Phone: {users[username]['phone']}")
            print(f"Age: {users[username]['age']}")
            print(f"Address: {users[username]['address']}")
            
            # Here you could add more functionality after login
            # For example, another menu for logged-in users
        else:
            print("Invalid username or password. Please try again.")
            
    elif choice == 3:
        print("Exiting...")
        break
        
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")