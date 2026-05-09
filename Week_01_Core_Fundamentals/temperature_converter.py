"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


if __name__ == "__main__":
    main()

while True:
    print("Celcius to Fahrenheit: 1")
    print("Fahrenheit to Celcius: 2")
    print("Exit: 3")
    choice = input("Choose an option: ")
    if choice == "1":
        celcius = float(input("Enter a temperature in Celcius: "))
        fahrenheit = (celcius * 1.8) + 32
        print("The temperature in fahrenheit is:", fahrenheit)
    elif choice == "2":
        fahrenheit = float(input("Enter a temperature in Fahrenheit:"))
        celcius = (fahrenheit - 32) / 1.8
        print("The temperature in celcius is:", celcius)
    elif choice == "3":
        break