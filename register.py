from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk # pip install pillow
import pymysql #pip install pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration form")
        self.root.geometry("1350x700+0+0")
        
        self.bg=ImageTk.PhotoImage(file="bg/blk2.jpg",master=root)
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        frame1=Frame(self.root,bg="white")
        frame1.place(x=350,y=100,width=700,height=500)
        
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=40)
        
        fname=Label(frame1,text="First name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        
        Lname=Label(frame1,text="Last name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_Lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_Lname.place(x=370,y=130,width=250) 
        
        contact=Label(frame1,text="Phone number",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.txt_password=Entry(frame1,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=270,width=250)
        
        cpass=Label(frame1,text="Confirm password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_cpass=Entry(frame1,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_cpass.place(x=370,y=270,width=250)
        
        
     
        btn_register=Button(frame1,text="REGISTER NOW",font=("times new roman",15,"bold"),bg="green",fg="white",command=self.register_data).place(x=50,y=320)
        
        #btn_login=Button(frame1,text="LOGIN",font=("times new roman",15,"bold"),command=self.login_window,bg="green",fg="white").place(x=250,y=320)
        
    def login_window(self): 
        self.root.destroy()
        
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_Lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpass.delete(0,END) 
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_Lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_cpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpass.get():
            messagebox.showerror("Error","passwords must match",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="user")
                cur=con.cursor()
                cur.execute("select * from user where email=%s",self.txt_email.get())
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","user already exists,try with another email",parent=self.root)
                cur.execute("insert into user(f_name,L_name,contact,email,password) values(%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(),
                             self.txt_Lname.get(),
                             self.txt_contact.get(),
                             self.txt_email.get(),
                             self.txt_password.get()
                              ) )
                con.commit()
                con.close()
                messagebox.showinfo("success","Registration successful",parent=self.root)
                self.clear()
                self.root.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)
        
            
        
        
root=Tk()
obj=Register(root)
root.mainloop()