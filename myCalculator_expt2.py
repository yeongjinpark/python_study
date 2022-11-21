

# myCalculator3.py

from tkinter import *
from decimal import *

# key input function:
def click(key):
    display.insert(END, key)

##### main:
window = Tk()
window.title("MyCalculator")

# top_row frame generation
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# entry widget that can be changed
display = Entry(top_row, width=45, bg="light green")
display.grid()

# digit button frame geneartion
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
'7',  '8',  '9',
'4',  '5',  '6',
'1',  '2',  '3',
'0',  '.',  '=' ]

# genenrate digit buttons with loop
r = 0 # row counter
c = 0 # colum counter
for btn_text in num_pad_list:
    # this will be handled later:
    Button(num_pad, text=btn_text, width=5, command=click).grid(row=r,column=c)
    c = c+1
    if c > 2:
        c = 0
        r = r+1

# operater frame generation


# genenrate operator buttons with loop


##### main loop execution
window.mainloop()
