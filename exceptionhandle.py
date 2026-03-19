# Exception Handling in Python

# 1. Basic try-except block
print("=== Basic Try-Except ===")
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid integer")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")


# 2. Multiple exceptions in one block
print("\n=== Multiple Exceptions ===")
try:
    data = [1, 2, 3]
    print(data[10])
except (IndexError, TypeError) as e:
    print(f"Caught error: {type(e).__name__} - {e}")


# 3. Try-except-else block
print("\n=== Try-Except-Else ===")
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input")
else:
    print(f"Your age is: {age}")


# 4. Try-except-finally block
print("\n=== Try-Except-Finally ===")
try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleanup operations executed")
    if 'file' in locals():
        file.close()


# 5. Custom exceptions
print("\n=== Custom Exceptions ===")
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"Caught custom exception: {e}")


# 6. Raising exceptions
print("\n=== Raising Exceptions ===")
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")