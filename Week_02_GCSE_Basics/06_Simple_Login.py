"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():

    def loadDetails(filename="logindetails.txt"):
    details = {}
    with open (filename, "r") as file:
        for line in file:
            line = line.strip()
            if line and ":" in line:
                username, password = line.split(":", 1)
                details[username] = password
    return details

    def loginSystem():
        userDatabase = loadDetails()
        
        attempts = 0
    
        while attempts < 3:
            username = input("Enter your username:")
            password = input("Enter your password:")
            
            if username in userDatabase and userDatabase[username] == password:
                print("Welcome")
                return True
            else:
                attempts += 1
                print("Access Denied",3 - attempts, "attempts remaining")
                
                if attempts == 3:
                    print("No remaining attempts left.")
                    return False
                    
    loginSystem()
        
    pass


if __name__ == "__main__":
    main()
