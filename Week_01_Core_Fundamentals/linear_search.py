"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random


def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def main():
    values = random.sample(range(1, 100), 10)
    target = int(input("Enter a number to search for: "))
    print(linear_search(values, target))


if __name__ == "__main__":
    main()
