import tkinter as tk
from tkinter import *
from tkinter import messagebox

root=tk.Tk()
root.title('TIC TAC TOE')
def disable():
     b1.config(state='disable')
     b2.config(state='disable')
     b3.config(state='disable')
     b4.config(state='disable')
     b5.config(state='disable')
     b6.config(state='disable')
     b7.config(state='disable')
     b8.config(state='disable')
     b9.config(state='disable')
def check_win():
    global winner
    winner=False
    if b1['text'] +b2['text']+b3['text']=='XXX' :
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        winner=True
        messagebox.showinfo('TIC TAC TOE','X WINS')
        disable()
    elif b4['text'] +b5['text']+b6['text']=='XXX':
          b4.config(bg='red')
          b5.config(bg='red')
          b6.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','X WINS')
          disable()
    elif b7['text'] +b8['text']+b9['text']=='XXX':
          b7.config(bg='red')
          b8.config(bg='red')
          b9.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','X WINS')
          disable()
    elif b1['text'] +b3['text']+b5['text']=='XXX':
          b7.config(bg='red')
          b8.config(bg='red')
          b9.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','X WINS')
          disable()
    elif b2['text'] +b4['text']+b6['text']=='XXX' :
          b2.config(bg='red')
          b4.config(bg='red')
          b6.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','X WINS')
          disable()
    elif b3['text'] +b6['text']+b9['text']=='XXX' :
          b3.config(bg='red')
          b6.config(bg='red')
          b9.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','X WINS')
          disable()
    elif b1['text'] +b5['text']+b9['text']=='XXX' :
          b1.config(bg='red')
          b5.config(bg='red')
          b9.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','X WINS')
          disable()
    elif b3['text'] +b5['text']+b7['text']=='000' :
          b3.config(bg='red')
          b5.config(bg='red')
          b7.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','O WINS')
          disable()
    elif b1['text'] +b2['text']+b3['text']=='OOO' :
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        winner=True
        messagebox.showinfo('TIC TAC TOE','O WINS')
        disable()
    elif b4['text'] +b5['text']+b6['text']=='OOO' :
          b4.config(bg='red')
          b5.config(bg='red')
          b6.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','O WINS')
          disable()
    elif b7['text'] +b8['text']+b9['text']=='OOO' :
          b7.config(bg='red')
          b8.config(bg='red')
          b9.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','O WINS')
          disable()
    elif b1['text'] +b3['text']+b5['text']=='OOO' :
          b7.config(bg='red')
          b8.config(bg='red')
          b9.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','O WINS')
          disable()
    elif b2['text'] +b4['text']+b6['text']=='OOO' :
          b2.config(bg='red')
          b4.config(bg='red')
          b6.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','O WINS')
          disable()
    elif b3['text'] +b6['text']+b9['text']=='OOO' :
          b3.config(bg='red')
          b6.config(bg='red')
          b9.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','O WINS')
          disable()
    elif b1['text'] +b5['text']+b9['text']=='OOO' :
          b1.config(bg='red')
          b5.config(bg='red')
          b9.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','O WINS')
          disable()
    elif b3['text'] +b5['text']+b7['text']=='OOO' :
          b3.config(bg='red')
          b5.config(bg='red')
          b7.config(bg='red')
          winner=True
          messagebox.showinfo('TIC TAC TOE','O WINS')
          disable()
    if count==9 and winner==False:
          messagebox.showinfo('TIC TAC TOE','IT IS A TIE')
          disable()

def b_click(b):
    global count,clicked
    if b['text']=='' and clicked ==True:
        b['text']='X'
        clicked=False
        count=count+1
        check_win()
    elif b['text']=='' and clicked==False:
        b['text']='O'
        clicked=True
        count=count+1
        check_win()
    else:
        messagebox.showerror('TIC TAC TOE','ALREADY FILLED')

count=0
clicked=True #clicked is true when value is X and false when value is 0
  
b1=tk.Button(root,text='',font=('TIMES NEW ROMAN',20),height=3,width=6,bg='pink',command=lambda : b_click(b1))
b2=tk.Button(root,text='',font=('TIMES NEW ROMAN',20),height=3,width=6,bg='pink',command=lambda : b_click(b2))
b3=tk.Button(root,text='',font=('TIMES NEW ROMAN',20),height=3,width=6,bg='pink',command=lambda : b_click(b3))
b4=tk.Button(root,text='',font=('TIMES NEW ROMAN',20),height=3,width=6,bg='pink',command=lambda : b_click(b4))
b5=tk.Button(root,text='',font=('TIMES NEW ROMAN',20),height=3,width=6,bg='pink',command=lambda : b_click(b5))
b6=tk.Button(root,text='',font=('TIMES NEW ROMAN',20),height=3,width=6,bg='pink',command=lambda : b_click(b6))
b7=tk.Button(root,text='',font=('TIMES NEW ROMAN',20),height=3,width=6,bg='pink',command=lambda : b_click(b7))
b8=tk.Button(root,text='',font=('TIMES NEW ROMAN',20),height=3,width=6,bg='pink',command=lambda : b_click(b8))
b9=tk.Button(root,text='',font=('TIMES NEW ROMAN',20),height=3,width=6,bg='pink',command=lambda : b_click(b9))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
     
root.mainloop()
