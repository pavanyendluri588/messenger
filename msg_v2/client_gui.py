import  tkinter as tk
import time
import client1

class main_window():
    def __init__(self):
       self.root1 = tk.Tk()

       self.screem_width=int(self.root1.winfo_screenwidth())
       self.screem_height=int(self.root1.winfo_screenheight())
       self.root1.geometry(f'{self.screem_width-1000}x{self.screem_height-300}+450+100')
       self.root1.resizable(True,True)
       self.root1.title("client")

       self.connection_frame= tk.Frame(self.root1,width=self.screem_width,height=self.screem_height)
       self.connection_frame.pack()
       self.connection_frame_label =tk.Label(self.connection_frame,text="WELCOME TO SERVER CONNECTOR")
       self.connection_frame_label.place(x=10,y=10)
       self.connection_frame_code_label=tk.Label(self.connection_frame,text="code:")
       self.connection_frame_code_label.place(x=20,y=100)
       self.connection_frame_code_var=tk.IntVar()
       #self.connection_frame_code_var.set()
       self.connection_frame_code_entry=tk.Entry(self.connection_frame,textvariable=self.connection_frame_code_var)
       self.connection_frame_code_entry.place(x=65,y=100)
       self.connection_frame_submit_button  = tk.Button(self.connection_frame,text='submit',command=self.submit_fun)
       self.connection_frame_submit_button.place(x=40,y=150)



       self.connnected_frame=tk.Frame(self.root1,width=self.screem_width,height=self.screem_height)
       #self.connnected_frame.place(x=0,y=0)
       self.connnected_frame_conneected_label= tk.Label(self.connnected_frame,text='connected')
       self.connnected_frame_conneected_label.place(x=100,y=400)
       self.connnected_frame_back_button=tk.Button(self.connnected_frame,text="<back",command=self.back_fun)
       self.connnected_frame_back_button.place(x=300,y=0)





       self.failed_frame =tk.Frame(self.root1,width=self.screem_width,height=self.screem_height)
       #self.failed_frame.place(x=0,y=0)
       self.failed_frame_failed_label = tk.Label(self.failed_frame, text='failed connection')
       self.failed_frame_failed_label.place(x=100, y=400)
       self.failed_frame_back_button = tk.Button(self.failed_frame, text="<back",command=self.failed_frame_back_fun)
       self.failed_frame_back_button.place(x=300, y=0)
       self.root1.mainloop()

    def submit_fun(self):
        print("submit function is called")
        self.connection_frame.pack_forget()
        self.failed_frame.pack_forget()
        self.connnected_frame.pack()
        print("submit function is ended")
    def back_fun(self):
        print("back function is called")
        self.connnected_frame.pack_forget()
        self.failed_frame.pack_forget()
        self.connection_frame.pack()
        print("back function is ended")
    def failed_frame_back_fun(self):
        print("back function is called")
        self.connnected_frame.pack_forget()
        self.connection_frame.pack_forget()
        self.failed_frame.pack()
        print("back function is ended")
    def sleep_fun(self,n):
        time.sleep(n)
        self.back_fun()




obj = main_window()

