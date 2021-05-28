import sqlite3 
import flash

from Tkinter import *
from tkMessageBox import *
from random import randint
con=sqlite3.Connection('VIVEKDB.db')
cur=con.cursor()
cur.execute("create table if not exists ggame(name varchar(15),score integer(5),accuracy number(5,3))")
con.commit()



acc=0.0
l=3


            
cc=0
root=Tk()
root.config(background='yellow')
root.title('Welcome')
root.geometry("700x470")
Label(root,text='Welcome To',bg='yellow',fg='black',font='times 25 bold',width='22').grid(row=0,column=1,columnspan=2)
img=PhotoImage(file='1.gif')
Label(root,image=img).grid(row=2,column=1)

#Label(root,text=' ').grid(row=1,column=1)
#Label(root,text=' ').grid(row=2,column=1)
Label(root,text='Enter Your Name ',font='Calibri 14 bold',bg='yellow').grid(row=3,column=0)
def close():
    a1=askquestion('Exit','Are you Sure ?')
    if a1=='yes':
        root.destroy()
        
    
e1=Entry(root,width='29',bd=5,bg='grey',font='Arial 12 bold')
e1.grid(row=3,column=1,columnspan=4)


#Label(root,text=' ').grid(row=3,column=0)
#Label(root,text=' ',bg='white').grid(row=4,column=0)
#Label(root,text=' ').grid(row=5,column=3)
#Label(root,text=' ').grid(row=6,column=4)
#Label(root,text=' ').grid(row=7,column=1)
Button(root,text='Exit',font='Arial 10 bold',fg='white',bg='black',width=10,command=close).grid(row=8,column=5)

def fun():
    cur.execute("drop table ggame")
    
    cur.execute("create table if not exists ggame(name varchar(15),score integer(5),accuracy integer(2,2))")
    con.commit() 
            
    
    global z
    number=randint(1,10)
    root=Tk()
    #root.geometry('400x200')
    root.config(background='orange')
    root.title('Game Starts')
    #root.geometry("700x500")
    #Label(root,text=' ').grid(row=0,column=0)
    #Label(root,text=' ',bg='white').grid(row=1,column=1)
    #Label(root,text=' ').grid(row=1,column=2)
    #Label(root,text=' ').grid(row=1,column=3)
    Label(root,text='Welcome '+e1.get(),font='Verdana 30 italic bold',bg='orange').grid(row=1,column=0)
    Label(root,text='Please guess any number between 1 and 10       Attempts allowed- 3 ',font='Calibri 15 bold',bg='orange').grid(row=3,column=0)
    e2=Entry(root,width=8,bd=5,bg='grey',font='Arial 12 bold')
    #Label(root,text=' ').grid(row=3,column=1)
    #Label(root,text=' ').grid(row=4,column=2)
    e2.grid(row=4,column=0)
    #def dest():
        #m=askquestion('Play Again','Are You Sure')
        #if m=='yes':
            #root.destroy()
    def fun1():
        global acc
        global l
        global cc
    
       
        
        
       
        if e2.get()=='':
            Label(root,text='                              *Enter valid Value*                                ',font='Calibri 15 bold',bg='orange').grid(row=7,column=0)
            
        elif int(e2.get())<1:
            #a=askretrycancel('Warning','Please Enter value between 1 and 20')
            Label(root,text='                              *Enter valid Value*                                ',font='Calibri 15 bold',bg='orange').grid(row=7,column=0)
            #count(str(z))
            e2.delete(0,END)
            #\print z
            #fun()
            #Button(root,text='Submit',font='Arial 8 bold',bg='grey',fg='black',command=fun).grid(row=5,column=1)
            if l==0:
                r=Tk()
                r.config(background='red')
                r.title('Better Luck Next Time ')
                Label(r,text='You are out of Your 3 Attempts...The correct answer is '+str(number),fg='black',bg='red',font='Calibri 40 bold' ).pack()
                root.destroy()
                def de():
                    r.destroy()
                    
                Button(r,text='Exit',fg='white',bg='black',font='Arial 10 bold',width=10,command=de).pack()
                r.mainloop()
        elif int(e2.get())>10:
            
            Label(root,text='                         *Enter valid Value*                              ',font='Calibri 15 bold',bg='orange').grid(row=7,column=0)
           
            
            #count(str(z))
            e2.delete(0,END)
            if l==0:
                r=Tk()
                r.config(background='red')
                r.title('Better Luck Next Time ')
                Label(r,text='You are out of Your 3 Attempts...The correct answer is '+str(number),fg='black',bg='red',font='Calibri 40 bold' ).pack()
                root.destroy()
                def de():
                    r.destroy()
                    
                Button(r,text='Exit',fg='white',bg='black',font='Arial 10 bold',command=de).pack()
                r.mainloop()
            
              #Button(root,text='Submit',font='Arial 8 bold',bg='grey',fg='black',command=fun1).grid(row=5,column=1)
        
        elif int(e2.get())<number:
            l-=1
            cc+=1
            Label(root,text='*Your guess is too low...Enter Again       Attempts left- '+str(l),font='Calibri 15 bold',bg='orange').grid(row=7,column=0)
            #count(str(z))
            e2.delete(0,END)
            #askokcancel('Wrong guess','Your guess is too low')
            #fun()
            #Button(root,text='Submit',font='Arial 8 bold',bg='grey',fg='black',command=fun).grid(row=5,column=1)
            if l==0:
                r=Tk()
                r.config(background='red')
                r.title('Better Luck Next Time ')
                Label(r,text='You are out of Your 3 Attempts...The correct answer is '+str(number),fg='black',bg='red',font='Calibri 40 bold' ).pack()
                root.destroy()
                def de():
                    r.destroy()
                    
                Button(r,text='Exit',fg='white',bg='black',font='Arial 10 bold',command=de).pack()
                r.mainloop()
                
        elif int(e2.get())>number:
            l-=1
            cc+=1
            #askokcancel('Wrong guess','Your guess is too high')
            Label(root,text='*Your guess is too High...Enter Again       Attempts left- '+str(l),font='Calibri 15 bold',bg='orange').grid(row=7,column=0)
            #count(str(z))
            e2.delete(0,END)
            #fun()
            #Button(root,text='Submit',font='Arial 8 bold',bg='grey',fg='black',command=fun).grid(row=5,column=1)
            if l==0:
                r=Tk()
                r.config(background='red')
                r.title('Better Luck Next Time ')
                Label(r,text='You are out of Your 3 Attempts...The correct answer is '+str(number),fg='black',bg='red',font='Calibri 40 bold' ).pack()
                root.destroy()
                def de():
                    r.destroy()
                    
                Button(r,text='Exit',fg='white',bg='black',font='Arial 10 bold',command=de).pack()
                r.mainloop()
        
        
                        
        elif l==0:
                r=Tk()
                r.config(background='red')
                r.title('Better Luck Next Time ')
                Label(r,text='You are out of Your 3 Attempts...The correct answer is '+str(number),fg='black',bg='red',font='Calibri 40 bold' ).pack()
                root.destroy()
                def de():
                    r.destroy()
                    
                Button(r,text='Exit',fg='white',bg='black',font='Arial 10 bold',command=de).pack()
                r.mainloop()
        else:
            l=l-1
            cc+=1

            
            Label(root,text='                                        YOU GOT IT RIGHT                                           ',font='Calibri 15 bold',bg='orange').grid(row=7,column=0)
            
            #count(str(z))
            #e2.delete(0,END)
            #Label(root,text='*#*Your guess is correct in '+str(cc)+' attempt*#*',font='Calibri 18 bold').grid(row=6,column=0)
            root1=Tk()
            root1.config(background='cyan')
            root1.title('You Won!')
            Label(root1,text='Hurray!',bg='cyan',fg='black',font='Verdana 80 bold').grid(row=0,column=0)
            Label(root1,text='Your Guess is Correct in ' +str(cc)+ ' attempts',font='Calibri 30 bold',bg='cyan').grid(row=1,column=0)
            #print 'guess right in '
            #print gt
            #print 'attempts'
            #askokcancel('Right guess','Your guess is correct in '+str(gt)+' attempts')
            if l==2:
                acc=100
            elif l==1:
                acc=66
            elif l==0:
                acc=33
            else:
                acc=0
        
    Label(root,text=' ',bg='orange').grid(row=5,column=0)
    z=Button(root,text='Guess',font='Arial 10 bold',fg='white',bg='black',command=fun1).grid(row=6,column=0)
    #m=Button(root,text='Play Again',font='Arial 10 bold',fg='white',bg='black',command=dest).grid(row=6,column=0)
    #z.bind('<Button-1>',mcount)
    #z.grid(row=5,column=1)
Button(root,text='Submit',font='Arial 10 bold',fg='white',bg='black',command=fun).grid(row=5,column=1)
p=str(e1.get())
cur.execute("insert into ggame values(?,?,?)",(p,cc,acc))
def scoreboard():
    #frame=Tk()
    
    p=str(e1.get())

    
    cur.execute("insert into ggame values(?,?,?)",(p,cc,acc))
    con.commit()
    #print p,cc,acc
    
    cur.execute("select * from ggame")
    i=cur.fetchall()
    score=Tk()
    score.title('ScoreBoard')
    Label(score,text='Name',bg='yellow',fg='black',font='Calibri 20 bold').grid(row=0,column=0)
    Label(score,text=' ',bg='yellow').grid(row=0,column=1)
    Label(score,text=' No. of attempts',bg='yellow',fg='black',font='Calibri 20 bold').grid(row=0,column=2)
    Label(score,text=' ',bg='yellow').grid(row=0,column=3)
    Label(score,text=' Accuracy in %',bg='yellow',fg='black',font='Calibri 20 bold').grid(row=0,column=4)
    score.config(background='yellow')
    Label(score,text=str(i[0][0]),bg='yellow',font='Calibri 15 italic').grid(row=1,column=0)
    Label(score,text=' ',bg='yellow').grid(row=1,column=1)
    Label(score,text=str(i[0][1]),bg='yellow',font='Calibri 15 italic').grid(row=1,column=2)
    Label(score,text=' ',bg='yellow').grid(row=1,column=3)
    Label(score,text=str(i[0][2]),bg='yellow',font='Calibri 15 italic').grid(row=1,column=4)
    def dele():
        cur.execute("drop table ggame")
        score.destroy()
    Button(score,text='Reset',bg='black',fg='white',bd=4,command=dele).grid(row=2,column=2)
    score.mainloop()
    #return i
    #print acc
    #Label(frame,text=str(i)).grid(row=0,column=0)
    #e1.delete(0,END)
    con.commit()
Button(root,text='ScoreBoard',font='Arial 10 bold',fg='white',bg='black',width=10,command=scoreboard).grid(row=8,column=0)
            
    





root.mainloop()
