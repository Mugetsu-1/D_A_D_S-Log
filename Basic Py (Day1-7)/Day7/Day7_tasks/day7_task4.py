# Check if a given number is palindrome or not

def check_palindrome():
    num = input("Enter a number: ")
    
    if num == num[::-1]:
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")

check_palindrome()