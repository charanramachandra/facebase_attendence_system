from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("developer window")

        title_lble=Label(self.root,text=" DEVELOPER ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lble.place(x=0,y=0,width=1530,height=45)


        top_img=Image.open(r"college_images\02.jpg")
        top_img=top_img.resize((1530,750),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(top_img)

        first_label=Label(self.root,image=self.photoimg_top)
        first_label.place(x=0,y=42,width=1530,height=750)


      # main frame 


        mainframe=Frame(first_label,bd=2)
        mainframe.place(x=1000,y=0,width=500,height=600)

        dev_img=Image.open(r"college_images\charan.jpg")
        dev_img=dev_img.resize((200,200),Image.ANTIALIAS)
        self.photoimg_dev=ImageTk.PhotoImage(dev_img)

        first_label=Label(mainframe,image=self.photoimg_dev)
        first_label.place(x=300,y=0,width=200,height=200)

         #Develpoer  info
        dep_label=Label(mainframe,text="Hello my name is,Charan",font=("times new roman",18,"bold"),bg="white")
        dep_label.place(x=0,y=5)

        dep_label=Label(mainframe,text="I am Full Stack Developer",font=("times new roman",18,"bold"),bg="white")
        dep_label.place(x=0,y=40)

        
        sub_img=Image.open(r"college_images\full_stack.png")
        sub_img=sub_img.resize((495,390),Image.ANTIALIAS)
        self.photoimg_sub=ImageTk.PhotoImage(sub_img)

        first_label=Label(mainframe,image=self.photoimg_sub)
        first_label.place(x=0,y=205,width=495,height=390)

















if __name__ == "__main__" :
    root=Tk()
    obj=Developer(root)
    root.mainloop()