# Combined implementation of both tasks
#Create a list of usernames Input a username from the user
#Check if the username is present in the list or not.
# Create a dictionary of usernames and passwords, 
# extract all the usernames from the dictionary and 
# input username from the user and check 
# if the username is present in the extracted list of 	usernames


# List Implementation
print("\nList-based checking names(username)")

usernames_list = ["saugatthapa", "john_doe", "alice_smith"]

print("Available usernames:")
for username in usernames_list:
    print(username)

username_input1 = input("\nEnter username to check in list: ").strip()

if username_input1 in usernames_list:
    print(f"FOUND: '{username_input1}' exists in the list")
else:
    print(f"NOT FOUND: '{username_input1}' is not in the list")

# Dictionary Implementation
print("\nDictionary-based checking names(username)")
users_dict = {
    "saugatthapa": "pass123",
    "john_doe": "johnPass", 
    "alice_smith": "alicePass"
}

print("User database:")
for uname, pwd in users_dict.items():
    print(f"Username: {uname} Password: {pwd}")

extracted_usernames = list(users_dict.keys())

username_input2 = input("\nEnter username to check in dictionary: ").strip()

if username_input2 in extracted_usernames:
    print(f"FOUND: '{username_input2}' exists in dictionary")
    print(f"Password: {users_dict[username_input2]}")
else:
    print(f"NOT FOUND: '{username_input2}' is not in dictionary")