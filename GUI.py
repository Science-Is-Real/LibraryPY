import time
from tkinter import *
root = Tk()
root.title('LibraryPY')
root.geometry('1500x720+0+0')
curLabels = []
curRow = 0
lRow = 0

def Talk(speech, x = 0):
    global curLabels
    global curRow
    curLabels.append(Label(root,text=speech))
    if curRow < 10:
        curLabels[-1].grid(row=curRow,column=0,sticky="w")
    else:
        curLabels = curLabels[1:]
        for x in range(10):
            curLabels[x].grid_forget()
            curLabels[x].grid(row=x,column=0,sticky="w")
        curLabels[-1].grid(row=10,column=0,sticky="w")
    curRow += 1
    if x == 0:
        Talk(" ",1)
    root.update()
nowRow = 1

def button(Text, Command):
    global nowRow
    b = Button(root, text = str(Text), command = Command).grid(row = nowRow, column = 15, sticky = 'w', pady = 10)
    nowRow += 1

def labels(Text):
    global nowRow
    l = Label(root, text = str(Text)).grid(row = nowRow - 1, column = 30)
labelOne = Label(root, text = 'Entry box  ').grid(row = 0, column = 20)
e = Entry(root, width = 60)
e.grid(row = 0, column = 30)
e.focus_set()
def callback():
    return e.get()
