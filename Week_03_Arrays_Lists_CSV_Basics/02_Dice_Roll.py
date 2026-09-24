"""
TASK: 02 Dice Roll

# Skills: RNG, Loops
Simulate rolling a six-sided die X number of times:
Print each roll, store all values in a list of updated totals for each number (56 ones for example):
Allow the user to print:
- Totals for each side
- average dice roll
- Counts for each of the 6 sides
- Extend (look up how to use mathplotlib and produce a bar graph for all of the statistics)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
   
    import random

rolls = []
total = 0

numberOfRolls = int(input("How many times will you roll the dice?"))

for i in range(numberOfRolls):
    rolled = random.randint(1,6)
    print("Roll: ", rolled)
        
    rolls.append(rolled)
    total += rolled 
print(total)
    
    pass


if __name__ == "__main__":
    main()
