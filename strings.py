name = "bhushan"
print(name[3:1:-1])  # Slice the string
print(len(name))  # Prints the length of the string
print(list(name))  # Converts string to list
print(name.upper())  # Make the whole string in uppercase
print(name.capitalize())  # Make the first letter of string capital
print(name.isalnum())  # Returns true if the string is alphanumeric
print(name.count("h"))  # Counts the element present in number
name[0] = "a"  # It will throw an error because strings are immutable and cannot be changed
