from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *
from datetime import datetime
import sqlite3
from tkinter import messagebox, ttk
import os
import sys

class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        self.root.resizable(False, False)


        # ===== Background Colors =====
        left_lbl = Label(self.root, bg="#08A3D2", bd=0).place(x=0, y=0, relheight=1, width=600)
        right_lbl = Label(self.root, bg="#031F3C", bd=0).place(x=600, y=0, relheight=1, relwidth=1)

        # ===== Login Frame =====
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=50)

        email_lbl = Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        pass_lbl = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=240)
        self.txt_pass_ = Entry(login_frame, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        # Buttons
        btn_reg = Button(login_frame, cursor="hand2", command=self.register_window, text="Register New Account?", font=("times new roman", 14), bg="white", bd=0, fg="#B00857").place(x=250, y=320)
        btn_forget = Button(login_frame, cursor="hand2", command=self.forget_password_window, text="Forget Password?", font=("times new roman", 14), bg="white", bd=0, fg="red").place(x=450, y=320)
        
        # This is the line that was crashing - fixed by aligning the 'login' function below
        btn_login = Button(login_frame, text="Login", command=self.login, font=("times new roman", 20, "bold"), fg="white", bg="#B00857", cursor="hand2").place(x=250, y=380, width=180, height=40)

        # ===== Clock & Date Label =====
        self.lbl = Label(self.root, text="", font=("Book Antiqua", 22, "bold"), fg="white", bg="#081923", bd=0, justify=CENTER)
        self.lbl.place(x=90, y=120, height=450, width=350)
        
        self.working()

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




    def register_window(self):
        self.root.destroy()
        os.system(f"{sys.executable} register.py")

    def reset(self):
        self.txt_email.delete(0, END)
        self.txt_pass_.delete(0, END)

    def login(self):
        if self.txt_email.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and password=?", (self.txt_email.get(), self.txt_pass_.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", f"Welcome: {row[1]}", parent=self.root)
                    self.root.destroy()
                    os.system(f"{sys.executable} database.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def forget_password(self):
        if self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_pass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?", (self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Security answer is incorrect", parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?", (self.txt_new_pass.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Password Reset Successful", parent=self.root2)
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)

    def forget_password_window(self):
        if self.txt_email.get() == "":
            messagebox.showerror("Error", "Please enter Email to reset password", parent=self.root)
        else:
            self.root2 = Toplevel()
            self.root2.title("Forget Password")
            self.root2.geometry("400x440+450+150")
            self.root2.config(bg="white")
            self.root2.focus_force()
            self.root2.grab_set()
            
            t = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)
            
            # Question
            qlbl = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
            self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly', justify=CENTER)
            self.cmb_quest.place(x=50, y=130, width=300)
            self.cmb_quest['values'] = ("Select", "Your First Pet Name?", "Your Birth Place?", "Your Best Friend!")
            self.cmb_quest.current(0)

            albl = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
            self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
            self.txt_answer.place(x=50, y=210, width=300)

            nlbl = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=260)
            self.txt_new_pass = Entry(self.root2, font=("times new roman", 15), bg="lightgray", show="*")
            self.txt_new_pass.place(x=50, y=290, width=300)

            btn_res = Button(self.root2, text="Reset Password", command=self.forget_password, font=("times new roman", 15, "bold"), bg="green", fg="white").place(x=100, y=350, width=200, height=35)

if __name__ == "__main__":
    root = Tk()
    obj = login_window(root)
    root.mainloop()