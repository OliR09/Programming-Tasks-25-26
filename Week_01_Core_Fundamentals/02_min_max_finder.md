# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

def find_min_max(Values):
    max_value = Values
    for i in Values:
        if i > max_value:
        max_value = i
    min_value = Values
    for i in Values:
        if i < min_value:
        min_value = i
    print(min_value, max_value)


