from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("student detailes")

        
        #=========================== variables ============================
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()
        


            #first image
        img=Image.open(r"college_images\07.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=800,height=200)


        
            #second image
        img2=Image.open(r"college_images\07.jpg")
        img2=img2.resize((800,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_label=Label(self.root,image=self.photoimg2)
        first_label.place(x=800,y=0,width=800,height=200)



        # bg img
        bg_img=Image.open(r"D:\facebase_attendence_system\college_images\07.jpg")
        bg_img=bg_img.resize((1530,710),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        first_label=Label(self.root,image=self.bg_photoimg)
        first_label.place(x=0,y=200,width=1530,height=710)

        title_lble=Label(first_label,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lble.place(x=0,y=0,width=1530,height=45)

        mainframe=Frame(first_label,bd=2)
        mainframe.place(x=5,y=50,width=1515,height=530)

        #left side label frame 

        leftsideframe=LabelFrame(mainframe,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))  
        leftsideframe.place(x=10,y=10,width=750,height=500) 

        img_left=Image.open(r"D:\facebase_attendence_system\college_images\students2.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        first_label=Label(self.root,image=self.photoimg_left)
        first_label.place(x=25,y=290,width=740,height=130)

        left_inside_frame=Frame(leftsideframe,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=140,width=740,height=300)


        # labeland entry 

         #attendance  ID
        attendanceID_label=Label(left_inside_frame,text="ATTENDANCE ID : ",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_id,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         #  roll
        roll_label=Label(left_inside_frame,text="ROLL : ",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #  name
        name_label=Label(left_inside_frame,text="NAME : ",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # department

        department_label=Label(left_inside_frame,text="Department : ",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        department_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_dep,font=("times new roman",12,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        # time

        time_label=Label(left_inside_frame,text="Time : ",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #date


        date_label=Label(left_inside_frame,text="Date : ",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        # attendance  

        attendance_label=Label(left_inside_frame,text="Attendance Status : ",font=("times new roman",12,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        
        self.attendance_combo=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_attend_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.attendance_combo["values"]=("status","Present","Absent")
        self.attendance_combo.current(0)
        self.attendance_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        # buttons 

        
        btn_farme=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_farme.place(x=0,y=250,width=725,height=40)

        save_btn=Button(btn_farme,text=" Import CSV",command=self.importCsv,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_farme,text=" Export CSV",command=self.exportCsv,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_farme,text= " Update",command=self.action,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        recive_btn=Button(btn_farme,text=" Reset",width=19,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        recive_btn.grid(row=0,column=3)

 


        #right side label frame 

        rightsideframe=LabelFrame(mainframe,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))  
        rightsideframe.place(x=800,y=10,width=660,height=500) 

        table_farme=Frame(rightsideframe,bd=2,relief=RIDGE,bg="white")
        table_farme.place(x=5,y=5,width=650,height=450)

       # ==================================== scroll  bar table =====================

        scroll_x=ttk.Scrollbar(table_farme,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_farme,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_farme,column=("ID","Roll.no","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("ID",text="Attendance ID")
        self.AttendanceReportTable.heading("Roll.no",text="Roll")
        self.AttendanceReportTable.heading("Name",text="NAME")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="TIME")
        self.AttendanceReportTable.heading("Date",text="DATE")
        self.AttendanceReportTable.heading("Attendance",text="attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("ID",width=100)
        self.AttendanceReportTable.column("Roll.no",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)




        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


# =============================== fetch data ====================================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)



# import csv 
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

# export csv 
    def exportCsv(self):
        try :
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile :
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showinfo("Error",f"Due to : {str(es)}",parent=self.root)
# update


    def action(self):
        ids=self.var_attend_id.get()
        roll=self.var_attend_roll.get()
        name=self.var_attend_name.get()
        dep=self.var_attend_dep.get()
        time=self.var_attend_time.get()
        date=self.var_attend_date.get()
        attendn=self.var_attend_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer= csv.DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "ID":ids,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])


    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")







if __name__ == "__main__" :
    root=Tk()
    obj=Attendance(root)
    root.mainloop()