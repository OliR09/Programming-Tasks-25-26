"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
   
    def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [9,8,7,6,5,4,3,2,1]
bubbleSort(array)
print(array)

    pass


if __name__ == "__main__":
    main()
