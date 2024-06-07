from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import tkinter
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help



class Facebase_Attendence_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("facebase attendence system")



        img=Image.open(r"D:\facebase_attendence_system\college_images\07.jpg")
        img=img.resize((1530,710),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=1530,height=800)

        title_lble=Label(first_label,text="FACEBASE ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lble.place(x=0,y=0,width=1530,height=45)

    #==================== time ================================

        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(first_label,font=("times new roman",14,"bold"),bg="white",fg="red")
        lbl.place(x=20,y=0,width=110,height=45)
        time()

     #student detail button 
        img2=Image.open(r"D:\facebase_attendence_system\college_images\09.jpeg")
        img2=img2.resize((220,220),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
    
        b1=Button(first_label,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(first_label,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        
       #face detection  button 
        img3=Image.open(r"D:\facebase_attendence_system\college_images\03.jpg")
        img3=img3.resize((220,220),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
    
        b1=Button(first_label,image=self.photoimg3,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(first_label,text="Face Detecor",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #student attendence  button 
        img4=Image.open(r"D:\facebase_attendence_system\college_images\attendence.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
    
        b1=Button(first_label,image=self.photoimg4,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(first_label,text="student attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
       
        #  help  desk  button 
        img5=Image.open(r"D:\facebase_attendence_system\college_images\Help-Desk.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
    
        b1=Button(first_label,image=self.photoimg5,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(first_label,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        # train image button 
        img6=Image.open(r"D:\facebase_attendence_system\college_images\08.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
    
        b1=Button(first_label,image=self.photoimg6,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(first_label,text="Train Image",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)


        #  photos  button 
        img7=Image.open(r"D:\facebase_attendence_system\college_images\06.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
    
        b1=Button(first_label,image=self.photoimg7,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(first_label,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40)

        #  developer  button 
        img8=Image.open(r"D:\facebase_attendence_system\college_images\developer.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
    
        b1=Button(first_label,image=self.photoimg8,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(first_label,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)


        #  exit  button 
        img9=Image.open(r"D:\facebase_attendence_system\college_images\exit.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
    
        b1=Button(first_label,image=self.photoimg9,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(first_label,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)


    def open_img(self):
        os.startfile("data")

    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project ",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return



#================================================ Function Buttons ============================================


    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


#================================================ train Buttons funtion ============================================


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


#================================================ face recognition function Buttons ============================================


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

#================================================ attendance Buttons ============================================


    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

#================================================ developer Buttons ============================================


    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

#================================================ Help Buttons ============================================


    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)









if __name__ == "__main__":
    root=Tk()
    obj=Facebase_Attendence_system(root)
    root.mainloop()