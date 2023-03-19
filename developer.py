from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x780+0+0")
        self.root.title("Face Recognition System")



# Title

        title_lbl = Label(self.root, text="DEVELOPERS", font=("coolvetica", 35, "bold"),
                          bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1550, height=45)
# Top Image

        img_top = Image.open(r"Images\dev.jpg")
        img_top = img_top.resize((1550, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1550, height=720)

 # Frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=500, y=20, width=500, height=500)




#Developer info
        dev_label = Label(main_frame, text="Developers: Shudhanshu Yadav,", font=(
            "coolvetica", 20, "bold"), bg="white", justify=LEFT)
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="Trupti Yadav, Bipasha Reddy", font=(
            "coolvetica", 20, "bold"), bg="white", justify=LEFT)
        dev_label.place(x=0,y=40)

        img2 = Image.open(r"Images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2 = img2.resize((500, 390), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=105, width=500, height=390)










        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
