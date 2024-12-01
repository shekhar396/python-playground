# String initialization
str1 = 'a'
str2 = 'b'

# Concatenating strings
print(str1 + str2)  # Outputs: 'ab'

# Repeating a string multiple times
print(5 * str1)  # Outputs: 'aaaaa'

# Getting the ASCII value of characters
print(ord(str1))  # Outputs: 97 (ASCII value of 'a')
print(ord(str2))  # Outputs: 98 (ASCII value of 'b')

# Using chr to get characters from ASCII values
print(chr(97) * 5)  # Outputs: 'aaaaa'
print(chr(98))      # Outputs: 'b'

# Working with a string
the_string = "Hello World"

# Attempting to delete a character by index (will raise an error since strings are immutable)
# del the_string[1]  # Uncommenting this line will cause a TypeError

# Iterating over the string and printing characters with a space
for ch in the_string:
    print(ch, end=' ')  # Outputs: 'H e l l o   W o r l d'
print()  # For a new line

# Slicing the string
print(the_string[1:3])  # Outputs: 'el'

# Membership checks in a string
print("e" in the_string)       # Outputs: True
print("e" not in the_string)  # Outputs: False
