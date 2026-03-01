try:
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")

    num1 = int(num1_str)
    num2 = int(num2_str)

    print(f"Sum: {num1 + num2}")

    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"Division: {num1 / num2}")

except ValueError:
    print("Invalid input")