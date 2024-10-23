#Write a programm that checks if a given number is between 10 and 20(20 is inclusive) use logical operators
number=int(input("enter number:"))
if 10 < number <= 20:
    print(f"{number} is between 10 and 20 ( 20 inclusive)")
else:
    print(f"{number} is not between 10 and 20 (20 inclusive)")

# #Write a programm that prints the squares of all integers from 1 to 10 using a for loop
integers=[1,2,3,4,5,6,7,8,9,10]
for m in integers:
    m= m * m
    print(m)

#Write a simple programm that asks a user for their age, if the user is greater or equal to 18; adult and you are qualified, else: you are not qualified
age= int(input("Enter your age"))
if age >= 18:
    print("adult, you are qualified")
else:
    print("you are not qualified") 

#We have the following student details and marks; enter these details from the keyboard.
#   student_name=Ritah Liz
#   student_number=SEP23/BCS/14
#   programming=78
#   data_science=89
#   computer_applications=55
#a) Calculate the average mark and print the answer in three decimal places
student_name="Ritah Liz"
student_number="SEP23/BCS/14"
programming=78
data_science=89
computer_applications=55
total_sum= programming + data_science + computer_applications
number=3
average=(total_sum / number)
print(total_sum)
print(average)

# Write a programm that converts celsius temperature to fahrenheit.the programm should ask a user to enter the temperature in celsius and display the temp to fahrenheit

temperature =float(input("Enter the temperature in °C: "))
fahrenheit_temp =(9/5)*temperature + 32
print(f"The temperature  in °F is:{fahrenheit_temp:.3f}°F")

#A car's miles per gallons can be calculated with the following fomula. Write the programm that asks the user for the number of miles driven and gallons used.It should calculate the cars's miles and display the results
#fomula is; MPG=Miles driven/ gallons of gas used

miles_driven = float(input("enter the miles_driven: "))
gallons = float(input("enter the number of gallons: "))              
mpg = miles_driven/gallons
print(f"The cars miles per gallons used are: {mpg:.3f}")


