# Login Register System using password and username

import json

def register():
    try:
        print("\nRegistration")
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        
        # Input validation
        if not username or not password:
            print("Error: Username and password cannot be empty!")
            return
        
        if len(username) < 3:
            print("Error: Username must be at least 3 characters long!")
            return
            
        if len(password) < 4:
            print("Error: Password must be at least 4 characters long!")
            return
        
        dict_credential = {username: password}
        json_credential = json.dumps(dict_credential)
        
        # Write to file with error handling
        try:
            file = open("File_Handling/Day10/Day10_tasks/credential.json", "a")
            file.write(json_credential + "-")
            file.close()
            print("Registration successful!")
            
        except FileNotFoundError:
            print("Error: Directory path does not exist!")
        except IOError as e:
            print(f"File error during registration: {e}")
        
    except json.JSONEncodeError as e:
        print(f"Error encoding data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during registration: {e}")

def login():

    try:
        print("\nLogin")
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        
        # Try to read file with error handling
        try:
            file = open("File_Handling/Day10/Day10_tasks/credential.json", "r")
            content = file.read()
            file.close()
            
        except FileNotFoundError:
            print("No users registered yet. Please register first.")
            return False
        except IOError as e:
            print(f"File error during login: {e}")
            return False
        
        # Handle empty file
        if not content.strip():
            print("No users registered yet. Please register first.")
            return False
        
        list_credential = content.split("-")
        login_success = False
        
        for i in list_credential:
            if i.strip():  # Check if string is not empty
                try:
                    dict_credential = json.loads(i)
                    if username in dict_credential and dict_credential.get(username) == password:
                        print("Login Successful!")
                        login_success = True
                        break
                except json.JSONDecodeError:
                    print("Warning: Corrupted data found in storage - skipping")
                    continue
                except Exception as e:
                    print(f"Warning: Error processing user data: {e}")
                    continue
        
        if not login_success:
            print("Login Failed: Invalid username or password")
        
        return login_success
        
    except Exception as e:
        print(f"An unexpected error occurred during login: {e}")
        return False

def view_users():
    try:
        # Try to read file
        try:
            file = open("File_Handling/Day10/Day10_tasks/credential.json", "r")
            content = file.read()
            file.close()
            
        except FileNotFoundError:
            print("No users registered yet.")
            return
        except IOError as e:
            print(f"File error: {e}")
            return
        
        if not content.strip():
            print("No users registered yet.")
            return
        
        list_credential = content.split("-")
        print("\nRegistered Users:")
        user_count = 0
        
        for i in list_credential:
            if i.strip():
                try:
                    dict_credential = json.loads(i)
                    for user in dict_credential:
                        print(f"Username: {user}")
                        user_count += 1
                except json.JSONDecodeError:
                    continue
        
        print(f"Total users: {user_count}")
        
    except Exception as e:
        print(f"Error viewing users: {e}")

def main_menu():
    while True:
        try:
            print("\nLogin-Register System")
            print("1. Register")
            print("2. Login")
            print("3. View Users")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == "1":
                register()
            elif choice == "2":
                login()
            elif choice == "3":
                view_users()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, 3, or 4")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred in the menu: {e}")

if __name__ == "__main__":
    main_menu()