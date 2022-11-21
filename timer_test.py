import tkinter as tk
import time

def startTimer():
    time.sleep(1)
    global timer
    timer += 1
    timeText.configure(text=str(timer))
    window.after(10, startTimer)
    

window = tk.Tk()

timer = 0

timeText = tk.Label(window, text="0", font=("Helvetica", 80))
timeText.pack()




startTimer()
window.mainloop()
