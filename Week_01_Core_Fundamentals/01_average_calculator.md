# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

def calculate_average():
    Values = []
    while True:
        num = int(input("Input numbers to find the average of, type "x" to finish))

        if num == "x":
            break

        try:
            Values.append(int(num))
        except:
            print("Please input a valid integer.")
    mean = sum(Values) / len(Values)
    print("Average is:", mean)

calculate_average(Values)