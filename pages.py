import tkinter as tk
from tkinter import *
import qrcode

my_qrcode = qrcode.Qrcode()

def login():
    #getting form data
        uname=username.get()
        pwd=password.get()
        #applying empty validation
        if uname=='' or pwd=='':
            message.set("fill the empty field!!!")
        else:
            if uname=="abcd@gmail.com" and pwd=="abc":
                exit()
            else:
                message.set("Wrong username or password!!!")
        #defining loginform function

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,width="40",height="15", text="Auto Login Page",font=('Helvetica', 18, "bold"),
                bg="orange",fg="white").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go To Email Address",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Go To QRCode Access",
                  command=lambda: master.switch_frame(PageTwo)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        global  message
        global username
        global password
        username = StringVar()
        password = StringVar()
        message=StringVar()
        tk.Frame.__init__(self, master)
        tk.Label(self, width="40",height="15",text="Email Address",font=('Helvetica', 18, "bold"),
                bg="orange",fg="white").pack(side="top", fill="x", pady=5)
        tk.Label(self, text="Username * ").place(x=175,y=260)
        #Username textbox
        tk.Entry(self, textvariable=username).place(x=245,y=262)
        #Password Label
        tk.Label(self, text="Password * ").place(x=175,y=300)
        #Password textbox
        tk.Entry(self, textvariable=password ,show="*").place(x=245,y=302)
        #Label for displaying login status[success/failed]
        tk.Label(self, text="",textvariable=message).place(x=260,y=320)
        #Login button
        tk.Button(self, text="Login", width=10, height=1, bg="white",command=login).place(x=270,y=340)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, width="40",height="15",text="QRCode Access",font=('Helvetica', 18, "bold"),
                bg="orange",fg="white").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        my_qrcode.Qrcode_publisher()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()