# Simple Calculator App with For Loop

print("Simple Calculator")

# user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operations = [
    ("Addition", "+", num1 + num2),
    ("Subtraction", "-", num1 - num2),
    ("Multiplication", "*", num1 * num2),
    ("Division", "/", num1 / num2 if num2 != 0 else "Error: Division by zero"),
    ("Modulus", "%", num1 % num2 if num2 != 0 else "Error: Modulus by zero")
]

print("\nResults:")

for operation in operations:
    name, symbol, result = operation
    if "Error" in str(result):
        print(f"{name}: {num1} {symbol} {num2} = {result}")
    else:
        print(f"{name}: {num1} {symbol} {num2} = {result}")