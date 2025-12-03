# Make a login system using registration using function

def register():
    username = input("Create username: ")
    password = input("Create password: ")
    return username, password

def login(users):
    username = input("Username: ")
    password = input("Password: ")
    
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials!")
        return False

def login_system():
    users = {}
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            username, password = register()
            users[username] = password
            print("Registration successful!")
        
        elif choice == '2':
            if login(users):
                break
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

login_system()