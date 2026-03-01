class InvalidAgeError(Exception):
    """Raised when an age is invalid."""
    pass

try:
    num1_str = input("Enter Name: ")
    num2_str = input("Enter Age: ")

    age = int(num2_str)

    print(f"Hello {num1_str}")

    if age < 0:
        raise InvalidAgeError("Age cannot be negative!")

    if age < 13:
        print ("You are a Child")
    elif age > 13 and age <= 17:
        print ("You are a Teenager")
    elif age > 18 and age <= 59:
        print ("You are an Adult")
    elif age > 60:
        print ("You are a Senior Citizen")

    if age >=18:
        print ("You are eligible to vote")
    else:
        print("You are not eligible to vote")

    print(f"You will be {age+1} next year ")


except InvalidAgeError:
    print ("Age cannot be negative")
except ValueError:
    print("Invalid age input")