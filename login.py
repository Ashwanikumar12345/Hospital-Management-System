# Created on : 25-Oct-2023, 1:30:33 am
# Author     : Mukesh Shah
#=========================IMPORTING MODULES========================================

import tkinter
from functools import partial
from tkinter import messagebox
from PIL import ImageTk, Image
#=========================LOGIN CREDENTIALS========================================

def validateLogin(username, password):
    if username.get() == "admin" and password.get() == "123" :
        homep()
    else:
        tkinter.messagebox.showinfo("ERROR" , "NO USER FOUND!!!")

#=========================PAGE HOPPERS=============================================

def homep():
    f.destroy()
    import main

#===========================LOGIN WINDOW===========================================

f = tkinter.Tk()
f.title("Login Screen")
f.geometry("1540x800+0+0")
l = tkinter.Label(f , bd = 10 , relief = 'ridge' , text = "CHECKUP CLINIC" , fg = "Black" , bg = "Grey" , font = ("Times New Roman" , 30 , 'bold'))
l.pack(side = "top" , fill = 'x')

#============================FRAMES================================================
#Frames are the boundary in which all code is displayed
df = tkinter.Frame(f, bd=20, relief='solid',bg = 'white')
df.place(x=0, y=70, width=1540, height=635, )

dfc = tkinter.Frame(df , bd=20 , bg= 'light blue', relief = 'groove' )
dfc.place(x=350 , y = 70 , width = 780 , height = 400)
#Labels are used for texts
l1 = tkinter.Label(df, bd=10, text="LOGIN ", font=("Times New Roman", 28, 'bold')).pack(side='top', fill='x')

dfright = tkinter.Frame(df ,bd = 10 ,relief = "ridge")
dfright.place(x=770, y=150, width=275, height=200)
load= Image.open(r"C:\Users\Mukesh Shah\Desktop\WhatsApp Image 2024-03-13 at 01.04.11_93bac95e.jpg")
render = ImageTk.PhotoImage(load)
img = tkinter.Label(dfright, image=render)
img.pack()


#=============================================LOGIN LABELS==============================================================

usernameLabel = tkinter.Label(dfc, text="Username:" , font = ("Arial" , 15,'bold'), padx=2,pady=3,relief = 'ridge',bg="white").place(x=50,y=125)
username = tkinter.StringVar()
usernameEntry = tkinter.Entry(dfc, textvariable=username,relief = 'sunken').place(x=160,y=126, height = 32, width = 150)
passwordLabel = tkinter.Label(dfc, text="Password:" , font = ("Arial" , 14, 'bold'),padx=2,pady=3,bg="white",relief = 'ridge').place(x=50,y=175)
password = tkinter.StringVar()
passwordEntry = tkinter.Entry(dfc, textvariable=password, show='*',relief = 'sunken').place(x=158,y=176, height = 31, width = 152)
validateLogin = partial(validateLogin, username, password)
loginButton = tkinter.Button(dfc, text="Login", command=validateLogin,padx=2,pady=3).place(x=165,y=250, width = 100)


#MAILOOP IS USED TO EXECUTE AND RUN THE GUI
f.mainloop()