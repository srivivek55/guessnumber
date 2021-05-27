
from Tkinter import *
from tkMessageBox import *
root=Tk()
root.config(background='purple')
root.geometry('750x800')
def fun(e=0):
    root.destroy()
img1=PhotoImage(file='yo.gif')
lb=Label(root,image=img1,bg='purple')
Label(root,text=' ',bg='purple').grid(row=0,column=0,sticky=N+S+E+W)
Label(root,text='NAME:- VIVEK SRIVASTAVA',font='Algerian 30 bold',fg='black',bg='purple').grid(row=1,column=1,sticky=N+S+E+W)
Label(root,text='ER NO.:- 171B155',font='Algerian 30 bold',fg='black',bg='purple').grid(row=2,column=1,sticky=N+S+E+W)
Label(root,text='BATCH:- B5',font='Algerian 30 bold',fg='black',bg='purple').grid(row=3,column=1,sticky=N+S+E+W)
Label(root,text='EMAIL ID:- vivekpopt2t@gmail.com',font='Algerian 30 bold',fg='black',bg='purple').grid(row=4,column=1,sticky=N+S+E+W)
Label(root,text='MOB NO.:- 7379509676',font='Algerian 30 bold',fg='black',bg='purple').grid(row=5,column=1,sticky=N+S+E+W)
lb.bind('<Button-1>',fun)
lb.bind('<Button-2>',fun)
lb.bind('<Button-3>',fun)
lb.grid(row=0,column=1,sticky=N+S+E+W)
showinfo('Hello','Please Click on the Photo to Continue')
root.mainloop()
