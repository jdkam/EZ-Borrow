import sqlite3
import datetime

from sqlite3 import Error
from datetime import date

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
        while choice > len(rows)-1:
            print("Not a valid selection")
            choice = int(input("Enter the row you wish to select: "))
        
        print("\nYou have selected the following:")
        print(rows[choice])
       
        
        print("\n******RETURNING TO MAIN MENU******\n")
    
def borrowItemFromLibrary():
    today = str(date.today())
    name = input("Enter your name: ")
    itemName = input("Enter the name of the item you wish to borrow: ")
    recordId = input("Enter the record ID of the item you wish to borrow: ")
    cur.execute("Select * from record Where name=? AND recordID=?", (itemName, recordId))
    rows = cur.fetchall()

    if not rows:
        print("Item not found")
        return
    else:
        cur.execute("Update record Set availability='no',personBorrowing=?,dateBorrowed=? Where recordID=? AND name=?", (name, today, recordId, itemName))
        con.commit()
        print("\n******RETURNING TO MAIN MENU******\n")
  
def returnBorrowedItem():
    itemName = input("Enter the name of the item you wish to return: ")
    recordId = input("Enter the record ID of the item you wish to return: ")
    cur.execute("Select * from record Where name=? AND recordID=?",(itemName, recordId))
    rows = cur.fetchall()

    if not rows:
        print("Item not found")
        return
    else:
       cur.execute("Update record Set availability='yes', personBorrowing=NULL,dateBorrowed=NULL Where recordID=? AND name=?", (recordId, itemName))
       con.commit()
       print("\n******RETURNING TO MAIN MENU******\n")
    
def donateItemToLibrary():
    recordType = input("Enter the item type you wish to donate: ")
    recordName = input("Enter the item name you wish to donate: ")
    isbn = input("Enter the ISBN of the item you wish to donate: ")
    recordId = input("Enter the record ID of the item you wish to donate: ")
    library = input("Enter the library you wish to donate to: ")
    cur.execute("Select * from library where libraryName=\'" + library + "\'")
    rows = cur.fetchall()

    if not rows:
        print("Library not found")
        return
    else:
        cur.execute("Insert into record values (?,?,?,?,'yes',NULL,NULL)",(isbn, recordId, recordType, recordName))
        cur.execute("Insert into owns values(?,?,?)", (library, isbn, recordId))
        con.commit()
        print("\n******RETURNING TO MAIN MENU******\n")
def findEventInLibrary():
    library = input("Enter the library where the event is held: ")
    eventName = input("Enter the event name you wish to find: ")
    cur.execute("Select libraryName,eventName,event.eventType,event.time,event.date,event.room,event.audienceType From hosts join event On hosts.eventName=event.name Where libraryName=? AND eventName=?", (library,eventName))
    rows = cur.fetchall()

    if not rows:
        print("Library or event not found")
        return
    else:
        print("******Search Results******\n")
        index = 0
        for row in rows:
            print(index, " -- ", end = " ")
            print(row)
            index += 1
        print("\n******RETURNING TO MAIN MENU******\n")
    
def registerForEventInLibrary():
    userId = input("Enter your user ID: ")
    eventName = input("Enter the event name you wish to register for: ")
    cur.execute("Select * From event Where name=\'" + eventName + "\'")
    rows = cur.fetchall()

    if not rows:
        print("Event not found")
        return
    else:
        cur.execute("Insert into attending values(?,?)", (eventName, userId))
        con.commit()
        print("\n******RETURNING TO MAIN MENU******\n")
    
def volunteerForLibrary():
    library = input("Enter the library you wish to volunteer for: ")
    userId = input("Enter your user ID: ")
    cur.execute("Select libraryName, userID From library, people Where libraryName=? AND userID=?", (library, userId))
    rows = cur.fetchall()

    if not rows:
        print("Library or user ID not found")
        return
    else:
        cur.execute("Insert into personnel values (?,?)", (userId, "Volunteer"))
        cur.execute("Insert into worksAt values (?,?)", (library, userId))
        con.commit()
        print("You are now registered as a volunteer at ", library)
        print("\n******RETURNING TO MAIN MENU******\n")


'''
def askForHelpFromLibrarian():
''' 
def displayOptions():
    print(" Options: ")
    print(" F : Find an item in the library.")
    print(" B : Borrow an item from the library.")
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
print(" Welcome to CMPT 354 Library Database Application ")
print(" Authors: Jordan Kam, Austin Kwan")
print("--------------------------------------------------")
while exitFlag != 1:
    displayOptions()
    val = input("Enter your choice: ").upper()
    if val == "F":
        findItemInLibrary()
        print("\n")
    elif val == "B":
        borrowItemFromLibrary()
        print("\n")
    elif val == "R":
        returnBorrowedItem()
        print("\n")
    elif val == "D":
        donateItemToLibrary()
        print("\n")
    elif val == "E":
        findEventInLibrary()
        print("\n")
    elif val == "A":
        registerForEventInLibrary()
        print("\n")
    elif val == "V":
        volunteerForLibrary()
        print("\n")
    elif val == "H":
        askForHelpFromLibrarian()
        print("\n")
    elif val == "X":
        exitFlag = 1
    else:
        print("That is not an option. Please try again.\n")
    
print("Exited application successfully.")
