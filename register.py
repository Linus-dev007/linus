from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import os

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Window")
        self.root.geometry("1300x680+70+90")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        # === Background Image ===
        try:
            self.bg = ImageTk.PhotoImage(file="img/bg2.png")
            bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)
        except Exception:
            self.root.config(bg="lightgray")

        # === Left Side Image ===
        try:
            self.left_raw = Image.open("img/side.png")
            self.left_resized = self.left_raw.resize((400, 500)) 
            self.left_img = ImageTk.PhotoImage(self.left_resized)
            
            left_label = Label(self.root, image=self.left_img, bd=0)
            left_label.place(x=80, y=100, width=400, height=500)
        except Exception:
            left_label = Label(self.root, bg="white", bd=0)
            left_label.place(x=80, y=100, width=400, height=500)

        # === Sign In Button (On top of Left Image) ===
        btn_login = Button(self.root, text="Sign In", command=self.login_window, font=("times new roman", 16, "bold"), bg="#3f51b5", fg="white", bd=0, cursor="hand2").place(x=170, y=470, width=220)

        # === Registration Frame ===
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="Register Here", font=("times new roman", 28, "bold","italic"), bg="white", fg="green").place(x=50, y=30)
      
        # ======= Row_01 =======
        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_f_name = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_f_name.place(x=50, y=130, width=250)
        
        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_l_name = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_l_name.place(x=370, y=130, width=250)

        # ======= Row_02 =======
        contact = Label(frame1, text="Contact Number", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # ======= Row_03 =======
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest['values'] = ("Select", "Your First Pet Name?", "Your Birth Place?", "Your Best Friend!")
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)
        
        # ======= Row_04 =======
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_cpassword.place(x=370, y=340, width=250)

        # === Terms & Register Button ===
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I agree with the terms and conditions.", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("robotic",12,"italic")).place(x=50, y=380)
        
        btn_register = Button(frame1, text="Register Now", font=("times new roman", 16, "bold"), bg="green", fg="white", bd=0, cursor="hand2", command=self.register_data).place(x=50, y=420, width=250, height=40)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py") 

    def clear(self):
        self.txt_f_name.delete(0, END)
        self.txt_l_name.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)
        self.var_chk.set(0)

    def register_data(self):
        if self.txt_f_name.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error", "All Fields Are Required!", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same!", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree to Our terms & conditions!", parent=self.root)            
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?", (self.txt_email.get(),))
                row = cur.fetchone()
                
                if row != None:
                    messagebox.showerror("Error", "User Already Exist! Please try with another Email.", parent=self.root)            
                else:
                    cur.execute("insert into employee (f_name, l_name, contact, email, question, answer, password) values(?,?,?,?,?,?,?)",
                                (
                                    self.txt_f_name.get(),
                                    self.txt_l_name.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get()
                                ))   
                    con.commit()
                    con.close()      
                    messagebox.showinfo("Success", "Registration Successful!", parent=self.root)
                    self.clear()
                    self.login_window()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)  

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()