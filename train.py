from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x820+0+0")
        self.root.title("Model Training")

        #background image
        img=Image.open(r"C:\Users\srinj\OneDrive\Desktop\face_recog2\image\pg3.jpg")
        img=img.resize((1530,820),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=820)

        #title
        title_lbl=Label(f_lbl, text="Train  Model  on  Existing  Dataset", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        #button to train data lmao
        btn_frame=Frame(f_lbl, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=400,y=400,width=700,height=60)

        btn=Button(btn_frame, text="Train", width=45, font=("times new roman", 20, "bold"), bg="blue", fg="white")
        btn.grid(row=0,column=0)
        btn.bind("<Button-1>", lambda e: self.train_classifier())

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
            
        clf = cv2.face.LBPHFaceRecognizer_create()
        if len(faces) > 0 and len(ids) > 0:
            clf.train(faces, np.array(ids))  # Make sure ids is a NumPy array
            clf.write("classifier.xml")  # Save the trained model
            cv2.destroyAllWindows()  # Close any OpenCV windows
            messagebox.showinfo("Result", "Training Datasets Completed!")
        else:
            messagebox.showerror("Error", "No faces or IDs found. Please check your dataset!")


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()