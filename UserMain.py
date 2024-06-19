from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog #get the val of user
import tkinter
from tkinter import filedialog #help in dil handling...
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
import PIL.Image
from PIL import ImageTk, Image
import PIL.Image
import imageio
import threading
import qrtools #generate qr
from PIL import Image
from pyzbar.pyzbar import decode
import pyzbar.pyzbar as pyzbar #decode qr
#from pyzbar.pyzbar import ZBarSymbol




main = Tk()
main.title("Authentication of products-Counterfeit Elimination Using BlockChain")
main.attributes('-fullscreen', True)
#main.geometry('1300x1200')



video_name = "bg\\hii.jpg" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
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

def authenticateProduct():
    text.delete('1.0', END)
    filename_ = askopenfilename(initialdir = "original_barcodes")
    
    #qr=qrtools.QR()
    #qr.decode(filename_)
    image = cv2.imread(filename_)
    decodedObjects = pyzbar.decode(image)
    for obj in decodedObjects:
        digital_signature_=obj.data
        digital_signature=digital_signature_.decode("utf-8")
        
    
    #digital_signature=digital_signature_
    #img=cv2.imread(filename)
    #det=cv2.QRCodeDetector()
    #digital_signature, pts, st_code=det.detectAndDecode(img)
    flag = True
    for i in range(len(blockchain.chain)):
        if i > 0:
            b = blockchain.chain[i]
            data = b.transactions[0]
            arr = data.split("#")
            if arr[5] == digital_signature:
                output = ''
                text.insert(END,"Uploaded Product Barcode Authentication Successfull\n")
                text.insert(END,"Details extracted from Blockchain after Validation\n\n")
                text.insert(END,"Product ID                                 : "+arr[0]+"\n")
                text.insert(END,"Product Name                               : "+arr[1]+"\n")
                text.insert(END,"Company/User Details                       : "+arr[2]+"\n")
                text.insert(END,"Address Details                            : "+arr[3]+"\n")
                text.insert(END,"Product registered Date & Time             : "+arr[4]+"\n")
                text.insert(END,"Product QR-Code                            : "+str(digital_signature)+"\n")

                output='<html><body><table border=1>'
                output += '<tr><th>Block No</th><th>Product ID</th><th>Product Name</th><th>Company/User Details</th><th>Address Details</th><th>Scan Date & Time</th><th>Product QR-Code No</th></tr>'
                output+='<tr><td>'+str(i)+'</td><td>'+arr[0]+'</td><td>'+arr[1]+'</td><td>'+arr[2]+'</td><td>'+arr[3]+'</td><td>'+arr[4]+'</td><td>'+str(digital_signature)+'</td></tr>'
                f = open("output.html", "w")
                f.write(output)
                f.close()
                webbrowser.open("output.html",new=1)
                flag = False
                break
    if flag:
        o1=''
        text.insert(END,str(digital_signature)+",  this hash is not present in the blockchain \n")
        text.insert(END,"Uploaded Product Barcode Authentication Failed: FAKE")
        o1='<html><body><link rel="stylesheet" href="styles.css">'
        o1+='<h1>FAKE PRODUCT!!</h1>'
        o1+='</body></html>'
        f = open("o1.html", "w")
        f.write(o1)
        f.close()
        webbrowser.open("o1.html",new=1)




def authenticateProductWeb():
    text.delete('1.0', END)
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, frame = cap.read()
        data, bbox, _ = detector.detectAndDecode(frame)
        digital_signature=data
        if digital_signature:
	        break
        cv2.imshow("QR-Code scanner", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    flag = True
    for i in range(len(blockchain.chain)):
        if i > 0:
            b = blockchain.chain[i]
            data = b.transactions[0]
            arr = data.split("#")
            #global digital_signature
            if arr[5] == digital_signature:
                output = ''
                text.insert(END,"Uploaded Product Barcode Authentication Successfull\n")
                text.insert(END,"Details extracted from Blockchain after Validation\n\n")
                text.insert(END,"Product ID                   : "+arr[0]+"\n")
                text.insert(END,"Product Name                 : "+arr[1]+"\n")
                text.insert(END,"Company/User Details         : "+arr[2]+"\n")
                text.insert(END,"Address Details              : "+arr[3]+"\n")
                text.insert(END,"Scan Date & Time             : "+arr[4]+"\n")
                #text.insert(END,"Product Qr code              : "+str(bytes) +"\n")
                text.insert(END,"Product QR-Code              : "+str(digital_signature)+"\n")

                output='<html><body><table border=1>'
                output += '<tr><th>Block No</th><th>Product ID</th><th>Product Name</th><th>Company/User Details</th><th>Address Details</th><th>Scan Date & Time</th><th>Product digital Signature</th></tr>'
                output+='<tr><td>'+str(i)+'</td><td>'+arr[0]+'</td><td>'+arr[1]+'</td><td>'+arr[2]+'</td><td>'+arr[3]+'</td><td>'+arr[4]+'</td><td>'+str(digital_signature)+'</td></tr>'
                f = open("output.html", "w")
                f.write(output)
                f.close()
                webbrowser.open("output.html",new=1)
                flag = False
                break
    if flag:
        o1=''
        text.insert(END,str(digital_signature)+",  this hash is not present in the blockchain \n")
        text.insert(END,"Uploaded Product Barcode Authentication Failed fake product")
        text.insert(END,"Uploaded Product Barcode Authentication Failed: FAKE")
        o1='<html><body><link rel="stylesheet" href="styles.css">'
        o1+='<h1>FAKE PRODUCT!!</h1>'
        o1+='</body></html>'
        f = open("o1.html", "w")
        f.write(o1)
        f.close()
        webbrowser.open("o1.html",new=1)
        
        
 
    
    

main.wm_attributes('-transparentcolor', '#ab23ff')
font = ('times', 30, 'bold')
title = Label(main, text='Authentication of products-Counterfeit Elimination Using BlockChain')
title.config(bg='green',fg='white')  
title.config(font=font)           
title.config(height=3, width=50)       
title.place(x=170,y=5)

font1 = ('times', 13, 'bold')


def run12():
    main.destroy()
    import Main
    #os.system('AdminMain.py',)
    

scanButton = Button(main, text="Home Page",bg="white", command=run12)
scanButton.place(x=1400,y=200)
scanButton.config(font=font1)

scanButton = Button(main, text="Authenticate Scan", command=authenticateProduct)
scanButton.place(x=420,y=300)
scanButton.config(font=font1)


scanButton = Button(main, text="Authenticate web Scan", command=authenticateProductWeb)
scanButton.place(x=850,y=300)
scanButton.config(font=font1)

font1 = ('times', 13, 'bold')
text=Text(main,height=15,width=100)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=300,y=450)
text.config(font=font1)


main.config(bg='cornflower blue')
main.mainloop()
