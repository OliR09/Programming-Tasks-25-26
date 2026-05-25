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


def calculate_average(values):
    if len(values) == 0:
        raise ValueError("The list cannot be empty")
    total = 0.0
    for i in values:
        total += i

    return total / len(values)


def main():
    pass
    numbers = []

    UserNum = input("Enter a list of numbers separated by spaces: ")
    split_numbers = UserNum.split()
    for num in split_numbers:
        try:
            numbers.append(float(num))
        except ValueError:
            print(num, " is not a valid number")

    if len(numbers) > 0:
        average = calculate_average(numbers)
        print(average)
    else:
        print("No valid numbers were entered.")


if __name__ == "__main__":
    main()
