try:
    num1_str = input("Enter first Name: ")
    num2_str = input("Enter last Name: ")
    num3_str = input("Enter Age: ")

    age = int(num3_str)

    print(f"Full Name: {num1_str + num2_str}")
    print(f"You will be {age+1} next year ")

    if age < 0:
        print("Age cannot be negative")

except ValueError:
    print("Invalid age input")