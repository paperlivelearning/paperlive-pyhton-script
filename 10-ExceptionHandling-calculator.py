# Basic calculator program in Python using while loop

print("Simple Calculator")
print("-----------------")
print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    try:
        choice = input("Enter operation number (1-5) : ")

        if choice == "5":
            print("Exiting calculator...")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = num1 + num2
            operation = "+"
        elif choice == "2":
            result = num1 - num2
            operation = "-"
        elif choice == "3":
            result = num1 * num2
            operation = "*"
        elif choice == "4":
            result = num1 / num2
            operation = "/"
        else:
            print("Invalid operator!")
            continue

        print("-----------------")
        print(f"{num1} {operation} {num2} = {result}")
        print("-----------------")
    
    except ValueError:
        print("Invalid number! Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except Exception as e:
        print("An error occurred:", str(e))

