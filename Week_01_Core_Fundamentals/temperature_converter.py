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

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    while True:
        print("Celcius to Fahrenheit: 1")
        print("Fahrenheit to Celcius: 2")
        print("Exit: 3")
        choice = input("Choose an option: ")
        if choice == "1":
            celsius = float(input("Enter a temperature in Celcius: "))
            print("The temperature in Fahrenheit is:", celsius_to_fahrenheit(celsius))
        elif choice == "2":
            fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
            print("The temperature in Celsius is:", fahrenheit_to_celsius(fahrenheit))
        elif choice == "3":
            break


if __name__ == "__main__":
    main()
