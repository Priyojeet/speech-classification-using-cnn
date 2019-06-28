from tkinter import *
import tkinter.messagebox

window = Tk()
window.geometry("600x600")
window.title("testing")

def printt():
    first = fn.get()
    second = ln.get()
    dob1 = dob.get()
    gen = radio_var.get()
    print(f"{first}{second}{dob1}{gen}")
    tkinter.messagebox.showinfo("welcome", 'user is registered!!')

def exit1():
    exit()


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

b1 = Button(window, text='Signup', width=12, command=printt)
b1.place(x=150, y=440)

b2 = Button(window, text='exit', width=12, command=exit1)
b2.place(x=300, y=440)


window.mainloop()

