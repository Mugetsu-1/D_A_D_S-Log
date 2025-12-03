#Updated Calc with match case

print("Simple Calculator")

# user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")

choice = input("Enter your choice (1-5): ")

print("\nResult:")

match choice:
    case "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    case "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    case "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    case "4":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Cannot divide by zero!")
    case "5":
        if num2 != 0:
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        else:
            print("Error: Cannot calculate modulus with zero!")
    case _:
        print("Invalid choice! Please select between 1-5.")

