from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("student detailes")

        title_lble=Label(self.root,text="TRAIN DATA SET ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lble.place(x=0,y=0,width=1530,height=45)


        top_img=Image.open(r"college_images\02.jpg")
        top_img=top_img.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(top_img)

        first_label=Label(self.root,image=self.photoimg_top)
        first_label.place(x=0,y=55,width=1530,height=325)
        
         # button 
        b1_1=Button(self.root,text="Train Data",cursor="hand2",command=self.train_classifier,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        botton_img=Image.open(r"college_images\04.jpg")
        botton_img=botton_img.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(botton_img)

        first_label=Label(self.root,image=self.photoimg_bottom)
        first_label.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # Gray scale image 
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)



        # train the classifier and save=======================================================

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","training data set compleated !!!!")



       





if __name__ == "__main__" :
    root=Tk()
    obj=Train(root)
    root.mainloop()