# Simple Calculator Program

print("=== CALCULATOR ===")

# Function definitions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "NOT DEFINED (division by zero)"
    return a / b

while True:
    # Menu
    print("\nSelect operation:")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. EXIT")

    # Input choice with validation
    try:
        x = int(input("Enter choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if x == 5:
        print("Exiting calculator. Goodbye!")
        break

    if x not in (1, 2, 3, 4):
        print("Invalid choice! Please select between 1 and 5.")
        continue

    # Get numbers
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number! Please enter numeric values.")
        continue

    # Perform operation
    if x == 1:
        result = add(a, b)
    elif x == 2:
        result = sub(a, b)
    elif x == 3:
        result = mult(a, b)
    elif x == 4:
        result = divide(a, b)

    print("Result:", result)
