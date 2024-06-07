from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")

        title_lble=Label(self.root,text=" DEVELOPER ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lble.place(x=0,y=0,width=1530,height=45)


        top_img=Image.open(r"college_images\help1.jpg")
        top_img=top_img.resize((1530,750),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(top_img)

        first_label=Label(self.root,image=self.photoimg_top)
        first_label.place(x=0,y=42,width=1530,height=750)
        
        dev_lble=Label(first_label,text=" Email:Charancharry08@gmail.com ",font=("times new roman",35,"bold"),bg="white",fg="yellow")
        dev_lble.place(x=500,y=300)






if __name__ == "__main__" :
    root=Tk()
    obj=Help(root)
    root.mainloop()