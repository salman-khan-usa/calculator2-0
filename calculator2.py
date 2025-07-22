from tkinter import *

def click(event):
    text = event.widget.cget("text")

    if text == '=':
        try:
            result =str(eval(str(sv.get())))
            sv.set(result)

        except:
            sv.set("Error")    

    elif text == 'C':
        sv.set("")
    
    elif text == '⌫':
        sv.set(sv.get()[:-1])
          

    else:
        sv.set(sv.get()+text)

root =Tk()
root.title("VIP CALCULATOR")
root.geometry('400x500')
root.configure(background='black')


#Setting screen value
sv = StringVar()

#Making Screen
screen = Entry(root,textvariable=sv,font=('Calibri',25,'bold'),justify=RIGHT,bg='black',fg='white',)
screen.pack(padx=5,pady=5,fill=X)


#Making frames for butons
f1 = Frame(root,bg='black')
f1.pack(pady=5)

f2 = Frame(root,bg='black')
f2.pack(pady=5)

f3 = Frame(root,bg='black')
f3.pack(pady=5)

f4 = Frame(root,bg='black')
f4.pack(pady=5)


#First Group of Button
b1 = Button(f1,text='1',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)

b2 = Button(f1,text='2',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
b2.pack(side=LEFT)
b2.bind("<Button-1>",click)

b3 = Button(f1,text='3',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
b3.pack(side=LEFT)
b3.bind("<Button-1>",click)

bd = Button(f1,text='/',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
bd.pack(side=LEFT)
bd.bind("<Button-1>",click)

#Second group of button

b4 = Button(f2,text='4',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
b4.pack(side=LEFT)
b4.bind("<Button-1>",click)

b5 = Button(f2,text='5',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
b5.pack(side=LEFT)
b5.bind("<Button-1>",click)

b6 = Button(f2,text='6',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
b6.pack(side=LEFT)
b6.bind("<Button-1>",click)

ba = Button(f2,text='+',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
ba.pack(side=LEFT)
ba.bind("<Button-1>",click)

#Third Group of Buttons
b7 = Button(f3,text='7',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
b7.pack(side=LEFT)
b7.bind("<Button-1>",click)

b8 = Button(f3,text='8',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
b8.pack(side=LEFT)
b8.bind("<Button-1>",click)

b9 = Button(f3,text='9',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
b9.pack(side=LEFT)
b9.bind("<Button-1>",click)

b0 = Button(f3,text='*',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
b0.pack(side=LEFT)
b0.bind("<Button-1>",click)


#LAst Group of buttons
bm = Button(f4,text='0',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
bm.pack(side=LEFT)
bm.bind("<Button-1>",click)

be = Button(f4,text='C',fg='red',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
be.pack(side=LEFT)
be.bind("<Button-1>",click)

bc = Button(f4,text='=',fg='green',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
bc.pack(side=LEFT)
bc.bind("<Button-1>",click)

bb = Button(f4,text='-',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=5,height=2)
bb.pack(side=LEFT)
bb.bind("<Button-1>",click)

bb = Button(root,text='⌫',fg='red',bg= 'black',font=("Helvetica", 16, "bold"),width=2,height=1)
bb.place(x=360,y=60)
bb.bind("<Button-1>",click)

bb = Button(root,text='.',fg='white',bg= 'black',font=("Helvetica", 16, "bold"),width=2,height=2)
bb.place(x=360,y=285)
bb.bind("<Button-1>",click)


root.mainloop()