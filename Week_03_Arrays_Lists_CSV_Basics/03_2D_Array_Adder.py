"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D arraw and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():

    array = []

name = ""
age = ""

while name != "xxx":
    name = input("Enter your name, type xxx to finish: ")
    if name!= "xxx":
        age = input("Enter your age: ")
        array.append([name, age])
print(array)
choice = int(input("Who do you want to delete, in numbers"))
choice -= 1
array.pop(choice)
print(array)
    
    pass


if __name__ == "__main__":
    main()
