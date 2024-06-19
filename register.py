from curses.ascii import isdigit
from platform import python_implementation
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk # pip install pillow-loading images
import pymysql #pip install pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration form")
        self.root.geometry("1350x700+0+0")
        
        self.bg=ImageTk.PhotoImage(file="bg//OIP.jpg",master=root)
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
        first_name=self.txt_fname.get()
        lastname=self.txt_Lname.get()
        phone_no=self.txt_contact.get()
        emailid=self.txt_email.get()
        pwd=self.txt_password.get()
        confirm_pwd=self.txt_cpass.get()
        flag=0
        '''
        if self.txt_fname.get()=="" or self.txt_Lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_cpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" or "!" or "@" or "#" or "%" or "&" or "*") in self.txt_fname.get():
            messagebox.showerror("Error","username is invalid",parent=self.root)
        elif("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" or "!" or "@" or "#" or "%" or "&" or "*") in self.txt_Lname.get():
            messagebox.showerror("Error","lastname is invalid",parent=self.root)
        elif len(self.txt_contact.get())!=10 or ("!" or "@" or "#" or "%" or "&" or "*") in self.txt_contact.get():
            messagebox.showerror("Error", "Enter valid phno",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpass.get():
            messagebox.showerror("Error","Passwords must match",parent=self.root)
        elif  len(self.txt_password.get())<6:
            messagebox.showerror("Error","Passwords must contain atleast 6 characters",parent=self.root)  
        elif ("@" or "%" or "#" or "*") not in   self.txt_password.get():
            messagebox.showerror("Error!", "Enter valid password:include atleast one symbol('@','%','*','#')",parent=self.root)
        elif ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9") not in   self.txt_password.get():
            messagebox.showerror("Error!", "Enter valid password:include atleast one number",parent=self.root)
        elif ("a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z") not in   self.txt_password.get():
            messagebox.showerror("Error!", "Enter valid password:include atleast 1 lowercase letter",parent=self.root)
        elif("A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z") not in   self.txt_password.get():
            messagebox.showerror("Error!", "Enter valid password:include atleast 1 uppercase letter",parent=self.root)
        elif ("@" or ".") not in self.txt_email.get():
            messagebox.showerror("Error", "Enter valid mail",parent=self.root)'''
        for i in range(len(first_name)):
            if first_name[i].isdigit():
                messagebox.showerror("Error","enter valid name",parent=self.root)   
                flag=1
                break
        for i in range(len(lastname)):
            if lastname[i].isdigit():
                messagebox.showerror("Error","enter valid name",parent=self.root)   
                flag=-1
                break
        for i in range(len(phone_no)):
            if (phone_no[i]) not in ["1","2","3","4","5","6","7","8","9","0"]:
                messagebox.showerror("Error","enter valid phone number",parent=self.root)  
                flag=2 
                break
            elif len(phone_no)!=10:
                messagebox.showerror("Error","enter valid phone number of length 10",parent=self.root)  
                flag=2 
                break
        if(len(pwd))<6:
            messagebox.showerror("Error","enter password of minimum 6 characters",parent=self.root)  
            flag=3
        if pwd!=confirm_pwd:
            messagebox.showerror("Error","Passwords must match...!!",parent=self.root)  
            flag=5
        if "@gmail.com" not in emailid:
            messagebox.showerror("Error","enter valid mail ",parent=self.root)  
            flag=4
        a=0
        b=0
        c=0
        d=0
        for i in range(len(pwd)):
            if pwd[i]>='A' and pwd[i]<='Z':
                a=a+1 
                print(a)
            if pwd[i]>='a' and pwd[i]<='z':
                b+=1 
        
            if pwd[i] in ['@','%','*','#']:
                c+=1 
                
            if pwd[i] in ["1","2","3","4","5","6","7","8","9","0"]:
                d+=1
            print(pwd)   
        if a==0 or b==0 or c==0 or d==0:
            messagebox.showerror("Error","enter valid password with constraints( atleast 1 lowercase, uppercase, number and a symbol)",parent=self.root) 
            flag=6
        if flag==1 or flag==2 or flag==3 or flag==4 or flag==5 or flag==6 or flag==-1:
            #messagebox.showerror("Error","enter valid details",parent=self.root)  
            print("enter valid details")
        if flag==0:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="abhinaya")
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