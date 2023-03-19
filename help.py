from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x780+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")



# Title

        title_lbl = Label(self.root, text="HELP", font=("coolvetica", 35, "bold"),
                          bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1550, height=45)
# Top Image

        img_top = Image.open(r"Images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1550, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1550, height=720)

        dev_label = Label(f_lbl, text="Email:yadavtrupti296@gmail.com", font=(
            "coolvetica", 20, "bold"), bg="white", justify=LEFT)
        dev_label.place(x=550,y=220)





if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()