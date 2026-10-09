"""
TASK: 02 Simple Logger System

# Create a script that appends time-stamped log entries to a file.
Menu:
- Add Log
- View Log
- Clear Log

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():

    import time


def addLog():
    with open("Logs.txt", "w") as logsDoc:
        choice = input("Would you like to add another log? yes or no")
        if choice == "yes":
            types = input("Input the type of log ")
            desc = input("Input the description of the log")
            currentTime = time.strftime("%X")
            log = currentTime + "," + types + "," + desc + "\n"
            logsDoc.write(log)
    mainMenu()
            
def viewLogs():
    with open("Logs.txt", "r") as logsDoc:
        for line in logsDoc:
            print(line.strip())
    mainMenu()
                
def clearLogs():
    choice = input("Are you sure you want to clear all logs? yes or no")
    if choice == "yes":
        with open("Logs.txt", "w") as logsDoc:
            logsDoc.write("")
        print("Logs cleared")
    else:
        print("Cancelled")
    mainMenu()

def mainMenu():
    choice = int(input("What would you like to do now\n1. Add Log \n2. View logs \n3. Clear logs"))
    if choice == 1:
        addLog()
    elif choice == 2:
        viewLogs()
    elif choice == 3:
        clearLogs()
    else:
        print("Please use a valid number. 1,2,3")
        mainMenu()
    
mainMenu()

##time - TYPE - DESCRIPTION
    
    pass


if __name__ == "__main__":
    main()
