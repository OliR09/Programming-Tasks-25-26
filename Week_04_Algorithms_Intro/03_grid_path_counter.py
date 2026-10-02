"""
TASK: 03 Grid Path Counter

# Grid Path Counter - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b
Given an NxM grid:
- Count paths using recursion
- Count paths using iteration
Movement allowed: RIGHT or DOWN only.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
 
     rows = int(input("Input rows: "))
columns = int(input("Input columns: "))

grid = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(1)
    grid.append(row)
    
for i in range(1, rows):
    for j in range(1, columns):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
print(grid[rows-1][columns-1])

##program is finding out how many different ways you can go from top left to bottom right if 
##you can only move right and down

    
    pass


if __name__ == "__main__":
    main()
