# Print all the even numbers in a list of numbers.

def print_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("Original list:", numbers)
    print("Even numbers:", end=" ")
    
    for num in numbers:
        if num % 2 == 0:
            print(num, end=" ")

print_even_numbers()