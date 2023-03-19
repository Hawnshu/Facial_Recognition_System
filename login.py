from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import tkinter
from PIL import Image,ImageTk 
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import mysql.connector


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"Images\login.jpg")
        lbl_bg =Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"Images\LoginIconAppl.png ")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20, "bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #==========Icon Images================
        img2=Image.open(r"Images\LoginIconAppl.png ")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)


        img3=Image.open(r"Images\lock-512.png ")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)

        #LoginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activebackground="red")
        registerbtn.place(x=15,y=350,width=160)

        #forgetpassbtn
        registerbtn=Button(frame,text="Forget password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activebackground="red")
        registerbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all feild required")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin@123":
            messagebox.showinfo("Success","welcome Admin")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Admin@123",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select *from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
            
            ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                     if not open_main:
                          return
            conn.commit()
            conn.close()

            #===================reset password=======================================

    def reset_pass(self):
         if self.combo_security_Q.get()=="Select":
              messagebox.showerror("Error","Select the security Question",parent=self.root2)
         elif self.txt_security.get()=="":
              messagebox.showerror("Error","Please enter the answer",parent=self.root2)
         elif self.txt_newpass.get()=="":
              messagebox.showerror("Error","Please enter new password",parent=self.root2)
         else:
             conn=mysql.connector.connect(host="localhost",user="root",password="Admin@123",database="face_recognizer")
             my_cursor=conn.cursor()
             query=("select * from register where email=%s and securityQ=%s and securityA=%s")
             value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             if row==None:
                  messagebox.showerror("Error", "Please enter correct Answer",parent=self.root2)
             else:
                  query=("update register set password=%s where email=%s")
                  value=(self.txt_newpass.get(),self.txtuser.get())
                  my_cursor.execute(query,value)

                  conn.commit()
                  conn.close()
                  messagebox.showinfo("Info","Your password has been reset ,please login new password",parent=self.root2)
                  self.root2.destroy()
                  

              
         
    


            #=============================forgot password window============================

    def forgot_password_window(self):
         if self.txtuser.get()=="":
              messagebox.showerror("Error","Please Enter the email address to reset password")
         else:
             conn=mysql.connector.connect(host="localhost",user="root",password="Admin@123",database="face_recognizer")
             my_cursor=conn.cursor()
             query=("select * from register where email=%s")
             value=(self.txtuser.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             #print(row)

             if row==None:
                  messagebox.showerror("My Error","please enter the valid user name")
             else:
                  conn.close()
                  self.root2=Toplevel()
                  self.root2.title("Forgot Password")
                  self.root2.geometry("340x450+610+170")

                  l=Label(self.root2,text="Forget password",font=("times new roman",20,"bold"),fg="red",bg="white")
                  l.place(x=0,y=10,relwidth=1)


                  security_Q=Label(self.root2,text="Select Security Questions", font=("times new roman",15,"bold"),bg="white",fg="black")
                  security_Q.place(x=50,y=80)

                  self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                  self.combo_security_Q["values"]=("Select","Your Birth Place", "Your Friend Name","Your Pet Name")
                  self.combo_security_Q.place(x=50,y=110,width=250)    
                  self.combo_security_Q.current(0)





                  security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                  security_A.place(x=50,y=150)

                  self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                  self.txt_security.place(x=50,y=180,width=250)


                  new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                  new_password.place(x=50,y=220)

                  self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                  self.txt_newpass.place(x=50,y=250,width=250)

                  btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),bg="white",fg="green")
                  btn.place(x=100,y=290)







class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #============variables=========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #=============bg image===========
        self.bg=ImageTk.PhotoImage(file=r"Images\hackers2.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #=============left image===========
        self.bg1=ImageTk.PhotoImage(file=r"Images\thought-good-morning-messages-LoveSove.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #===========main Frame==========
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green")
        register_lbl.place(x=20,y=20)

        #================label and entry==========

        #------------------------------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #------------------------------row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #---------------------------------row3

        security_Q=Label(frame,text="Select Security Questions", font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place", "Your Friend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)    
        self.combo_security_Q.current(0)





        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #-----------------------------row4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
                     
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #======================checkbutton====================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms and Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #===============buttons================i
        img=Image.open(r"Images\register-now-button1.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=10,y=420,width=200)


        img1=Image.open(r"Images\loginpng.png")
        img1=img1.resize((200,45),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=300,y=420,width=200)


        #====================Function declaration==============

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All feilds are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Admin@123",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                         self.var_fname.get(),
                                                                                         self.var_lname.get(),
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_securityQ.get(),
                                                                                         self.var_securityA.get(),
                                                                                         self.var_pass.get()
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
         self.root.destroy()


            
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x780+0+0")
        self.root.title("Face Recognition System")

#1st Image

        img=Image.open(r"Images\Stanford.jpg")
        img=img.resize((550,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=516.66,height=130)

#2nd Image

        img1=Image.open(r"Images\facialrecognition.png")
        img1=img1.resize((515,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=515,height=130)

#3rd Image

        img2=Image.open(r"Images\u.jpg")
        img2=img2.resize((550,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

#BG Image

        img3=Image.open(r"Images\wp2551980.jpg")
        img3=img3.resize((1550,680),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1550,height=680)

#Title

        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM", font=("coolvetica",35,"bold"),
                        bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #==================TIME=======================================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        
        lbl = Label(title_lbl,font = ('times new roman',14, 'bold'),background = 'white',foreground = 'blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()



        

#Student Button
        
        img4=Image.open(r"Images\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.Student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.Student_details,cursor="hand2",font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


#Detect Face Button
        
        img5=Image.open(r"Images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)


 #Attendance Button
        
        img6=Image.open(r"Images\report.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)


#Help Button
        
        img7=Image.open(r"Images\help.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)


 #Train Button
        
        img8=Image.open(r"Images\Train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=380,width=220,height=220)

        b5_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b5_1.place(x=200,y=580,width=220,height=40)


#Photos Button
        
        img9=Image.open(r"Images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b6_1.place(x=500,y=580,width=220,height=40)

#Developer Button
        
        img10=Image.open(r"Images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=800,y=380,width=220,height=220)

        b7_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b7_1.place(x=800,y=580,width=220,height=40)

#Exit Button
        
        img11=Image.open(r"Images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b8.place(x=1100,y=380,width=220,height=220)

        b8_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b8_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
            os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
           self.root.destroy()
        else:
             return
#=====================================Functions buttons====================================================
    def Student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

    def open_img(self):
            os.startfile("data")

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)
        
    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)
    
    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)

    def developer_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Developer(self.new_window)

    def help_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Help(self.new_window)












if __name__ == "__main__":
    main()


    