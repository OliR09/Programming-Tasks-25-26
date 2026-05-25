"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

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


def reverse_array(values):
    reversed_values = []
    index = len(values) - 1
    while index >= 0:
        reversed_values.append(values[index])
        index -= 1
    return reversed_values


def reverse_list(values):
    return reverse_array(values)
