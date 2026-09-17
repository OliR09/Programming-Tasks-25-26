"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    shoppingList = []
    
    print("Enter your items for your shopping list. Type 'DONE' when finished")
    
    while True:
        item = input("Enter items:")
        if item == "DONE":
            break
        else:
            shoppingList.append(item)
            
    
    print("--SHOPPING LIST--")
    
    number = 1 
    for item in shoppingList:
        print(number, item)
        number += 1
        
    editChoice = input("Do you want to edit the list? y/n")
    if editChoice == "y":
        num = int(input("Input the number you want to edit"))
        newItem = input("Input the updated item")
        
        shoppingList[num - 1] = newItem
        
    print("The new list is:", shoppingList)
    pass


if __name__ == "__main__":
    main()
