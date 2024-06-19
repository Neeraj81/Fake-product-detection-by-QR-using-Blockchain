from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from Block import *
from Blockchain import *
from hashlib import sha256
import os
import datetime
import webbrowser
import qrcode
import random
import cv2
import sys
from PIL import ImageTk, Image
import PIL.Image
import imageio
import threading


main = tkinter.Tk()
main.title("Authentication of products-Counterfeit Elimination Using BlockChain")
main.attributes('-fullscreen', True)
#main.geometry('1300x1200')


video_name = "bg\\hii.jpg" #This is your video file path
video = imageio.get_reader(video_name)
def stream(label):
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(PIL.Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image

my_label = tkinter.Label(main)
my_label.pack()
thread = threading.Thread(target=stream, args=(my_label,))
thread.daemon = 1
thread.start()



global filename

blockchain = Blockchain()
if os.path.exists('blockchain_contract.txt'):
    with open('blockchain_contract.txt', 'rb') as fileinput:
        blockchain = pickle.load(fileinput)
    fileinput.close()

def addProduct():
    global filename
    text.delete('1.0', END)
    #filename = askopenfilename(initialdir = "original_barcodes")
    #with open(filename,"rb") as f:
    #    bytes = f.read()
    #f.close()
    pid = tf1.get()
    name = tf2.get()
    user = tf3.get()
    address = tf4.get()
    neer=hex(random.getrandbits(128))
    bytes=neer.encode('utf-8')
    digital_signature = sha256(bytes).hexdigest();
    
    global QRimg
    logo = Image.open('bg\\logo.jpg')
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    QRcode.add_data(digital_signature)
    QRcode.make(fit=True)
    QRimg = QRcode.make_image().convert('RGB')
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    QRimg.save('original_barcodes'+'\\'+str(pid)+'productQR.png')
 
    
    
    
    if len(pid) > 0 and len(name) > 0 and len(user) > 0 and len(address) > 0:
        current_time = datetime.datetime.now() 
        data = pid+"#"+name+"#"+user+"#"+address+"#"+str(current_time)+"#"+digital_signature
        blockchain.add_new_transaction(data)
        hash = blockchain.mine()
        b = blockchain.chain[len(blockchain.chain)-1]
        text.insert(END,"Blockchain Previous Hash        : "+str(b.previous_hash)+"\n")
        text.insert(END,"Block No                        : "+str(b.index)+"\n")
        text.insert(END,"Product Qr-code no              : "+str(digital_signature)+"\n")
        
        blockchain.save_object(blockchain,'blockchain_contract.txt')
        img2= Image.open('original_barcodes'+'\\'+str(pid)+'productQR.png')
        load=img2.resize((200,200))
        render = ImageTk.PhotoImage(load)
        img = Label(main, image=render)
        img.place(x=140, y=500)
        
        tf1.delete(0, 'end')
        tf2.delete(0, 'end')
        tf3.delete(0, 'end')
        tf4.delete(0, 'end')
        messagebox.showinfo("QR Code Generator", "QR Code is saved successfully!")

    else:
        text.insert(END,"Please enter all details")




def searchProduct():
    text.delete('1.0', END)
    pid = tf1.get()

    flag = True
    if len(pid) > 0:
        for i in range(len(blockchain.chain)):
            if i > 0:
                b = blockchain.chain[i]
                data = b.transactions[0]
                arr = data.split("#")
                if arr[0] == pid:
                    global QRimg
                    logo = Image.open('bg\\logo.jpg')
                    basewidth = 100
                    wpercent = (basewidth/float(logo.size[0]))
                    hsize = int((float(logo.size[1])*float(wpercent)))
                    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
                    #logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
                    QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
                    QRcode.add_data(arr[5])
                    QRcode.make(fit=True)
                    QRimg = QRcode.make_image().convert('RGB')
                    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
                    QRimg.paste(logo, pos)
                    QRimg.save('original_barcodes'+'\\'+str(pid)+'productQR.png')
                    output = ''
                    text.insert(END,"Product Details extracted from Blockchain using Product ID : "+pid+"\n\n")
                    text.insert(END,"Product ID                                 : "+arr[0]+"\n")
                    text.insert(END,"Product Name                               : "+arr[1]+"\n")
                    text.insert(END,"Company/User Details                       : "+arr[2]+"\n")
                    text.insert(END,"Address Details                            : "+arr[3]+"\n")
					#text.insert(END,"hash code                                  : "+arr[4]+"\n")
                    text.insert(END,"Product Registered Date & Time             : "+arr[4]+"\n")
                    text.insert(END,"Product Qr Code                            : "+arr[5]+"\n")

      
                    output='<html><body><table border=1>'
                    output += '<tr><th>Block No</th><th>Product ID</th><th>Product Name</th><th>Company/User Details</th><th>Address Details</th><th>Scan Date & Time</th><th>Product Qr code</th></tr>'
                    output += '<tr><td>' + str(i) + '</td><td>' + arr[0] + '</td><td>' + arr[1] + '</td><td>' + arr[2] + '</td><td>' + arr[3] + '</td><td>' + arr[4] + '</td><td>' + arr[5] + '</td></tr>'
                    f = open("output.html", "w")
                    f.write(output)
                    f.close()
                    #webbrowser.open("output.html",new=1)
                    flag = False
                    img2= Image.open('original_barcodes'+'\\'+str(pid)+'productQR.png')
                    load=img2.resize((200,200))
                    render = ImageTk.PhotoImage(load)
                    img = Label(main, image=render)
                    img.place(x=140, y=500)
                    #messagebox.showinfo("", "Retrieve product QR-code!")


                    break
    if flag:
        text.insert(END,"Given product id does not exists")
        
    
    









    

main.wm_attributes('-transparentcolor', '#ab23ff')
font = ('times', 30, 'bold')
title = Label(main, text='Authentication of products-Counterfeit Elimination Using BlockChain')
title.config(bg="green",fg='black')  
title.config(font=font)           
title.config(height=3, width=50)       
title.place(x=170,y=5)

font1 = ('times', 13, 'bold')

l1 = Label(main, text='Product ID :')
l1.config(font=font1)
l1.place(x=280,y=200)

tf1 = Entry(main,width=80)
tf1.config(font=font1)
tf1.place(x=470,y=200)

l2 = Label(main, text='Product Name :')
l2.config(font=font1)
l2.place(x=280,y=250)

tf2 = Entry(main,width=80)
tf2.config(font=font1)
tf2.place(x=470,y=250)

l3 = Label(main, text='Company/User Details :')
l3.config(font=font1)
l3.place(x=280,y=300)

tf3 = Entry(main,width=80)
tf3.config(font=font1)
tf3.place(x=470,y=300)

l4 = Label(main, text='Address Details :')
l4.config(font=font1)
l4.place(x=280,y=350)

tf4 = Entry(main,width=80)
tf4.config(font=font1)
tf4.place(x=470,y=350)

def run13():
    main.destroy()
    import Main

    #os.system('AdmMain.py',)
    

scanButton = Button(main, text="Home Page",bg="dark orange", command=run13)
scanButton.place(x=1400,y=200)
scanButton.config(font=font1)

saveButton = Button(main, text="Save Product with Blockchain Entry", command=addProduct)
saveButton.place(x=420,y=400)
saveButton.config(font=font1)

searchButton = Button(main, text="Retrieve Product Data", command=searchProduct)
searchButton.place(x=850,y=400)
searchButton.config(font=font1)


font1 = ('times', 13, 'bold')
text=Text(main,height=15,width=100)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=400,y=450)
text.config(font=font1)

main.config(bg='cornflower blue')
main.mainloop()
