# Make a simple login system without registration using functions

def simple_login():
    # Predefined users
    users = {
        "admin": "admin1",
        "user": "aadminn"
    }
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password!")

simple_login()