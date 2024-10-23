#Write a Python program that:

#Prompts the user to enter two numbers.
#Calculates and displays:
#The sum of the two numbers.
#The difference between the first and second number.
#The product of the two numbers.
#The quotient of the first number divided by the second number. If the second number is zero, display a message indicating that division by zero is not allowed.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculating sum, difference, product, and quotient
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

# To avoid division by zero error
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "undefined (cannot divide by zero)"

# Displaying the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")