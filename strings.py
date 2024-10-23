
#strings-in-depth.py
#strings in array like structured
#arrays in python are lists
#in arrays the first letter is 0
#example
marks=[90,60,70]#of the list in python(array)

name="whitney"
print(name[0])
print(name[6])

#looping through strings
#we loop through a string using keywords
#example
for character in name:
    print(character)

address="kigoma"
for character in address:
    print(character)

  #slicing in strings
  # we focus on accessing a range of characters in strings
  # we also envade in angle brackets
  #we include the start index and the end index
  # for example

print(name[1:3])
print(name[1:5])
print(name[1:4])
print(name[0:2])
message = "hello"
print(message[0:3])

#types of slicing
#negative slicing and positive slicing
#negative slicing
#we start from the right position and indexes are in negatves
message="hello"
print(message[-1])
print(message[-1:-5])
print(message[-1:-4])
print(message[-5:-3])
print(message[-4:])
print(message[4:])

#F STRINGS
#Work with formatted strings
#f is in lower case
#we don't concatenate
name="whitney"
age="20"
weiht=36.9441
height=46
print(f" my name is {name} and am {age} years old and i weigh {weiht} and my heiht is {height}")
total_cost=500000
print(f"total_cost is: {total_cost:,}")

#STRING MMETHOD
#Functions that we use to manupulate strings
#length len()
#space is counted in len
name="whitney"
total_length=len(name)
address="from Kigoma"
print(len(address))
print(len(name))
#b in upper case
print(name.upper())
#c in lower case
print(name.lower())

#Escape sequesces
#they always have a \
#\n-new line
#\t-tab
print("Hello world\nNice day")



