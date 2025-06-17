num = int(input("Enter a number: "))
try:
    print(10/num)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
    print(f"Exception message: {e}")
except ValueError as e:
    print("Error: Invalid input. Please enter a valid number.")
    print(f"Exception message: {e}")