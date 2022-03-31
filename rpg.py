from tkinter import *
from tkinter import messagebox
import random
import string

root = Tk()
root.title("Random Password Generator")
root.geometry('1000x800')
root.minsize(1000, 800)
root.maxsize(1000, 800)
root.configure(background="#676767")

f1 = Frame(root, width=500, height=330)
lab_title = Label(f1, width=50, font='sans-serif 12 bold', text="Hint: Enter Size >> Click: Generate Now", bd=1, relief=SOLID).pack()
f1.pack()

photo = PhotoImage(file="3.png")
genr_leb = Label(image=photo, width=500, height=330, bg="#676767", fg="white")
genr_leb.pack()


def rpg():
  global sc1
  passw=""
  length=int(c1.get())
  lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['@', '#', '$', '-', '!', '%', '&', '?']
  try:
    if(length>5 and length<30):
      all =lower+upper+num+symbols
      temp=random.sample(all, length)
      passw="".join(temp)
      sc1.set(passw)
    else:
      raise IOError
  except IOError:
      sc1.set(messagebox.showerror("ERROR !!!", "Oops! please enter number between 6 to 30"))
      sc1.set("")

def clean():
  messagebox.showinfo("Reset", "Reset Successfully !!!")
  sc1.set("")
  c1.set("")

def cop_y():
    root.clipboard_clear()
    root.clipboard_append(sc1.get())
    ccp.set(messagebox.showinfo("Info", "Password copied successfully"))

def about_us():
   top= Toplevel(root)
   top.geometry("900x250")
   top.title("About US!!!")
   Label(top, text="This application is developed by group of Sobit ,Vivek ,Kalyan & Yash.", font=('Georgia 14 bold')).pack()
   str=("As we know Passwords are a real security threat.\n Over 80% of hacking-related breaches are due to weak or stolen passwords, a recent report shows .\n So if you want to safeguard your personal info and assets, creating secure passwords is a big first step.\n And that’s where the LastPass Password Generator can help.\n Impossible-to-crack passwords are complex with multiple types of characters (numbers, letters, and symbols).\n Making your passwords different for each website or app also helps defend against hacking.\n This password generator tool runs locally on your Windows, Mac or Linux computer, as well as your iOS or Android device.\n The passwords you generate are never sent across the web.")
   Label(top, text=str, font=('Georgia 10')).pack()

sc1 = StringVar()
c1 = StringVar()
ccp = StringVar()
f2 = Frame(root, width=500, height=330)
lab_entry = Label(f2, text='Enter a number to get your password:',fg="white", font='Georgia 12 bold', bg="#676767").pack(side=LEFT)
c_entry=Entry(f2, textvariable=c1, width=24, fg="#676767", bg="white").pack()
f2.pack()

f4 = Frame(root, width=500, height=330)
Label(f4, text=' Your Password is :', font='Georgia 12 bold', fg="white", bg="#676767",width=29).pack()
f4.pack(pady=60)
e1= Entry(root, textvariable=sc1, font="Georgia 12 bold", width=45, fg="white", bg="#676767",bd=0).place(x=410,y=470)

Button(root, text="Reset", font="Georgia 12 bold", command=clean, bg="#Ff6700", fg="white").place(x=390, y=500)
Button(root, text="Copy", font="Georgia 12 bold", command=cop_y, bg="#Ff6700", fg="white").place(x=550, y=500)
Button(root, text="Generate Now", font="Georgia 12 bold", command=rpg).place(x=590, y=390)
Button(root, text="About us", font="Georgia 12 bold", bg="#Ff6700", fg="white", command=about_us).place(x=80,y=640)

root.mainloop()
