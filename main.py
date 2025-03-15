from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from Face_Recognition import Face_Recognition
from attendance import Attendance
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x820+0+0")
        self.root.title("Face Recognition System")

        #background image
        img=Image.open(r"C:\Users\srinj\OneDrive\Desktop\face_recog2\image\pg1.jpg")
        img=img.resize((1530,820),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=820)

        #title
        title_lbl=Label(f_lbl, text="Face Recognition Attendance System Software", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0,y=30,width=1530,height=40)

        #employee button
        img1=Image.open(r"C:\Users\srinj\OneDrive\Desktop\face_recog2\image\but1.png")
        img1=img1.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(f_lbl, image=self.photoimg1, cursor="hand2")
        b1.place(x=300,y=150,width=220,height=220)
        b1.bind("<Button-1>", lambda e: self.student_details())
        
        b1_1=Label(f_lbl, text="Employee Details", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=300,y=350,width=224,height=40)
        b1_1.bind("<Button-1>", lambda e: self.student_details())

        #face recognition button
        img2=Image.open(r"C:\Users\srinj\OneDrive\Desktop\face_recog2\image\but2.png")
        img2=img2.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(f_lbl, image=self.photoimg2, cursor="hand2")
        b2.place(x=660,y=150,width=220,height=220)
        b2.bind("<Button-1>", lambda e: self.face_details())
        
        b2_1=Label(f_lbl, text="Face Recognition", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b2_1.place(x=658,y=350,width=224,height=40)
        b2_1.bind("<Button-1>", lambda e: self.face_details())

        #attendance button
        img3=Image.open(r"C:\Users\srinj\OneDrive\Desktop\face_recog2\image\but3.png")
        img3=img3.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(f_lbl, image=self.photoimg3, cursor="hand2")
        b3.place(x=1020,y=150,width=220,height=220)
        b3.bind("<Button-1>", lambda e: self.attendance_details())
        
        b3_1=Label(f_lbl, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b3_1.place(x=1020,y=350,width=224,height=40)
        b3_1.bind("<Button-1>", lambda e: self.attendance_details())

        #train data button
        img4=Image.open(r"C:\Users\srinj\OneDrive\Desktop\face_recog2\image\but4.png")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(f_lbl, image=self.photoimg4, cursor="hand2")
        b4.place(x=480,y=450,width=220,height=220)
        b4.bind("<Button-1>", lambda e: self.train_details())
        
        b4_1=Label(f_lbl, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b4_1.place(x=480,y=650,width=224,height=40)
        b4_1.bind("<Button-1>", lambda e: self.train_details())

        #photos button
        img5=Image.open(r"C:\Users\srinj\OneDrive\Desktop\face_recog2\image\but5.png")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b5=Button(f_lbl, image=self.photoimg5, cursor="hand2")
        b5.place(x=840,y=450,width=220,height=220)
        b5.bind("<Button-1>", lambda e: self.open_img())
        
        b5_1=Label(f_lbl, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b5_1.place(x=840,y=650,width=224,height=40)
        b5_1.bind("<Button-1>", lambda e: self.open_img())

    def open_img(self):
        os.startfile("data")

    #function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()