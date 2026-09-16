"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    def checkPassword(password):
    length8 = False
    number = False
    SpecialCharacter = False
    Special = "@#£!%&*?"
    Capital = False
    Lower = False
    
    length = len(password)
    if length < 8:
        print("Password is too weak")
        
    for i in range(0, length):
        character = password[i]
        if character.isupper():
            Capital = True
        elif character.islower():
            Lower = True
        elif character.isdigit():
            number = True
        elif character in Special:
            SpecialCharacter = True
            
    if Capital == False:
        print("Your password must contain an uppercase letter")
    if Lower == False:
        print("Your password must contain a lowercase letter")
    if number == False:
        print("Your password must contain a number")
    if SpecialCharacter == False:
        print("Your password must contain a special character")
    else:
        print("Your password is strong")
            
password = "1234qweR#"
checkPassword(password)
    pass


if __name__ == "__main__":
    main()
