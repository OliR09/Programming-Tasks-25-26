"""
TASK: 01 Csv Writer

# Skills: CSV writing
CAsk the user for:
- Name
- age
- favourite colour
- anything you want
Append this to a CSV file (Extend: allow user to choose to edit the file and read the file)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    
    import csv

filename = people.csv

def addPerson():
    name = input("Input your name: ")
    age = input("Input your age: ")
    colour = input("Input your favourite colour: ")
    with open(filename, "r", newLine = "") as file:
        writer = csv.write(file)
        write.writerow([name, age, colour])
    print("Person added")
    
def readFile():
    with open(filename, "r", newLine = "") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
                
def editPerson():
    people = []
    with open(filename, "r", newLine = "") as file:
        reader = csv.reader(file)
        people = list(reader)
    
if len(people) == 0:
    print("The file is empty")

for i, person in enumerate(people):
    print(i+1, person)
    
choice = int(input("Who do you want to edit?")) - 1

name = input("Enter the new age: ")
age = input("Enter the new age: ")
colour = input("Enter the new favourite colour: ")

people[choice] = [name, age, colour]

with open(filename, "w", newLine = "") as file:
    writer = csv.writer(file)
    writer.writerows(people)

    pass


if __name__ == "__main__":
    main()
