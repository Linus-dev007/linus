from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox, ttk
import os
import time
from math import *
from datetime import datetime
import sqlite3

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1370x700+0+0")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        #======= Logo =======
        img = Image.open("img/logo.png")
        img = img.resize((50, 50)) 
        self.logo_dash = ImageTk.PhotoImage(img) 
        #====== Title ========
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #======= Menu ========
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,relwidth=0.98,height=80)

        #========= BUtton =========
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course)
        btn_course.place(x=20,y=5,width=200,height=40)
        btn_course.bind("<Enter>", lambda e: btn_course.config(bg="#0e6fa3"))
        btn_course.bind("<Leave>", lambda e: btn_course.config(bg="#0b5377"))
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student)
        btn_student.place(x=240,y=5,width=200,height=40)
        btn_student.bind("<Enter>", lambda e: btn_student.config(bg="#0e6fa3"))
        btn_student.bind("<Leave>", lambda e: btn_student.config(bg="#0b5377"))
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result)
        btn_result.place(x=460,y=5,width=200,height=40)
        btn_result.bind("<Enter>", lambda e: btn_result.config(bg="#0e6fa3"))
        btn_result.bind("<Leave>", lambda e: btn_result.config(bg="#0b5377"))
        btn_view=Button(M_Frame,text="View",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report)
        btn_view.place(x=680,y=5,width=200,height=40)
        btn_view.bind("<Enter>", lambda e: btn_view.config(bg="#0e6fa3"))
        btn_view.bind("<Leave>", lambda e: btn_view.config(bg="#0b5377"))
        btn_logout=Button(M_Frame,text="LogOut",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout)
        btn_logout.place(x=900,y=5,width=200,height=40)
        btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="#0e6fa3"))
        btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="#0b5377"))
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_)
        btn_exit.place(x=1120,y=5,width=200,height=40)
        btn_exit.bind("<Enter>", lambda e: btn_exit.config(bg="#0e6fa3"))
        btn_exit.bind("<Leave>", lambda e: btn_exit.config(bg="#0b5377"))
        # ========= Content_Window =========
        #===== Clock & Date Label =====
        self.lbl = Label(self.root, text="", font=("Book Antiqua", 18, "bold"), fg="white", bg="#081923", bd=0, justify=CENTER)
        self.lbl.place(x=60, y=200, height=400, width=300)
        self.working()

        #======== Image & Counter =========
        self.bg_img=Image.open("img/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=170,width=920,height=350)
        
        #========= Update_Detailes ========
        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=540,width=300,height=90)
        
        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=540,width=300,height=90)
        
        self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=540,width=300,height=90)
        self.update_details()

        #===Footer===
        footer=Label(self.root,text="Student Result Management Systeem\nContact Us for any Issue: 01881xxxx",font=("times new roman",13,),bg="#033054",fg="white").pack(side=BOTTOM,fill=X)


    def add_course(self):
     self.new_win=Toplevel(self.root)
     self.new_obj=CourseClass(self.new_win)

    def add_student(self):
     self.new_win=Toplevel(self.root)
     self.new_obj=studentClass(self.new_win)

    def add_result(self):
     self.new_win=Toplevel(self.root)
     self.new_obj=resultClass(self.new_win)
    
    def add_report(self):
     self.new_win=Toplevel(self.root)
     self.new_obj=reportClass(self.new_win)

    def logout(self):
      op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
      if op==True:
        self.root.destroy()
        os.system("python login.py")
      
    def exit_(self):
      op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
      if op==True:
        self.root.destroy()

    def working(self):
        #======= Get Time ========
        h = time.strftime("%H")
        m = time.strftime("%M")
        s = time.strftime("%S")
        
        #======= Date and Day  =======
        day_name = time.strftime("%A")
        date_today = time.strftime("%d %b, %Y")

        #==== Format the Display ========
        combined_text = (
            f"STUDENT\nMANAGEMENT\n\n"
            f"{h}:{m}:{s}\n"
            f"------------------\n"
            f"{day_name}\n"
            f"{date_today}"
        )
        self.lbl.config(text=combined_text)
        self.lbl.after(1000, self.working)

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
           
            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total students\n[{str(len(cr))}]")
           
            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
           

            self.lbl_course.after(200,self.update_details)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()