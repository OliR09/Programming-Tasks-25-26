"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
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
    
for i in range(1, len(numbers)):
    current = numbers[i]
    j = i - 1
    
    while j >= 0 and numbers[j] > current:
        numbers[j+1] = numbers[j]
        j -= 1
        
    numbers[j + 1] = current
    
    
    
print(numbers)
    pass


if __name__ == "__main__":
    main()
