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
from PIL import Image, ImageTk
import PIL.Image
import imageio
import threading


main = Tk()
main.attributes('-fullscreen', True)
#main.geometry('1300x1200')

main.title("Authentication of products-Counterfeit Elimination Using BlockChain")


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



def run1():
    main.after(10000, lambda: main.destroy())
    import AdminMain
    #os.system('AdminMain.py',)

def run2():
    main.destroy()
    import UserMain
    #os.system('UserMain.py')
def run3():
    main.destroy()
    import distributed
    
def quiti():
    main.destroy()
    
    
main.wm_attributes('-transparentcolor', '#ab23ff')
font = ('times', 30, 'bold')
title = Label(main, text='Authentication of products-Counterfeit Elimination Using BlockChain')
title.config(bg='green',fg='white')  
title.config(font=font)           
title.config(height=3, width=50)       
title.place(x=170,y=5)

font1 = ('times', 22, 'bold')

saveButton = tkinter.Button(main, text="Manufacturer login",bg="green",fg="white", command=run1)

saveButton.place(x=530,y=500)
saveButton.config(font=font1)

searchButton = tkinter.Button(main, text="User Page",bg="green", fg="white",command=run2)
searchButton.place(x=900,y=500)
searchButton.config(font=font1)
'''
searchButton1 = tkinter.Button(main, text="Distributed Systems",bg="green", command=run3)
searchButton1.place(x=690,y=650)
searchButton1.config(font=font1)
'''
searchButton = tkinter.Button(main, text="Close", command=quiti)
searchButton.place(x=1400,y=20)
searchButton.config(font=font1)



main.config(bg='cornflower blue')
main.mainloop()
