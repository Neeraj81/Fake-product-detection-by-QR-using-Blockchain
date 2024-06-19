from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk # pip install pillow
import pymysql #pip install pymysql

class Login:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Login form")
        self.root.geometry("1250x700+0+0")
        
        self.bg=ImageTk.PhotoImage(file="bg//OIP.jpg",master=root)
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        frame1=Frame(self.root,bg="white")
        frame1.place(x=350,y=100,width=600,height=500)
        
        title=Label(frame1,text="LOGIN",font=("times new roman",30,"bold"),bg="white",fg="green").place(x=50,y=40)
        
        email=Label(frame1,text="EMAIL",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=50,y=140)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=50,y=180,width=300)
        
        password=Label(frame1,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.txt_password=Entry(frame1,font=("times new roman",15),show="*",bg="lightgray")
        self.txt_password.place(x=50,y=280,width=300)
        
        btn_reg=Button(frame1,text="REGISTER NEW ACCOUNT?",command=self.register_window,font=("times new roman",10),bg="white",bd=0,fg="red").place(x=50,y=320)
          
        btn_login=Button(frame1,text="LOGIN",command=self.login,font=("times new roman",15,"bold"),bg="green",fg="white").place(x=50,y=350)
        
    def register_window(self):
        import register
        
        
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="abhinaya")
                cur=con.cursor()
                cur.execute("select *from user where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","INVALID USERNAME AND PASSWORD",parent=self.root)
                    
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import AdminMain
                con.close()
            except Exception as em:
                messagebox.showerror("Error",f"Error due to :{str(em)}",parent=self.root)
        
        
      
root=Tk()
obj=Login(root)
root.mainloop()
       
