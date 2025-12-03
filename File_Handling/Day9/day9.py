# Login Register System using password and username
import json


# Registration
username = input("Enter your username: ")
password = input("Enter your password: ")

dict_credential = {username:password}
json_credential = json.dumps(dict_credential) # dumps() converts dictionary to JSON
file = open("credential.py","a")
file.write(json_credential+"-")
file.close()

# JSON => JavaScript Object Notation
# JSON is similar to dictionary data type in Python
# It is easier to convert JSON to dictionary and vice versa

# Login
username = input("Enter your username: ")
password = input("Enter your password: ")

file = open("credential.py","r")
content = file.read()
file.close()

list_credential = content.split("-")
# print(content)
# print(type(content))
# print(list_credential)
# print(type(list_credential))

for i in list_credential:
    if i != "":
        dict_credential = json.loads(i) # loads() converts JSON to dictionary
        if username in dict_credential and dict_credential.get(username) == password:
            print("Login Successful")
            break
else:
    print("Login Failed")
    
# FOR ELSE => It behaves as a loop
# If break is encountered in for part, it exits the loop\
# If break is not encountered in for part, the else part is executed


# Task: Update this program using function and loops and everything that is taught