from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x820+0+0")
        self.root.title("Face Recognitioni")

        #background image
        img=Image.open(r"C:\Users\srinj\OneDrive\Desktop\face_recog2\image\pg4.jpg")
        img=img.resize((1530,820),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=820)

        #title
        title_lbl=Label(f_lbl, text="Face  Recognition  Application", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        #button to recognise face
        btn_frame=Frame(f_lbl, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=400,y=700,width=700,height=60)

        btn=Button(btn_frame, text="Recognize Face", width=45, font=("times new roman", 20, "bold"), bg="blue", fg="white")
        btn.grid(row=0,column=0)
        btn.bind("<Button-1>", lambda e: self.face_recog())

    # #Ffunction to mark attendance
    # def mark_attendance(self, n, r, s):
    #     with open("attendance.csv","r+",newline="\n") as f:
    #         myDataList=f.readlines()
    #         name_list=[]
    #         for line in myDataList:
    #             entry=line.split((","))
    #             name_list.append(entry[0])
    #         d1=now.strftime("%d/%m/%Y")
    #         if ((n not in name_list) and (r not in name_list) and (s not in name_list) and (d1 not in name_list)):
    #             now=datetime.now()
    #             #d1=now.strftime("%d/%m/%Y")
    #             dstring=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{n},{r},{s},{dstring},{d1},Present")

    def face_recog(self):

        #Ffunction to mark attendance
        def mark_attendance(self, n, r, s):
            with open("attendance.csv","r+",newline="\n") as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split((","))
                    name_list.append(entry[0])
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                if ((n not in name_list) and (r not in name_list) and (s not in name_list) and (d1 not in name_list)):
                    #now=datetime.now()
                    #d1=now.strftime("%d/%m/%Y")
                    dstring=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{n},{r},{s},{dstring},{d1},Present")

        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", username="root", password="Sr1nj0yee!", database="schema")
                my_cursor=conn.cursor()

                # my_cursor.execute("select 'Name' from student_table where 'Employee ID'=%s",(id,))
                # i=my_cursor.fetchone()
                # #i="+".join(i)
                # i = ""+str(i)
                my_cursor.execute("SELECT Name FROM student_table WHERE `Employee ID`=%s", (id,))
                # use backticks `` fr sql queries not quotes '' as quotes make it a string literal
                i = my_cursor.fetchone()

                if i:
                    # Convert the tuple to a string
                    i = "+".join(str(x) for x in i)

                my_cursor.execute("SELECT Department FROM student_table WHERE `Employee ID`=%s",(id,))
                r=my_cursor.fetchone()
                #r="+".join(r)
                if r:
                    r = "+".join(str(x) for x in r)

                my_cursor.execute("SELECT Subsidiary FROM student_table WHERE `Employee ID`=%s",(id,))
                s=my_cursor.fetchone()
                if s:
                    s = "+".join(str(x) for x in s)

                if confidence>77:
                    cv2.putText(img,f"Name:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Subsidiary:{s}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    mark_attendance(self, i, r, s)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,h]

            return  coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret, img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1)==13:
                break
            #click enter key to exit
            
        video_cap.release()
        cv2.destroyAllWindows()
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()