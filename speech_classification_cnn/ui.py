from tkinter import *
import tkinter.messagebox
from finalizing import *
#from recordForRegistration import *


global s
window = Tk()
window.geometry("600x600")
window.title("testing")

def printt():
    first = fn.get()
    second = ln.get()
    dob1 = dob.get()
    gen = radio_var.get()
    s = f"{first}{second}{dob1}{gen}"
    print(s)
    #tkinter.messagebox.showinfo("welcome", 'user is registered!!')
    return s




def exit1():
    exit()

def destro():
    window.destroy()


def checking_window():
    win = Tk()
    win.title("welcome to the prediction")
    win.geometry("600x600")
    label5 = Label(win, text="let's check your voice prediction")
    label5.place(x=30, y=70)
    butn1 = Button(win, text='Record voice', width=12, command=getAudio)
    butn1.place(x=80, y=120)
    
    butn2 = Button(win, text='Predict', width=12, command=makePred)
    butn2.place(x=400, y=120)
    
    butn3 = Button(win, text='Exit', width=12, command=exit1)
    butn3.place(x=220, y=200)
    

fn = StringVar()
ln = StringVar()
dob = StringVar()
radio_var = StringVar()

label = Label(window, text = "registration form")
label.place(x=90, y =53)

label1 = Label(window, text = "fname:-")
label1.place(x=70, y =130)
entry1 = Entry(window, textvar = fn)
entry1.place(x=130, y=132)


label2 = Label(window, text = "lname:-")
label2.place(x=70, y =170)
entry1 = Entry(window, textvar = ln)
entry1.place(x=130, y=172)


label3 = Label(window, text = "dob:-")
label3.place(x=70, y =210)
entry3 = Entry(window, textvar = dob)
entry3.place(x=130, y=212)


label4 = Label(window, text = "gender :-")
label4.place(x=70, y=242)

r1 = Radiobutton(window, text="Male", variable=radio_var, value="Male")
r1.place(x=130, y=245)
r2 = Radiobutton(window, text="Female", variable=radio_var, value="Female")
r2.place(x=200, y=245)

lbl = Label(window, text = "click the recordVoice button")
lbl.place(x=70, y=280)
btn = Button(window, text='recordVoice', width=12)
btn.place(x=70, y=310)

b1 = Button(window, text='Register', width=12, command=printt)
b1.place(x=150, y=440)


b2 = Button(window, text='exit', width=12, command=destro)
b2.place(x=300, y=440)

b3 = Button(window, text='predict voice', width=12, command=checking_window)
b3.place(x=220, y=500)


window.mainloop()
