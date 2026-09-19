from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x560+80+240")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False, False)

        #======= title =======
        title=Label(self.root, text="Add Students Results",font=("times new roman",22,"italic","bold"),bg="#ffA500",fg="#EFE3E3").place(x=10,y=15,width=1180,height=50)
        
        #========= widgets =============
        #========= Variables =============
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()

        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",15,"bold"),bg='white').place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg='white').place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg='white').place(x=50,y=220)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg='white').place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",15,"bold"),bg='white').place(x=50,y=340)
        
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text="Search",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=490,y=96,width=120,height=35)
       
        lbl_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",16,"italic"),bg='lightyellow',state='readonly').place(x=280,y=160,width=330)
        lbl_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",16,"italic"),bg='lightyellow',state='readonly').place(x=280,y=220,width=330)
        lbl_marks=Entry(self.root,textvariable=self.var_marks,font=("goudy old style",16,"italic"),bg='lightyellow').place(x=280,y=280,width=330)
        lbl_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",16,"italic"),bg='lightyellow').place(x=280,y=340,width=330)


        #======== Button =========

        self.btn_add=Button(self.root,text="Submit",font=("times new romoan",15,"italic"),bg="#27a83f",activebackground="#27a83f",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=290,y=420,width=140,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("times new roman",15,"italic"),bg="#2196f3",activebackground="#2196f3",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=440,y=420,width=140,height=40)


    #======== Image =========
        self.bg_img=Image.open("img/result.png")
        self.bg_img=self.bg_img.resize((520,320),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=630,y=100,height=360) #width=920,height=350 (For adjust widthxhight)
       

    #=================================
    def fetch_roll(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])            
            #print(v)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    #=====================================
    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])            
            #print(v)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    #========================================
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    #============== add ==================
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search student record.",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Result already present",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    cur.execute("insert into result (roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Sucessfully",parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
       
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")   


if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()