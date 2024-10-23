# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 

def temperature():
    temperature = float(input("Enter the temperature:"))
    if temperature < 0:
        print("freezing.")
    elif 0 <= temperature <= 10:
        print("cold")
    elif 11 <= temperature <= 20:
        print("moderate")
    elif 21 <= temperature <= 30:
        print("warm")
    else:
        print("hot")
temperature()
    







# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place

import math
def volume_of_the_sphere():
    radius= float(input("Enter the radius of the sphere"))
    pie=math.pi
    volume = (4/3) *pie*radius**2
    print(f"The volume of the sphere with radius {radius} is {volume:.1f}")
volume_of_the_sphere() 

# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 

def calculate_bmi():
    weight = float(input("\n Enter the weight in kg"))
    height = float(input("\nEnter the height in m "))
    BMI = weight/height
    if weight <= 18.5:
       print("underweight")
    elif 18.5 <= weight <= 24.9:
        print("Normal weight")
    elif 25 <= weight <= 29.9:
        print("Over weight")
    else:
        print("obese")
calculate_bmi()






# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)

import math
def volume_cylinder():
    radius = float(input("Enter the radius of the cylinder"))
    height = float(input("Enter the height of the cylinder"))
    volume = math.pi * (radius**2) * height
    print(f"The volume of the is{volume}")
volume_cylinder()

# Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50%                Fail 

def grades():
    grade = int(input("Enter the mark:"))
    if 90 <= grade <= 100:
        print("Grade is A")
    elif 80 <= grade <= 89:
        print("Grade is B")
    elif 70 <= grade <= 79:
        print("Grade is C")
    elif 60 <= grade <= 69:
        print("Grade is D")
    elif 50 <= grade <= 59:
        print("Grade is E")
    else:
        print("fail")
grades()





#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.

favourite_foods = ["chicken", "liver", "sandwich", "pizza", "burgers",  "beef"]
favourite_foods.append("ice cream")
favourite_foods.append("beef")
favourite_foods.remove("pizza")
print("Updated list of favourite foods:", favourite_foods)



#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.

numbers= [2, 5, 8, 10, 3, 6]
first_element = [0]
last_element = [-1]
print("first element:", first_element)
print("last element:",last_element)

reversed_element = numbers[-1]
print("List of reversed order:", reversed_element)

total_sum = sum(numbers)
print("sum of all elements:", total_sum)