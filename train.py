from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x780+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")


# Title

        title_lbl = Label(self.root, text="Train Data Set", font=("coolvetica", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1550, height=45)
# Top Image

        img_top = Image.open(r"Images\facialrecognition.png")
        img_top = img_top.resize((1550, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1550, height=325)
        
# Button
        
        b1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("coolvetica",30,"bold"),
                        bg="magenta",fg="white")
        b1.place(x=0,y=380,width=1550,height=60)

# Bottom Image

        img_bottom = Image.open(r"Images\opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((1550, 360), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1550, height=360)


    def train_classifier(self):
        data_dir=("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #Gray Scaling
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('-')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)


# ==========Train the Classifier==========
     
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")




if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()