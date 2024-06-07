from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        title_lble=Label(self.root,text="FACE RECOGNITION ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lble.place(x=0,y=0,width=1530,height=45)
    #1st img

        top_img=Image.open(r"college_images\03.jpg")
        top_img=top_img.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(top_img)

        first_label=Label(self.root,image=self.photoimg_top)
        first_label.place(x=0,y=55,width=650,height=700)
     

        #2nd image

        next_img=Image.open(r"college_images\01.jpg")
        next_img=next_img.resize((950,700),Image.ANTIALIAS)
        self.photoimg_next=ImageTk.PhotoImage(next_img)

        

        first_label=Label(self.root,image=self.photoimg_next)
        first_label.place(x=650,y=55,width=950,height=700)

         # button 
        b1_1=Button(first_label,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=40,y=300,width=300,height=50)
# ============================ face recognition========================

    def mark_attendence(self,i,r,n,d):
        with open ("charan.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now() 
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")







# ============================ face recognition========================
   
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300))) 

                conn=mysql.connector.connect(host="localhost",database='face_recoginezer',user='root',password='')
                my_cur=conn.cursor()
                query="select student_name from student where student_id='"+str(id)+"'"
                print(query)
                my_cur.execute(query)
                n=my_cur.fetchone()
                print(n)
                n="+".join(n)

                my_cur.execute("select roll_no from student where student_id="+str(id))
                r=my_cur.fetchone()
                r="+".join(r)


                my_cur.execute("select department from student where student_id="+str(id))
                d=my_cur.fetchone()
                d="+".join(d)

                
                my_cur.execute("select student_id from student where student_id="+str(id))
                i=my_cur.fetchone()
                i="+".join(i)





                if confidence>77:
                    cv2.putText(img,f"student id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i, r, n, d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                

                coord=[x,y,w,y]
            
            return coord


        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf) 
            return img


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)


        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)


            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        
        cv2.destroyAllWindows()











if __name__ == "__main__" :
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()