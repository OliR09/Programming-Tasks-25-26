"""
TASK: 03 Contact Book

# Store contacts in a text file, each line containing
name,phone,email
Program must allow:
- Add contact
- Search contact (sequential search)
- Display all

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():

  def addContact():
    with open("contactBook.txt", "a") as file:
        details = input("Input the name, phone and email. Type xxx to end")
        while details != "xxx":
            file.write(details + "\n")
            details = input("Input the name, phone and email. Type xxx to end")
            
def searchContacts():
    search = input("Input who what you are looking for: name, phone, email")
    
    with open("contactBook.txt", "r") as contactBook:
        lineNum = 0
        found = False
        for line in contactBook:
            lineNum += 1
            if search in line:
                print(line)
                print("Found on line", lineNum)
                found = True
        if not found:
            print("Contact not found")
            
def DisplayAll():
    with open("contactBook.txt", "r") as contactBook:
        for line in contactBook:
            print(line)
                
choice = int(input("What would you like to do? 1. Add contact.  2. Search Contacts.  3. Display all."))
if choice == 1:
    addContact()
elif choice == 2:
    searchContacts()
elif choice == 3:
    DisplayAll()
else:
    print("Please input a valid number")  
    
    pass


if __name__ == "__main__":
    main()
