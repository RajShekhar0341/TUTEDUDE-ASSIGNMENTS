# TUTEDUDE-ASSIGNMENTS
**Task 1 – Basic Arithmetic Operations**

The first task is designed to take two numerical inputs from the user and perform four fundamental arithmetic operations: addition, subtraction, multiplication, and division.

**Code Explanation:**
num_one = int(input("Enter first no"))
num_two = int(input("Enter second no"))

The input() function collects data from the user via keyboard.
By default, input() returns data as a string, so int() is used to convert that input into an integer.
This process is repeated twice to get two separate numbers from the user.

addition = num_one + num_two
subtration = num_one - num_two
multiplication = num_one * num_two
division = num_one / num_two

Addition (+): Adds the two numbers.
Subtraction (-): Subtracts the second number from the first.
Multiplication (*): Multiplies the two numbers.
Division (/): Divides the first number by the second and returns a float result.
These results are stored in separate variables: addition, subtration, multiplication, and division.

code: 
print(addition)
print(subtration)
print(multiplication)
print(division)

The results of the above operations are displayed using print() statements.
However, these outputs are printed as raw numbers without context labels (like “Sum is:”), which may be confusing for some users.

**Summary of Concepts Demonstrated:**
Input handling using input()
Type conversion using int()
Arithmetic operators (+, -, *, /)
Output display using print()

**Task 2 – String Concatenation and Greeting Message**
The second task collects the user’s first and last name and generates a personalized greeting.

**Code Explanation:**
f_name = str(input("enter your first name"))
l_name = str(input("enter your last name"))

These lines prompt the user to enter their first and last name.
Even though input() already returns a string, the use of str() explicitly emphasizes type conversion.

full_name = f_name + " " + l_name

The two names are joined using the + operator along with a space " " in between.
This creates the full name in the format: First Last.

print(f"Hello good moring {full_name}")

This line prints a greeting message using an f-string, a modern Python feature for inserting variables into strings.
There’s a spelling mistake in the word “moring” which should be corrected to “morning.”

**Summary of Concepts Demonstrated:**
String input handling
String concatenation
String formatting using f-strings
Output display with personalized messaging


