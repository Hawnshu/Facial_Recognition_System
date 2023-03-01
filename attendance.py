from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x780+0+0")
        self.root.title("Face Recognition System")


# 1st Image

        img = Image.open(r"Images\smart-attendance.jpg")
        img = img.resize((800, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

# 2nd Image

        img1 = Image.open(r"Images\iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

# BG Image

        img3 = Image.open(r"Images\wp2551980.jpg")
        img3 = img3.resize((1550, 680), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1550, height=680)

# Title

        title_lbl = Label(bg_img, text="Attendance", font=("coolvetica", 35, "bold"),
                          bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1550, height=45)

# Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1525, height=537)

# Left Label Frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("coolvetica", 12, "bold"))
        Left_frame.place(x=12, y=5, width=740, height=525)
        
        img_left = Image.open(r"Images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((730, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=3, y=0, width=730, height=130)


# Left Inside Frame

        leftInside_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE)
        leftInside_frame.place(x=3, y=135, width=730, height=365)


#Labels And Entry

# Attendance ID

        attendance_label = Label(leftInside_frame, text="Attendance ID :", font=(
            "coolvetica", 12, "bold"), bg="white")
        attendance_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        attendance_entry = ttk.Entry(leftInside_frame, width=20, font=("coolvetica", 12, "bold"))
        attendance_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


# Name

        name_label = Label(leftInside_frame, text="Name :", font=(
            "coolvetica", 12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        name_entry = ttk.Entry(leftInside_frame, width=20, font=("coolvetica", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

# Roll No.

        roll_label = Label(leftInside_frame, text="Roll Number :", font=(
            "coolvetica", 12, "bold"), bg="white")
        roll_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        roll_entry = ttk.Entry(leftInside_frame, width=20, font=("coolvetica", 12, "bold"))
        roll_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

# Department

        dep_label = Label(leftInside_frame, text="Department :", font=(
            "coolvetica", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        dep_entry = ttk.Entry(leftInside_frame, width=20, font=("coolvetica", 12, "bold"))
        dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

# Time

        time_label = Label(leftInside_frame, text="Time :", font=(
            "coolvetica", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        time_entry = ttk.Entry(leftInside_frame, width=20, font=("coolvetica", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

# Date

        date_label = Label(leftInside_frame, text="Date :", font=(
            "coolvetica", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        date_entry = ttk.Entry(leftInside_frame, width=20, font=("coolvetica", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

# Attendance Status

        attendance_label = Label(leftInside_frame, text="Attendance Status :", font=(
            "coolvetica", 12, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        self.atten_status = ttk.Combobox(leftInside_frame, 
                                         font=("Times New Roman", 10, "bold"), width=20, state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)




# Right Label Frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance",
                                 font=("coolvetica", 12, "bold"))
        Right_frame.place(x=770, y=5, width=740, height=525)

        img_right = Image.open(r"Images\gettyimages-1022573162.jpg")
        img_right = img_right.resize((730, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=3, y=0, width=730, height=130)








        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
