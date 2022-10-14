from tkinter import *

root =Tk()
root.title("CLIENT")
text = Text(root,height=10,width=100)

def send2():
    send1="you-->"+ent.get()
    text.insert(END,"\n"+send1)
    ent.delete(0,END)

text.grid(column=0,row=0,columnspan=2)
ent = Entry(root,width=120)
ent.grid(column=0,row=1)
send= Button(root,text="SEND",command=send2,width=10)
send.grid(column=1,row=1)



root.mainloop()