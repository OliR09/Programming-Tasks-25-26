"""
TASK: 05 File Word Search

# Skills: File reading, loops, Data mining
Ask user for a filename and a search term. https://sherlock-holm.es/ascii/ is a site that has the entire collection of Sherlock Holmes
Load the file and count how many lines contain the search term

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
  
filename = input("Input the filename")
searchTerm = input("Input the term to search")

file = open(filename, "r")
count = 0
for line in file:
    if searchTerm in line:
        count += 1
        
print("Number of lines: ", count)
  

pass


if __name__ == "__main__":
    main()
