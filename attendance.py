from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import cv2
import os
import csv


mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x780+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

######## Variables ########
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

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

        attendance_entry = ttk.Entry(leftInside_frame, textvariable=self.var_atten_id, width=20, font=("coolvetica", 12, "bold"))
        attendance_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


# Name

        name_label = Label(leftInside_frame, text="Name :", font=(
            "coolvetica", 12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        name_entry = ttk.Entry(leftInside_frame,textvariable=self.var_atten_name, width=20, font=("coolvetica", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

# Roll No.

        roll_label = Label(leftInside_frame, text="Roll Number :", font=(
            "coolvetica", 12, "bold"), bg="white")
        roll_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        roll_entry = ttk.Entry(leftInside_frame,textvariable=self.var_atten_roll, width=20, font=("coolvetica", 12, "bold"))
        roll_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

# Department

        dep_label = Label(leftInside_frame, text="Department :", font=(
            "coolvetica", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        dep_entry = ttk.Entry(leftInside_frame,textvariable=self.var_atten_dep, width=20, font=("coolvetica", 12, "bold"))
        dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

# Time

        time_label = Label(leftInside_frame, text="Time :", font=(
            "coolvetica", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        time_entry = ttk.Entry(leftInside_frame,textvariable=self.var_atten_time, width=20, font=("coolvetica", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

# Date

        date_label = Label(leftInside_frame, text="Date :", font=(
            "coolvetica", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        date_entry = ttk.Entry(leftInside_frame,textvariable=self.var_atten_date, width=20, font=("coolvetica", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

# Attendance Status

        attendance_label = Label(leftInside_frame, text="Attendance Status :", font=(
            "coolvetica", 12, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        self.atten_status = ttk.Combobox(leftInside_frame, 
                                         font=("Times New Roman", 10, "bold"),textvariable=self.var_atten_attendance, width=20, state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)

# Button Frame

        btn_frame = Frame(leftInside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=80, y=230, width=540, height=35)

# Import Button
        import_btn = Button(btn_frame, text="Import CSV",command=self.importCSV, width=17, font=(
            "coolvetica", 12, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

# Export Button
        export_btn = Button(btn_frame, text="Export CSV",command=self.exportCSV, width=17, font=(
            "coolvetica", 12, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

# # Update Button
#         update_btn = Button(btn_frame,command=self.update_data, text="Update", width=17, font=(
#             "coolvetica", 12, "bold"), bg="blue", fg="white")
#         update_btn.grid(row=0, column=2)

# Reset Button
        reset_btn = Button(btn_frame,command=self.reset_data, text="Reset", width=17, font=(
            "coolvetica", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=2)



# Right Label Frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance",
                                 font=("coolvetica", 12, "bold"))
        Right_frame.place(x=770, y=5, width=740, height=525)


# Table Frame

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=2, width=725, height=495)


####### Scroll Bar Table #######
   
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time",
                                                                    "date","attendance"),xscrollcommand=scroll_x.set,
                                                                    yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendancce")

        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


######## Fetch Data ########

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
#Import CSV

    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
#Export CSV

    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to " +os.path.basename(fln) +" Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    

#Get Cursor
    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


#Reset
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
