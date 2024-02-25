# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    else:
        return a / b

# Function to display the menu of operations
def display_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Main program
while True:
    display_menu()
    choice = input("Enter choice (1/2/3/4/5): ")

    # Exit the program if choice is 5
    if choice == '5':
        print("Thank you for using the simple calculator!")
        break

    # Request input of two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Call functions according to choice
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please choose again.")