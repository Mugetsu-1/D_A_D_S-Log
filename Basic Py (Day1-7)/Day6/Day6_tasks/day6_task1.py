# Simple Calculator with Functions

def display_menu():
    print("\nCalculator Menu:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exit")

def get_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Cannot calculate modulus with zero!"
    return a % b

def display_result(a, b, operator, result):
    print(f"\n{a} {operator} {b} = {result}")

def main():
    print("Simple Calculator!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == "6":
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice! Please enter 1-6.")
            continue
        
        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            continue
        
        result = None
        operator = ""
        
        if choice == "1":
            result = add(num1, num2)
            operator = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"
        elif choice == "4":
            result = divide(num1, num2)
            operator = "/"
        elif choice == "5":
            result = modulus(num1, num2)
            operator = "%"
        
        display_result(num1, num2, operator, result)

if __name__ == "__main__":
    main()