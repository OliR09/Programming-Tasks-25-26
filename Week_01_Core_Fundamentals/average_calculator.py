"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

from optparse import Values


def main():
    pass


if __name__ == "__main__":
    main()

def calculate_average(Values):
    total = 0
    for i in Values:
        total += i
    average = total / len(Values)
    return average
    while True:
        num = int(input("Input numbers to find the average of, type 'x' to finish"))

        if num == "x":
            break

        try:
            values.append(int(num))
        except:
            print("Please input a valid integer.")
    mean = sum(values) / len(values)
    print("Average is:", mean)

calculate_average(Values)