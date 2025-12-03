# Login system with file handling for username storage

def register():
    username = input("Create username: ")
    password = input("Create password: ")
    return username, password

def save_username(username):
    with open("File_Handling/Day8/Day8_tasks/users.json", "a") as file:
        file.write(username + "\n")

def read_usernames():
    try:
        with open("File_Handling/Day8/Day8_tasks/users.json", "r") as file:
            usernames = [line.strip() for line in file.readlines()]
        return usernames
    except FileNotFoundError:
        return []

def login(users):
    username = input("Username: ")
    password = input("Password: ")
    
    if username in users:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials!")
        return False

def login_system():
    users = read_usernames()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            username, password = register()
            save_username(username)
            users = read_usernames()
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