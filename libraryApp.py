import sqlite3

from sqlite3 import Error

def findItemInLibrary():
    itemName = input("Enter the name of the item you wish to search: ")
    cur.execute("Select * from record Where name=\'" + itemName + "\'")
    rows = cur.fetchall()

    if not rows:
        print("Item not found")
        return
    else:
        print("******Search Results******\n")
        index = 0
        for row in rows:
            print(index, " -- ", end = " ")
            print(row)
            index = index + 1
        choice = int(input("Enter the row you wish to select: "))
        print("\nYou have selected the following:")
        print(rows[choice])
        print("\n******RETURNING TO MAIN MENU******\n")
        
'''
def borrowItemFromLibrary():

def returnBorrowedItem():

def donateItemToLibrary():

def findEventInLibrary():

def registerForEventInLibrary():

def volunteerForLibrary():

def askForHelpFromLibrarian():
'''
def displayOptions():
    print(" Options: ")
    print(" F : Find an item in the library.")
    print(" B : Borrow and item from the library.")
    print(" R : Return a borrowed item.")
    print(" D : Donate an item to the library.")
    print(" E : Find an event in the library.")
    print(" A : Register for an event in the library.")
    print(" V : Volunteer for the library.")
    print(" H : Ask for help from a librarian.")
    print(" X : Exit the applitcation.")

con = sqlite3.connect('library.db')
cur = con.cursor()
print("Opened Database successfully \n")
exitFlag = 0
print(" Welcome to Library Database Application ")
print("-----------------------------------------")
while exitFlag != 1:
    displayOptions()
    val = input("Enter your choice: ")
    val.upper()
    if val == "F":
        findItemInLibrary()
    elif val == "B":
        borrowItemFromLibrary()
    elif val == "R":
        returnBorrowedItem()
    elif val == "D":
        donateItemToLibrary()
    elif val == "E":
        findEventinLibrary()
    elif val == "A":
        registerForEventInLibrary()
    elif val == "V":
        volunteerForLibrary()
    elif val == "X":
        print("Exiting Program\nGoodbye!")
        exitFlag = 1
    else:
        print("That is not an option. Please try again.")
    
