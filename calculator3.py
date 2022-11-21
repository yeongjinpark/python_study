from tkinter import*
from decimal import*
# key input function:
def click(key):
    # =버튼이 눌렸을 떄 계산수행:
    if key=="=":
        try:
            result=str(eval(display.get()))[0:10]
            display.insert(END,"="+result)
        except:
            display.insert(END,"==>ERROR")
    # C버튼이 눌려졌을때 display 엔트리 위젯 내용 비움:
    elif key=="C":
        display.delete(0,END)
    #첫 번쨰 상수버튼에 대한 연결코드:
    elif key==constants_list[0]:
        display.insert(END,"3.141592654")
    elif key==constants_list[1]:
        display.insert(END,"300000000")
    elif key==constants_list[2]:
        display.insert(END,"330")
    elif key==constants_list[3]:
        display.insert(END,"149597887.5")
    
    
    #그 외
    else:
        display.insert(END,key)

##### main:
window=Tk()
window.title("MyCalculator")
# top_row frame generation
top_row=Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)
# entry widget that can be changed
display=Entry(top_row,width=45, bg="light green")
display.grid()
# digit button frame geneartion
num_pad=Frame(window)
num_pad.grid(row=1, column=0, sticky=W)
num_pad2=Frame(window)
num_pad2.grid(row=1, column=1, sticky=W)


pad3=Frame(window)
pad3.grid(row=2, column=0, sticky=W)
pad4=Frame(window)
pad4.grid(row=2, column=1, sticky=W)

num_pad_list=[
'7','8','9',
'4','5','6',
'1','2','3',
'0','.','=']

num_pad_list2=[
'*','/',
'+','-',
'(',')',
'C']

constants_list=[
'pi',
'sepped of light(m/s)',
'speed of sound(m/s)',
'average distance to sun(km)']

pad_list4=[
'factorial(!)',
'->roman',
'->binary',
'binary->10']

# genenrate digit buttons with loop
r=0# row counter
c=0# colum counter

for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    # this will be handled later:
    Button(num_pad,text=btn_text,width=5,command=cmd).grid(row=r,column=c)
    c=c+1
    print(btn_text);
    if c>2:
        c=0
        r=r+1
r=0
c=0

for btn_text in num_pad_list2:
    def cmd(x=btn_text):
        click(x)
    # this will be handled later:
    Button(num_pad2,text=btn_text,width=5,command=cmd).grid(row=r,column=c)
    c=c+1
    print(btn_text);
    if c>1:
        c=0
        r=r+1

r=0
c=0

for btn_text in constants_list:
    def cmd(x=btn_text):
        click(x)
    # this will be handled later:
    Button(pad3,text=btn_text,width=22,command=cmd).grid(row=r,column=c)
    c=c+1
    print(btn_text);
    if c>0:
        c=0
        r=r+1

r=0
c=0

for btn_text in pad_list4:
    def cmd(x=btn_text):
        click(x)
    # this will be handled later:
    Button(pad4,text=btn_text,width=12,command=cmd).grid(row=r,column=c)
    c=c+1
    print(btn_text);
    if c>0:
        c=0
        r=r+1

    
##### main loop execution
window.mainloop()
