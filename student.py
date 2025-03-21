from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x820+0+0")
        self.root.title("Employee")

        #variables
        self.var_dept=StringVar()
        self.var_sub=StringVar()
        self.var_year=StringVar()
        self.var_fin_q=StringVar()
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_gen=StringVar()
        self.var_add=StringVar()
        self.var_ph=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()

        #background image
        img=Image.open(r"C:\Users\srinj\OneDrive\Desktop\face_recog2\image\pg2.png")
        img=img.resize((1530,820),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=820)

        #title
        title_lbl=Label(f_lbl, text="Employee Management System", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        #outer frame
        main_frame=Frame(f_lbl, bd=2, bg="black")
        main_frame.place(x=100,y=150,width=1330,height=570)

        #left inner frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Information", font=("times new roman", 15, "bold"))
        left_frame.place(x=10,y=10,width=650,height=550)

        #current post
        current_post=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Post Information", font=("times new roman", 13, "bold"))
        current_post.place(x=10,y=10,width=620,height=240)

        #department
        dep_label=Label(current_post,text="Department", font=("times new roman", 13, "bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=70,pady=15,sticky=W)

        dep_combo=ttk.Combobox(current_post, textvariable=self.var_dept, font=("times new roman", 13),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Internal Applications/Downloads", "Environment & Sustainabiity", "System Department",
                             "Production Department", "Material Management", "Vigilance", "Enterprise & Resource Planning (ERP)",
                             "Engineering & Equipment Division (EED)", "Recruitment", "Finance Department", "Marketing & Sales",
                             "Personnel Department", "Parliament Affairs Division", "Company Secretary", "Corporate Social Responsibility",
                             "Clearing & Forwarding Division", "Administration Department", "Electronics & Telecommunication", "HRD",
                             "Appeal Cell", "Civil Department", "Coal Videsh", "Internal Audit", "Corporate Planning", "Legal Department",
                             "Project Monitoring Department", "Medical Department", "Contract Management Department", "Rajbhasa",
                             "CC & PR", "Safety & Rescue", "Welfare Department", "New Initiative", "Land & Rehabilitation")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=15,sticky=W)

        #subsidiary
        sub_label=Label(current_post,text="Subsidiary", font=("times new roman", 13, "bold"),bg="white")
        sub_label.grid(row=1,column=0,padx=70,pady=15,sticky=W)

        sub_combo=ttk.Combobox(current_post, textvariable=self.var_sub, font=("times new roman", 13),state="readonly",width=20)
        sub_combo["values"]=("Select Subsidiary","Bharat Coking Fields","Central Coalfields", 
                             "Central Mine, Planning & Design Institute", "Eastern Coalfields", "Mahanadi Coalfields", "Northern Coalfields",
                             "South Eastern Coalfields", "Western Coalfields", "None of the above")
        sub_combo.current(0)
        sub_combo.grid(row=1,column=1,padx=10,pady=15,sticky=W)

        #year of joining
        yr_label=Label(current_post,text="Year of Joining", font=("times new roman", 13, "bold"),bg="white")
        yr_label.grid(row=2,column=0,padx=70,pady=15,sticky=W)

        yr_combo=ttk.Entry(current_post, textvariable=self.var_year, font=("times new roman", 13, "bold"),width=22)
        yr_combo.grid(row=2,column=1,padx=10,pady=15, sticky=W)

        #financial quarter
        fin_label=Label(current_post,text="Financial Quarter", font=("times new roman", 13, "bold"),bg="white")
        fin_label.grid(row=3,column=0,padx=70,pady=15,sticky=W)

        fin_combo=ttk.Combobox(current_post, textvariable=self.var_fin_q, font=("times new roman", 13),state="readonly",width=20)
        fin_combo["values"]=("Select Financial Quarter","!st Quarter", "2nd Quarter", "3rd QUarter", "4th Quarter")
        fin_combo.current(0)
        fin_combo.grid(row=3,column=1,padx=10,pady=15,sticky=W)

        #employee id frame
        emp_id=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Employee ID", font=("times new roman", 13, "bold"))
        emp_id.place(x=10,y=260,width=620,height=250)

        #employee name
        n_label=Label(emp_id,text="Name", font=("times new roman", 13, "bold"),bg="white")
        n_label.grid(row=0,column=0,padx=15,pady=15,sticky=W)

        n_combo=ttk.Entry(emp_id, textvariable=self.var_name, font=("times new roman", 13, "bold"),width=15)
        n_combo.grid(row=0,column=1,padx=15,pady=15, sticky=W)

        #employee roll
        i_label=Label(emp_id,text="ID Number", font=("times new roman", 13, "bold"),bg="white")
        i_label.grid(row=1,column=0,padx=15,pady=15,sticky=W)

        i_combo=ttk.Entry(emp_id, textvariable=self.var_id, font=("times new roman", 13, "bold"),width=15)
        i_combo.grid(row=1,column=1,padx=15,pady=15, sticky=W)

        #employee address
        e_label=Label(emp_id,text="Address", font=("times new roman", 13, "bold"),bg="white")
        e_label.grid(row=3,column=0,padx=15,pady=15,sticky=W)

        e_combo=ttk.Entry(emp_id, textvariable=self.var_add, font=("times new roman", 13, "bold"),width=15)
        e_combo.grid(row=3,column=1,padx=15,pady=15, sticky=W)

        #employee phone
        p_label=Label(emp_id,text="Phone Number", font=("times new roman", 13, "bold"),bg="white")
        p_label.grid(row=0,column=3,padx=15,pady=15,sticky=W)

        p_combo=ttk.Entry(emp_id, textvariable=self.var_ph, font=("times new roman", 13, "bold"),width=15)
        p_combo.grid(row=0,column=4,padx=15,pady=15, sticky=W)

        #gender
        gen_label=Label(emp_id,text="Gender", font=("times new roman", 13, "bold"),bg="white")
        gen_label.grid(row=2,column=0,padx=15,pady=15,sticky=W)

        gen_combo=ttk.Combobox(emp_id, textvariable=self.var_gen, font=("times new roman", 13),state="readonly",width=13)
        gen_combo["values"]=("Select Gender","Male", "Female", "Can't Specify")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=15,pady=15,sticky=W)

        #employee dob
        d_label=Label(emp_id,text="Date of Birth", font=("times new roman", 13, "bold"),bg="white")
        d_label.grid(row=1,column=3,padx=15,pady=15,sticky=W)

        d_combo=ttk.Entry(emp_id, textvariable=self.var_dob, font=("times new roman", 13, "bold"),width=15)
        d_combo.grid(row=1,column=4,padx=15,pady=15, sticky=W)

        #employee email
        p_label=Label(emp_id,text="Email", font=("times new roman", 13, "bold"),bg="white")
        p_label.grid(row=2,column=3,padx=15,pady=15,sticky=W)

        p_combo=ttk.Entry(emp_id, textvariable=self.var_email, font=("times new roman", 13, "bold"),width=15)
        p_combo.grid(row=2,column=4,padx=15,pady=15, sticky=W)

        #right inner frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details", font=("times new roman", 15, "bold"))
        right_frame.place(x=670,y=10,width=650,height=550)

        #form submission
        form_sub=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Form Submission Box", font=("times new roman", 13, "bold"))
        form_sub.place(x=10,y=10,width=630,height=150)

        #radio buttons
        self.var_rad=StringVar()
        rad_1=ttk.Radiobutton(form_sub, text="Take Photo Sample", variable=self.var_rad, value="Yes")
        rad_1.grid(row=0,column=3)

        rad_2=ttk.Radiobutton(form_sub, text="No Photo Sample", variable=self.var_rad, value="No")
        rad_2.grid(row=1,column=3)

        #buttons frame
        btn_frame=Frame(form_sub, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=9,y=50,width=610,height=35)

        save=Button(btn_frame, text="Save", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save.grid(row=0,column=0)
        save.bind("<Button-1>", lambda e: self.add_data())

        update=Button(btn_frame, text="Update", width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update.grid(row=0,column=1)
        update.bind("<Button-1>", lambda e: self.update_data())

        delete=Button(btn_frame, text="Delete", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete.grid(row=0,column=2)
        delete.bind("<Button-1>", lambda e: self.delete_data())

        reset=Button(btn_frame, text="Reset", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset.grid(row=0,column=3)
        reset.bind("<Button-1>", lambda e: self.reset_data())

        btn_frame2=Frame(form_sub, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x=9,y=85,width=610,height=35)

        add=Button(btn_frame2, text="Add Photo Sample", width=30, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        add.grid(row=0,column=0)
        add.bind("<Button-1>", lambda e: self.generate_dataset())

        update_ps=Button(btn_frame2, text="Update Photo Sample", width=30, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_ps.grid(row=0,column=1)

        #search
        search=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search Box", font=("times new roman", 13, "bold"))
        search.place(x=10,y=170,width=630,height=80)

        #search box
        sb = Label(search, text="Search By", font=("times new roman", 13, "bold"), bg="white")
        sb.grid(row=0, column=0, padx=2, pady=15, sticky="w")

        sb_combo = ttk.Combobox(search, font=("times new roman", 13), state="readonly")
        sb_combo["values"] = ("Select Search Criteria", "Department", "Subsidiary", "Year of Joining", "Financial Quarter", "Employee ID", "Employee Name")
        sb_combo.current(0)
        sb_combo.grid(row=0, column=1, padx=2, pady=15, sticky="w")

        sb_entry = ttk.Entry(search, font=("times new roman", 13, "bold"),width=12)
        sb_entry.grid(row=0, column=2, padx=2, pady=15, sticky="w")

        s = Button(search, text="Search", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        s.grid(row=0, column=3, padx=2, pady=15)

        sall = Button(search, text="Show All Results", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        sall.grid(row=0, column=4, padx=2, pady=15)

        #table
        t_fr=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        t_fr.place(x=10,y=270,width=630,height=240)

        scroll_x=ttk.Scrollbar(t_fr,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(t_fr,orient=VERTICAL)

        self.student_table=ttk.Treeview(t_fr, column=("dept","sub","year","fin_q","name","id","gen","add","ph","dob","email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept",text="Department")
        self.student_table.heading("sub",text="Subsidiary")
        self.student_table.heading("year",text="Year of Joining")
        self.student_table.heading("fin_q",text="Financial Year")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("id",text="Employee ID")        
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("add",text="Address")
        self.student_table.heading("ph",text="Phone No")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are Required!", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Sr1nj0yee!", database="schema")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_table values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dept.get(),
                    self.var_sub.get(),
                    self.var_year.get(),
                    self.var_fin_q.get(),
                    self.var_name.get(),
                    self.var_id.get(),
                    self.var_gen.get(),
                    self.var_add.get(),
                    self.var_ph.get(),
                    self.var_dob.get(),
                    self.var_email.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success!","Employee details have been added successfully")
            except Exception as es:
                messagebox.showerror("Error!",f"Due to :{str(es)}",parent=self.root)
            
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Sr1nj0yee!", database="schema")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_table")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0])
        self.var_sub.set(data[1])
        self.var_year.set(data[2])
        self.var_fin_q.set(data[3])
        self.var_name.set(data[4])
        self.var_id.set(data[5])
        self.var_gen.set(data[6])
        self.var_add.set(data[7])
        self.var_ph.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        #self.var_rad.set(data[11])
        # if len(self.data) > 11:  # Ensure the list is long enough
        #     self.var_rad.set(self.data[11])
        # else:
        #     self.var_rad.set(0)

    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are Required!", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update?","Do you want to update the employee details",  parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="Sr1nj0yee!", database="schema")
                    my_cursor=conn.cursor()
                    my_cursor.execute("""
                        UPDATE student_table 
                        SET Department=%s, 
                            Subsidiary=%s, 
                            `Year of Joining`=%s, 
                            `Financial Year`=%s, 
                            Name=%s, 
                            Gender=%s, 
                            Address=%s, 
                            `Phone No`=%s, 
                            `Date of Birth`=%s, 
                            Email=%s 
                        WHERE `Employee ID`=%s
                    """, (
                        self.var_dept.get(),
                        self.var_sub.get(),
                        int(self.var_year.get()),  # Assuming this is an integer field
                        self.var_fin_q.get(),
                        self.var_name.get(),
                        self.var_gen.get(),
                        self.var_add.get(),
                        int(self.var_ph.get()),  # Assuming this is an integer field
                        self.var_dob.get(),      # Make sure this is in the 'YYYY-MM-DD' format for DATE
                        self.var_email.get(),
                        self.var_id.get()        # Assuming Employee ID is an integer field
                    ))

                else:
                    if not update:
                        return
                messagebox.showinfo("Success!","Employee details have been updated successfully")
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error!",f"Due to :{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Employee ID is required!", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete?","Do you want to delete the employee details",  parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="Sr1nj0yee!", database="schema")
                    my_cursor=conn.cursor()
                    sql="delete from student_table where 'Employee ID'=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                if my_cursor.rowcount > 0:
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Record deleted successfully!")
                else:
                    messagebox.showerror("Error", "No record found with that Employee ID.")
            except Exception as es:
                messagebox.showerror("Error!",f"Due to :{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_sub.set("Select Subsidiary")
        self.var_year.set("")
        self.var_fin_q.set("Select Financial Quarter")
        self.var_name.set("")
        self.var_id.set("")
        self.var_gen.set("Select Gender")
        self.var_add.set("")
        self.var_ph.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_rad.set("")

    #generate data set or take photos
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are Required!", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Sr1nj0yee!", database="schema")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_table")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("""
                        UPDATE student_table 
                        SET Department=%s, 
                            Subsidiary=%s, 
                            `Year of Joining`=%s, 
                            `Financial Year`=%s, 
                            Name=%s, 
                            Gender=%s, 
                            Address=%s, 
                            `Phone No`=%s, 
                            `Date of Birth`=%s, 
                            Email=%s 
                        WHERE `Employee ID`=%s
                    """, (
                        self.var_dept.get(),
                        self.var_sub.get(),
                        int(self.var_year.get()),  # Assuming this is an integer field
                        self.var_fin_q.get(),
                        self.var_name.get(),
                        self.var_gen.get(),
                        self.var_add.get(),
                        int(self.var_ph.get()),  # Assuming this is an integer field
                        self.var_dob.get(),      # Make sure this is in the 'YYYY-MM-DD' format for DATE
                        self.var_email.get(),
                        self.var_id.get()==id+1        # Assuming Employee ID is an integer field
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                #using opencv for face detection
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor 1.3 and minimum neighbour 5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset complete...")
            except Exception as es:
                messagebox.showerror("Error!",f"Due to :{str(es)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()