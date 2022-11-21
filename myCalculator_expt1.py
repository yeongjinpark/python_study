

# myCalculator_expt1.py

from tkinter import *
from decimal import *


##### main:
window = Tk()
window.title("MyCalculator")

# Result display with entry widget
display = Entry(window, width=45, bg="light green")
display.grid()

# generate digit button:
def click1():
    display.insert(END, "1")
    
Button(window, text="1", width=5, command=click1).grid(row=1,column=0)

def click2():
    display.insert(END, "2")
Button(window, text="2", width=5, command=click2).grid(row=2,column=0)
def click3():
    display.insert(END, "3")
Button(window, text="3", width=5, command=click3).grid(row=3,column=0)

##### main loop execution
window.mainloop()
