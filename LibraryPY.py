from GUI import *
from Tkinter import *
import os
from os.path import join
import datetime
bookData = open('bookData', 'w+')
userData = open('userData.txt', 'w+')

def command():
    button('Check out', checkOut())
    button('Check in', checkIn())
    button('Add a book', addBook())
    labels
    button('Add a user', addUser())

def checkOut():
    checkedOutBooks = []
    user = input('User number: ')
    checkedOutBooksInput = input('Type "done" when done./nBook number: ')
    while checkedOutBooksInput != 'done':
        checkedOutBooks.append(checkedOutBooksInput)
        checkedOutBooksInput = input('Type "done" when done./nBook number: ')
    
    
def checkIn():
    checkedInBooks = []
    user = input('User number: ')
    checkedInBooksInput = input('Type "done" when done./nBook number: ')
    while checkedInBooksInput != 'done':
        checkedInBooks.append(checkedInBooksInput)
        checkedInBooksInput = input('Type "done" when done./nBook number: ')

def addBook():
    bookName = input('Book name: ')
    bookAuthor = input('Book author: ')
    bookDate = input('Publishing date: ')
    bookISBN = input('ISBN: ')
    bookNumber = input('Book number: ')
    bookData.write(bookNumber + '=[' + bookName + ',' + bookAuthor + ',' + bookdate + ',' + bookISBN + 'no]') 
    
def addUser():
    userName1 = input('Name: ')
    userNumber = input('Number: ')
    userData.write(userNumber + '=[' + str(userName1) + ',none]')
