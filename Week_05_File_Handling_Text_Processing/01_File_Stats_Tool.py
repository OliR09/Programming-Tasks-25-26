"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():

    filename = input("Enter the filename: ")

file = open(filename, "r")

lines = 0
characters = 0
mostFreq = []

for line in file:
    line += 1
    characters += len(line)
    lineWords = line.split()
    for word in lineWords:
        mostFreq.append(word)
        
        
print("Number of lines:", lines)
print("Number of words:", len(mostFreq))
print("Number of characters:", characters)

mostFrequentWord = ""
highest = 0
for i in mostFreq:
    count = mostFreq.count(i)
    
    if count > highest:
        highest = count
        mostFrequentWord = i
        
print("Most frequent word is:", mostFrequentWord)
    
    pass


if __name__ == "__main__":
    main()
