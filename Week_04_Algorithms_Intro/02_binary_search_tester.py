"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():

import random
numbers = []

for i in range(10):
    numbers.append(random.randint(1,100))
    
numbers.sort()

low = 0 
high = len(numbers) - 1

print(numbers)
target = int(input("What is the target number?"))

found = False

while low <= high:
    middle = (low + high) // 2
    
    if numbers[middle] == target:
        found = True
        print("Found at index",middle + 1)
        break
    elif numbers[middle] < target:
        low = middle + 1
    else:
        high = middle - 1
        
if found:
    print("Found")
    
else:
    print("Not found")
    
    pass


if __name__ == "__main__":
    main()
