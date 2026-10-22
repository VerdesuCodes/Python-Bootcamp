#checking the type of different data types in Python

print(type("Hello")) # This will print the type of the string "Hello", which is <class 'str'>.

print(type(123)) # This will print the type of the integer 123, which is <class 'int'>.

print(type(123.456)) # This will print the type of the float 123.456, which is <class 'float'>.

print(type(True)) # This will print the type of the boolean value True, which is <class 'bool'>.

str()
int()
float()
bool()

name = input("What is your name? ")
n_characters= len(name)
n_characters_str = str(n_characters)

print("Your name has " + n_characters_str + " characters.")