import random
from tkinter import *
from tkinter import messagebox

def copytoClip():
    root.clipboard_clear()
    root.clipboard_append(password)
def getval():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    num = "1234567890"
    symbols = "!@$%^&*()_-+={}[]:\";\'<>,.?/|\\ "
    global password
    password = ""
    word = ""
    try:
        if letter.get() == 1:
            word += letters
        if n.get() == 1:
            word += num
        if sy.get() == 1:
            word += symbols

        for a in range(int(l.get())):
            password += random.choice(word)

        thisentry.delete(0,END)
        thisentry.insert(0, password)

    except Exception as e:
        messagebox.showerror("Random Password Generator","Insufficient Data")

root=Tk()
root.title("Random Password Generator")
root.geometry("400x375")

frame1= Frame(root)
frame1.pack()
heading= Label(frame1,text="Generate Your Password Here!" , font="Courier 16 bold",pady=14)
heading.pack()

frame2= Frame(root, borderwidth=6,relief=SUNKEN)
frame2.pack()
frame3= Frame(frame2,pady=25)
frame3.pack()
length= Label(frame3,text="Lenght :")
length.grid(row=0,column=0,padx=20)

l=StringVar()
lenvalue= Entry(frame3,textvariable=l).grid(row=0,column=1,padx=20)

frame4= Frame(frame2)
frame4.pack()
a= Label(frame4,text="Which character types you want in your Password : " ).grid(row=0,column=0)

letter = IntVar()
n = IntVar()
sy = IntVar()
letters = Checkbutton(frame4,text="Letters ",variable= letter).grid(row=3,column=0)
number= Checkbutton(frame4,text="Numbers",variable= n).grid(row=4,column=0)
symbol= Checkbutton(frame4,text="Symbols ",variable= sy).grid(row=5,column=0)

frame6= Frame(frame2)
frame6.pack()
thisentry= Entry(frame6,text="",justify="center",bg="systembuttonface",border=0)
thisentry.pack()

frame5= Frame(frame2)
frame5.pack()
button1=Button(frame5,text="Get Strong Password",command=getval).grid(row=0,column=0,padx=10,pady=10)
button2=Button(frame5,text="Copy to Clipboard",command=copytoClip).grid(row=0,column=1,padx=10,pady=10)

root.mainloop()