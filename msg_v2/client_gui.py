import  tkinter as tk
import time
import client3
import socket

class main_window():
    def __init__(self):
       self.root1 = tk.Tk()

       self.screem_width=int(self.root1.winfo_screenwidth())
       self.screem_height=int(self.root1.winfo_screenheight())
       self.root1.geometry(f'{535}x{600}+450+100')
       self.root1.resizable(True,True)
       self.root1.title("client")

       self.connection_frame= tk.Frame(self.root1,width=self.screem_width,height=self.screem_height)
       self.connection_frame.pack()
       self.connection_frame_label =tk.Label(self.connection_frame,text="WELCOME TO SERVER CONNECTOR")
       self.connection_frame_label.place(x=10,y=10)
       self.connection_frame_name_label =tk.Label(self.connection_frame,text="username:")
       self.connection_frame_name_label.place(x=10,y=50)
       self.connection_frame_name_var = tk.StringVar()
       self.connection_frame_name_entry = tk.Entry(self.connection_frame,textvariable=self.connection_frame_name_var)
       self.connection_frame_name_entry.place(x=70,y=50)
       self.connection_frame_code_label=tk.Label(self.connection_frame,text="code:")
       self.connection_frame_code_label.place(x=20,y=100)
       self.connection_frame_code_var=tk.StringVar()
       self.connection_frame_code_var.set( socket.gethostbyname(socket.gethostname()))
       #self.connection_frame_code_var.set()
       self.connection_frame_code_entry=tk.Entry(self.connection_frame,textvariable=self.connection_frame_code_var)
       self.connection_frame_code_entry.place(x=65,y=100)

       self.connection_frame_port_label = tk.Label(self.connection_frame, text="port:")
       self.connection_frame_port_label.place(x=200, y=100)
       self.connection_frame_port_var = tk.IntVar()
       self.connection_frame_port_var.set(9999)
       # self.connection_frame_code_var.set()
       self.connection_frame_port_entry = tk.Entry(self.connection_frame, textvariable=self.connection_frame_port_var)
       self.connection_frame_port_entry.place(x=255, y=100)

       self.connection_frame_submit_button  = tk.Button(self.connection_frame,text='submit',command=self.submit_fun)
       self.connection_frame_submit_button.place(x=40,y=150)



       self.connnected_frame=tk.Frame(self.root1,width=self.screem_width,height=self.screem_height,bg='green')
       #self.connnected_frame.place(x=0,y=0)
       self.connnected_frame_text_indiaplay_box=""
       self.connnected_frame_conneected_label= tk.Label(self.connnected_frame,text='connected to server',font=("Comic Sans MS", 20, "bold"))
       self.connnected_frame_conneected_label.place(x=130,y=0)
       self.connnected_frame_back_button=tk.Button(self.connnected_frame,text="<back",command=self.back_fun,font=("TkDefaultFont", 10, "bold"))
       self.connnected_frame_back_button.place(x=480,y=0)
       self.connnected_frame_text_displlay_label= tk.Text(self.connnected_frame,width=57,height=26,bg='grey',fg='white',font=("TkDefaultFont", 13, "bold"))
       self.connnected_frame_text_displlay_label.place(x=7,y=50)
       self.connnected_frame_massage_input_var=tk.StringVar()
       self.connnected_frame_massage_input_entry=tk.Entry(self.connnected_frame,textvariable=self.connnected_frame_massage_input_var,font=("TkDefaultFont", 15, "bold"))
       self.connnected_frame_massage_input_entry.config(width=40,fg='red')
       self.connnected_frame_massage_input_entry.place(x=10,y=555,height=38)
       self.connnected_frame_send_button=tk.Button(self.connnected_frame,text="send",font=("TkDefaultFont", 15, "bold"),command=self.connnected_frame_send_fun)
       self.connnected_frame_send_button.place(x=465,y=555)




       self.failed_frame =tk.Frame(self.root1,width=self.screem_width,height=self.screem_height)
       #self.failed_frame.place(x=0,y=0)
       self.failed_frame_failed_label = tk.Label(self.failed_frame, text='failed connection')
       self.failed_frame_failed_label.place(x=100, y=400)
       self.failed_frame_back_button = tk.Button(self.failed_frame, text="<back",command=self.failed_frame_back_fun)
       self.failed_frame_back_button.place(x=300, y=0)
       self.root1.mainloop()

    def submit_fun(self):

        #if client3.connect(self.connection_frame_code_var.get(),self.connection_frame_port_var.get()) == 'connected':
        if 'connected' == 'connected':
            self.connection_frame.pack_forget()
            self.failed_frame.pack_forget()
            self.connnected_frame.pack()
        #elif client3.connect(self.connection_frame_code_var,self.connection_frame_port_var) == 'failed':
        elif 'failed1' == 'failed':
            self.connection_frame.pack_forget()
            self.connnected_frame.pack_forget()
            self.failed_frame.pack()


        """print("submit function is called")
        self.connection_frame.pack_forget()
        self.failed_frame.pack_forget()
        self.connnected_frame.pack()
        print("submit function is ended")
        """
    def back_fun(self):
        print("back function is called")
        self.connnected_frame.pack_forget()
        self.failed_frame.pack_forget()
        self.connection_frame.pack()
        print("back function is ended")
    def connnected_frame_send_fun(self):
        self.connnected_frame_text_displlay_label.delete("1.0","end")
        self.send_data="["+self.connection_frame_name_var.get()+"]>"+self.connnected_frame_massage_input_var.get()+"\n"
        print("self.send_data",self.send_data)
        self.connnected_frame_text_indiaplay_box = self.connnected_frame_text_indiaplay_box + self.send_data
        print("self.connnected_frame_text_indiaplay_box:",self.connnected_frame_text_indiaplay_box)
        self.connnected_frame_text_displlay_label.insert(tk.END,"\n"+self.connnected_frame_text_indiaplay_box)
        self.connnected_frame_massage_input_var.set("")
    def failed_frame_back_fun(self):
        print("back function is called")
        self.connnected_frame.pack_forget()
        self.connection_frame.pack()
        self.failed_frame.pack_forget()
        print("back function is ended")
    def sleep_fun(self,n):
        time.sleep(n)
        self.back_fun()





obj = main_window()

