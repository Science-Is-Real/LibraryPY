import GUI.py
from TKinter import *
bookData = open('bookData', 'w+')
userData = open('userData.txt', 'w+')

def checkOut():
    checkedOutBooks = []
    checkedOutBooksInput = input(' Type "done" when done./nBook number: ')
    while checkedOutBooksInput != done:
        checkedOutBooks.append(checkedOutBooksInput)
        checkedOutBooksInput = input(' Type "done" when done./nBook number: ')
    
    
def checkIn():
    

def addBook():
    bookName = input('Book name: ')
    bookAuthor = input('Book author: ')
    bookDate = input('Publishing date: ')
    bookISBN = input('ISBN: ')
    bookNumber = input('Book number: ')
    bookData.write(bookNumber + '=[' + bookName + ',' + bookAuthor + ',' + bookdate + ',' + bookISBN + ']') 
    
def addUser():
    userName1 = input('Name: ')
    userNumber = input('Number: ')
    userData.write(userNumber + '=[' + str(userName1) + ',none]')
