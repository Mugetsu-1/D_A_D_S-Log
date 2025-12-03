# Login Register System using password and username

import json

def register():
    print("\nRegistration")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    dict_credential = {username: password}
    json_credential = json.dumps(dict_credential)
    
    file =open("File_Handling/Day9/Day9_tasks/credential.json","a")
    file.write(json_credential + "-")
    file.close()
    
    print("Registration successful!")

def login():
    print("\nLogin")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    file =open("File_Handling/Day9/Day9_tasks/credential.json","r")
    content = file.read()
    file.close()
    
    list_credential = content.split("-")
    login_success = False
    
    for i in list_credential:
        if i != "":
            dict_credential = json.loads(i)
            if username in dict_credential and dict_credential.get(username) == password:
                print("Login Successful")
                login_success = True
                break
    
    if not login_success:
        print("Login Failed")
    
    return login_success

def main_menu():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3")

main_menu()