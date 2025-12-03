# Manage ad perform operation in file using python code

# File Handling flow
# 1. Open the file => open()
# 2. Perform operation => read(), write()
# 3. Close the file => close()


# There are 3 mode for opening a file
# "r" => For Reading a file. If file doesnot exist, it throws an error
# "w"=> For writing to file. If file doesnot exist, it creates a empty file
# "w" => When we write into a file in w mode, it removes all the previous content and writes the new content
# "a" => For append to the file. If file doesnot exist, it creates a empty file
# "a" => When we write into a file in a mode, it preserves all the previous content and adds the new content


# open(file_path, mode)
# file = open("abc.txt","a")
# file.write("Data Scientist"+"-") # =>  We can write in the file only in string or JSON data type
# file.close()

# JSON => JavaScript Object Notation
# JSON is similar to dictionary
# json = {
#     "name":"Saugat",
#     "surname":"Thapa"
# }


# file = open("abc.txt","r")
# content = file.read()
# file.close()

# print(content)

# # split() => Method of string data type. Returns List of strings
# a = content.split("-")
# print(a)

# if "Data Scientist" in a:
#     print("Data Science is present in a")
# else:
#     print("Data Science not found")


# Register
# username = input("ENter a username: ")
# file = open("credential.txt","a")
# file.write(username+"-")
# file.close()

# Login
username = input("Enter a username: ")
file = open("credential.txt","r")
content = file.read()
file.close()

usernames = content.split("-")
for i in usernames:
    if i == username:
        print("Login Successful")
        break
else:
    print("Login Failed")

# For Else 
# If break keyword found in for loop, it exits the loop
# Else the else part is executed

# Task: Update login register using file handling