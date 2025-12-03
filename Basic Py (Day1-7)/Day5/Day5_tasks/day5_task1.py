# Updated Simple Calculator with While Loop

print("SIMPLE CALCULATOR")

while True:
    print("\nOptions:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "6":
        print("Thank you for using the calculator. Goodbye!")
        break
    
    if choice in ["1", "2", "3", "4", "5"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                result = num1 + num2
                print(f"\n{num1} + {num2} = {result}")
                
            elif choice == "2":
                result = num1 - num2
                print(f"\n{num1} - {num2} = {result}")
                
            elif choice == "3":
                result = num1 * num2
                print(f"\n{num1} * {num2} = {result}")
                
            elif choice == "4":
                if num2 != 0:
                    result = num1 / num2
                    print(f"\n{num1} / {num2} = {result}")
                else:
                    print("Error: Cannot divide by zero!")
                    
            elif choice == "5":
                if num2 != 0:
                    result = num1 % num2
                    print(f"\n{num1} % {num2} = {result}")
                else:
                    print("Error: Cannot calculate modulus with zero!")
                    
        except ValueError:
            print("Error: Please enter valid numbers!")
    else:
        print("Invalid choice! Please enter 1-6.")
