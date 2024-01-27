from tkinter import *
root=Tk()
e=Entry(root,borderwidth=19,text="please enter some thing")
e.insert(0,"enter your name:")
e.pack()
def myclick():

 mylabel=Label(root,text=e.get())
 mylabel.pack()
mybutton=Button(root,text="click me",command=myclick)

mybutton.pack()
root.mainloop()