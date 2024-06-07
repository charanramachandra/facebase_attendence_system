from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("student detailes")


        #=========================variables=======================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        
        img=Image.open(r"D:\facebase_attendence_system\college_images\07.jpg")
        img=img.resize((1530,710),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=1530,height=800)

        title_lble=Label(first_label,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lble.place(x=0,y=0,width=1530,height=45)


        mainframe=Frame(first_label,bd=2)
        mainframe.place(x=5,y=50,width=1530,height=680)


           #left side label frame 

        leftsideframe=LabelFrame(mainframe,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))  
        leftsideframe.place(x=10,y=10,width=750,height=650) 

        img2=Image.open(r"D:\facebase_attendence_system\college_images\students2.jpg")
        img2=img2.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img2)

        first_label=Label(self.root,image=self.photoimg_left)
        first_label.place(x=25,y=90,width=740,height=130)

         # current course 
        current_course_frame=LabelFrame(mainframe,bd=2,relief=RIDGE,text=" Current Course Informantion",font=("times new roman",12,"bold"))  
        current_course_frame.place(x=25,y=200,width=730,height=150)


            #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("select department","computer","IT","civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


            #courses 

        cousre_label=Label(current_course_frame,text="Courses",font=("times new roman",12,"bold"),bg="white")
        cousre_label.grid(row=0,column=2,sticky=W)

        cousre_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        cousre_combo["values"]=("select course","FE","SE","TE","BE")
        cousre_combo.current(0)
        cousre_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #years 


        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)


        #   semester

        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Slect semester","semester-1","semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)


        # class student information  
        class_student_frame=LabelFrame(mainframe,bd=2,relief=RIDGE,text=" class student Informantion",font=("times new roman",12,"bold"))  
        class_student_frame.place(x=25,y=350,width=730,height=300)

             #student ID
        studentID_label=Label(class_student_frame,text="StudentID : ",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
          

          #student name

        student_name_label=Label(class_student_frame,text="Student Name : ",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        # class division 
          
        class_div_label=Label(class_student_frame,text="Class Division : ",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,width=18,font=("times new roman",12,"bold"),state="readonly")
        division_combo["values"]=("select division","A","B","C")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
             

             #ROLL NUMBER

        Roll_no_label=Label(class_student_frame,text="Roll Number : ",font=("times new roman",12,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #gender
        gender_label=Label(class_student_frame,text="Gender : ",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=18,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("MALE","FEMALE","OTHERS")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #DOB
        DOB_label=Label(class_student_frame,text="DOB : ",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #E-mail

        email_label=Label(class_student_frame,text="E-mail : ",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #phone number

        phone_num_label=Label(class_student_frame,text="Phone Number : ",font=("times new roman",12,"bold"),bg="white")
        phone_num_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_num_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_num_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        # Address

        address_label=Label(class_student_frame,text="Address : ",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


     # teacher name

        teachername_label=Label(class_student_frame,text="Teacher name : ",font=("times new roman",12,"bold"),bg="white")
        teachername_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teachername_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teachername_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)





          #radio button 
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="Yes")
        radiobutton1.grid(row=6,column=0)


        self.var_radio2=StringVar()
        radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="No")
        radiobutton2.grid(row=6,column=1)



       # buttons farmes

        btn_farme=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_farme.place(x=0,y=200,width=725,height=40)

        save_btn=Button(btn_farme,text="save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_farme,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_farme,text="delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        recive_btn=Button(btn_farme,text="reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        recive_btn.grid(row=0,column=3)

        btn_farme1=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_farme1.place(x=0,y=235,width=725,height=45)


        take_Photo_sample_btn=Button(btn_farme1,command=self.genetare_dataset,text="Take Photo sample",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_Photo_sample_btn.grid(row=0,column=0)

        update_Photo_sample_btn=Button(btn_farme1,text="update Photo sample",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_Photo_sample_btn.grid(row=0,column=1)
        
        





         #right side label frame 

        rightsideframe=LabelFrame(mainframe,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))  
        rightsideframe.place(x=800,y=20,width=660,height=650) 

        img_right=Image.open(r"D:\facebase_attendence_system\college_images\students2.jpg")
        img_right=img_right.resize((720,120),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)


        first_label=Label(rightsideframe,image=self.photoimg_right)
        first_label.place(x=5,y=0,width=740,height=130)

#   =======================search system========================================

        search_farme=LabelFrame(rightsideframe,bd=2,bg="white",relief=RIDGE,text="search sytem",font=("times new roman",12,"bold"))
        search_farme.place(x=0,y=125,width=655,height=70)

        search_label=Label(search_farme,text="search By : ",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)


        search_combo=ttk.Combobox(search_farme,width=13,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        search_entry=ttk.Entry(search_farme,width=13,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        Search_btn=Button(search_farme,text="Search",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        showALL_btn=Button(search_farme,text="Show All",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showALL_btn.grid(row=0,column=4,padx=5,pady=5,sticky=W)


#   =======================table frame========================================

        table_farme=Frame(rightsideframe,bd=2,bg="white",relief=RIDGE)
        table_farme.place(x=0,y=210,width=655,height=420)

        scroll_x=ttk.Scrollbar(table_farme,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_farme,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_farme,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Depaertment")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="Yaer")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="E_mail")
        self.student_table.heading("phone",text="Phone_No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

          

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

      
#=================================== function declaration ==============================================
   
    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are requied",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",database='face_recoginezer',user='root',password='')
                my_cur=conn.cursor()
                query="INSERT INTO student(department,course,std_year,semister,student_id,student_name,division,roll_no,gender,DOB,email,phone,address,teacher,PhotoSample)  VALUES ('"+self.var_dep.get()+"','"+self.var_course.get()+"','"+self.var_year.get()+"','"+self.var_sem.get()+"','"+self.var_id.get()+"','"+self.var_name.get()+"','"+self.var_div.get()+"','"+self.var_roll.get()+"','"+self.var_gender.get()+"','"+self.var_dob.get()+"','"+self.var_email.get()+"','"+self.var_phone.get()+"','"+self.var_address.get()+"','"+self.var_teacher.get()+"','"+self.var_radio1.get()+"')"
                my_cur.execute(query)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showinfo("Error",f"Due to : {str(es)}",parent=self.root)



#==================================fetch data==========================================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",database='face_recoginezer',user='root',password='')
        my_cur=conn.cursor()
        query="select * from student"
        my_cur.execute(query)
        data=my_cur.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#   ======================================== get cursor==========================

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        contaents=self.student_table.item(cursor_focus)
        data=contaents["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])



# ========================== update data ==========================


    def update_data(self):
        if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are requied",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do u want to update student detailes",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",database='face_recoginezer',user='root',password='')
                    my_cur=conn.cursor()
                    query="update  student set department='"+self.var_dep.get()+"',course='"+self.var_course.get()+"',std_year='"+self.var_year.get()+"',semister='"+self.var_sem.get()+"',student_name='"+self.var_name.get()+"',division='"+self.var_div.get()+"',roll_no='"+self.var_roll.get()+"',gender='"+self.var_gender.get()+"',DOB='"+self.var_dob.get()+"',email='"+self.var_email.get()+"',phone='"+self.var_phone.get()+"',address='"+self.var_address.get()+"',teacher='"+self.var_teacher.get()+"',PhotoSample='"+self.var_radio1.get()+"' where  student_id='"+self.var_id.get()+"' "
                    my_cur.execute(query)
                else:
                    if not update:
                        return
                messagebox.showinfo("success","Student detailes has been updated sucessfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showinfo("Error",f"Due To : {str(es)}",parent=self.root)


# ========================== delete data ==========================


    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showinfo("Error","student ID must be requried",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do u want to delete this student data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",database='face_recoginezer',user='root',password='')
                    my_cur=conn.cursor()
                    query="delete from student where student_id= '"+self.var_id.get()+"'"
                    my_cur.execute(query)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student detials",perent=self.root)
            except Exception as es:
                messagebox.showinfo("Error",f"Due To : {str(es)}",parent=self.root)    


# ========================== delete data ==========================
 

    def reset_data(self):
        self.var_dep.set("select department")
        self.var_course.set("select course")
        self.var_year.set("select year")
        self.var_sem.set("select semester")
        self.var_id.set(" ")
        self.var_name.set("")
        self.var_div.set("select division")
        self.var_roll.set("")
        self.var_gender.set("MALE")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


# ==================================== collect photo sample ===================================


    def genetare_dataset(self):

        if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are requied",parent=self.root) 
        
        else:
            try:

                conn=mysql.connector.connect(host="localhost",database='face_recoginezer',user='root',password='')
                my_cur=conn.cursor()
                query="select * from student"
                my_cur.execute(query)
                myresult=my_cur.fetchall()
                id=0
                for x in myresult:
                    id+=1
                query2="update  student set department='"+self.var_dep.get()+"',course='"+self.var_course.get()+"',std_year='"+self.var_year.get()+"',semister='"+self.var_sem.get()+"',student_name='"+self.var_name.get()+"',division='"+self.var_div.get()+"',roll_no='"+self.var_roll.get()+"',gender='"+self.var_gender.get()+"',DOB='"+self.var_dob.get()+"',email='"+self.var_email.get()+"',phone='"+self.var_phone.get()+"',address='"+self.var_address.get()+"',teacher='"+self.var_teacher.get()+"',PhotoSample='"+self.var_radio1.get()+"' where  student_id='"+self.var_id.get()+"' "
                my_cur.execute(query2)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 


                    #=========================== load predefined data on face frontals from opencv ===========================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #Minimum Neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compleated ! ! !")
            except Exception as es:
                messagebox.showinfo("Error",f"Due To : {str(es)}",parent=self.root)  



if __name__ == "__main__" :
    root=Tk()
    obj=Student(root)
    root.mainloop()