#Lets create a tag your share list game in python 

import random as r 
import time as t 
from tkinter import *
import tkinter.messagebox as mb

def check():
    if uname.get() == 'alone._.king._.jr' :
        mb.showinfo("Successful",'Account Verified Proceed Further Details')
        Label(game,text = "Enter Your Share List Person Name",font = font1,fg='black').grid(row=3,column=0)
        rels = StringVar()
        Entry(game,textvariable=rels,fg='black',font=font1,show=' * ').grid(row = 3, column = 2)
        rel = ['Best Friend','Just Friend','Crush','Love','Life Partner','Enemy','Bestie']
        def check_rel():
            rel = ['Best Friend','Just Friend','Crush','Love','Life Partner','Enemy','Bestie']
            mb.showinfo("Your Relation Ship is ",r.choice(rel))
        Button(game,text='Check Relation Ship ',font = font1,fg= 'black',command=check_rel).grid(row=3,column = 3)





game = Tk()
game.title("Check Your Insta RelationShip")
game.geometry("600x400")
font= 'Euphorigenic',25
font1 = 'Euphorigenic',15
Label(game,text = "Tag Your Share Your List",font = font , fg = 'black').grid(row = 0 ,column=2,columnspan=2)
Label(game,text = ' ').grid(row=1)
Label(game,text = 'Enter Your User Name',font = font1,fg='black').grid(row = 2,column = 0)
uname = StringVar()
Entry(game,textvariable=uname,fg='pink',font=font1).grid(row = 2, column = 2)
Button(game,text = 'Enter Your User Name',font = font1,fg='black',command = check).grid(row = 2,column = 3)




game.mainloop()