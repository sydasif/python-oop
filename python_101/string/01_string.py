# Creating Strings
first_name = "Mike"
last_name = " Driscoll"
full_name = first_name + last_name
print(full_name)

# Converting an integer to a string
number = 5
string = str(number)
print(string)

# Escape sequences
escape_quote = "This string has a single quote, ', in the middle"
print(escape_quote)

escape_quote = "This string has a single quote, ', in the middle"
print(escape_quote)

# String Methods
name = "mike"
capital_name = name.capitalize()
print(capital_name)

caps_name = name.upper()
print(caps_name)

# List string methods and attributes
dir(str)

# Using .split() method
my_string = "This is a string of words"
print(my_string.split())

# Accessing the second element after splitting
second_element = my_string.split()[1]
print(second_element)
