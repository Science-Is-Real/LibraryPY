from TKinter import *
bookData = open('bookData', 'w+')
userData = open('userData.txt', 'w+')

def checkOut():
    checkedOutBooks = []
    checkedOutBooksInput = input(

def checkIn():


def addBook():
    bookName = input('Book name: ')
    bookAuthor = input('Book author: ')
    bookDate = input('Publishing date: ')
    bookISBN = input('ISBN: ')
    bookNumber = input('Book number: ')
    bookData.write(bookNumber + '=[' + bookName + ',' + bookAuthor + ',' + bookdate + ',' + bookISBN + ']') 
    
def addUser():
    userName = input('Name: ')
    userNumber = input('Number: ')
    userData.write(userNumber + '=[' userName + ',none]')
