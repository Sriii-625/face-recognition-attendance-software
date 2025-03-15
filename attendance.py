from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox, filedialog
import mysql.connector
import csv
import os

my_data = []
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x820+0+0")
        self.root.title("Attendance Management System")

        #variables
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_sub=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_atten=StringVar()

        #background image
        img=Image.open(r"C:\Users\srinj\OneDrive\Desktop\face_recog2\image\pg5.webp")
        img=img.resize((1530,820),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=820)

        #title
        title_lbl=Label(f_lbl, text="Employee Attendance Management System", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        #outer frame
        main_frame=Frame(f_lbl, bd=2, bg="black")
        main_frame.place(x=100,y=150,width=1330,height=570)

        #left inner frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Information", font=("times new roman", 15, "bold"))
        left_frame.place(x=10,y=10,width=650,height=550)

        #name
        t_label=Label(left_frame,text="Name", font=("times new roman", 13, "bold"),bg="white")
        t_label.grid(row=0,column=0,padx=70,pady=15,sticky=W)

        t_entry=ttk.Entry(left_frame, textvariable=self.var_name, font=("times new roman", 13, "bold"),width=22)
        t_entry.grid(row=0,column=1,padx=10,pady=15, sticky=W)

        #department
        dep_label=Label(left_frame,text="Department", font=("times new roman", 13, "bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=70,pady=15,sticky=W)

        dep_combo=ttk.Combobox(left_frame, textvariable=self.var_dept, font=("times new roman", 13),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Internal Applications/Downloads", "Environment & Sustainabiity", "System Department",
                             "Production Department", "Material Management", "Vigilance", "Enterprise & Resource Planning (ERP)",
                             "Engineering & Equipment Division (EED)", "Recruitment", "Finance Department", "Marketing & Sales",
                             "Personnel Department", "Parliament Affairs Division", "Company Secretary", "Corporate Social Responsibility",
                             "Clearing & Forwarding Division", "Administration Department", "Electronics & Telecommunication", "HRD",
                             "Appeal Cell", "Civil Department", "Coal Videsh", "Internal Audit", "Corporate Planning", "Legal Department",
                             "Project Monitoring Department", "Medical Department", "Contract Management Department", "Rajbhasa",
                             "CC & PR", "Safety & Rescue", "Welfare Department", "New Initiative", "Land & Rehabilitation")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=10,pady=15,sticky=W)

        #subsidiary
        sub_label=Label(left_frame,text="Subsidiary", font=("times new roman", 13, "bold"),bg="white")
        sub_label.grid(row=2,column=0,padx=70,pady=15,sticky=W)

        sub_combo=ttk.Combobox(left_frame, textvariable=self.var_sub, font=("times new roman", 13),state="readonly",width=20)
        sub_combo["values"]=("Select Subsidiary","Bharat Coking Fields","Central Coalfields", 
                             "Central Mine, Planning & Design Institute", "Eastern Coalfields", "Mahanadi Coalfields", "Northern Coalfields",
                             "South Eastern Coalfields", "Western Coalfields", "None of the above")
        sub_combo.current(0)
        sub_combo.grid(row=2,column=1,padx=10,pady=15,sticky=W)

        #time
        t_label=Label(left_frame,text="Time", font=("times new roman", 13, "bold"),bg="white")
        t_label.grid(row=3,column=0,padx=70,pady=15,sticky=W)

        t_entry=ttk.Entry(left_frame, textvariable=self.var_time, font=("times new roman", 13, "bold"),width=22)
        t_entry.grid(row=3,column=1,padx=10,pady=15, sticky=W)

        #date
        d_label=Label(left_frame,text="Date", font=("times new roman", 13, "bold"),bg="white")
        d_label.grid(row=4,column=0,padx=70,pady=15,sticky=W)

        d_entry=ttk.Entry(left_frame, textvariable=self.var_date, font=("times new roman", 13, "bold"),width=22)
        d_entry.grid(row=4,column=1,padx=10,pady=15, sticky=W)

        #attendance Status
        at_label=Label(left_frame,text="Attendance Status", font=("times new roman", 13, "bold"),bg="white")
        at_label.grid(row=5,column=0,padx=70,pady=15,sticky=W)

        at_combo=ttk.Combobox(left_frame, textvariable=self.var_atten, font=("times new roman", 13),state="readonly",width=20)
        at_combo["values"]=("Select Status","Present","Absent")
        at_combo.current(0)
        at_combo.grid(row=5,column=1,padx=10,pady=15,sticky=W)

        #buttons frame
        btn_frame=Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=58,y=380,width=540,height=70)

        import_csv=Button(btn_frame, text="Import CSV", width=26, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        import_csv.grid(row=0,column=0)
        import_csv.bind("<Button-1>", lambda e: self.import_func())

        export_csv=Button(btn_frame, text="Export CSV", width=27, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_csv.grid(row=0,column=1)
        export_csv.bind("<Button-1>", lambda e: self.export_func())

        update=Button(btn_frame, text="Update", width=26, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update.grid(row=1,column=0)
        update.bind("<Button-1>", lambda e: self.update_data())

        reset=Button(btn_frame, text="Reset", width=27, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset.grid(row=1,column=1)
        reset.bind("<Button-1>", lambda e: self.reset_data())

        #right inner frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details", font=("times new roman", 15, "bold"))
        right_frame.place(x=670,y=10,width=650,height=550)

        #table
        t_fr=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        t_fr.place(x=10,y=10,width=625,height=500)

        scroll_x=ttk.Scrollbar(t_fr,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(t_fr,orient=VERTICAL)

        self.attendance_table=ttk.Treeview(t_fr, column=("name","dept","sub","time","date","attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("name",text="Name")
        self.attendance_table.heading("dept",text="Department")
        self.attendance_table.heading("sub",text="Subsidiary")
        self.attendance_table.heading("time",text="Time")
        self.attendance_table.heading("date",text="Date")
        self.attendance_table.heading("attendance",text="Attendance")
        self.attendance_table["show"]="headings"

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)
        #self.fetch_data()

    def fetch_data(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)

    def import_func(self):
        global my_data
        my_data.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                my_data.append(i)
            self.fetch_data(my_data)

    def export_func(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to {es}",parent=self.root)

    def get_cursor(self, event=""):
        cursor_focus=self.attendance_table.focus()
        content=self.attendance_table.item(cursor_focus)
        data=content["values"]

        self.var_name.set(data[0])
        self.var_dept.set(data[1])
        self.var_sub.set(data[2])
        self.var_time.set(data[3])
        self.var_date.set(data[4])
        self.var_atten.set(data[5])

    def reset_data(self):
        self.var_name.set("Select Name")
        self.var_dept.set("Select Department")
        self.var_sub.set("Select Subsidiary")
        self.var_time.set("")
        self.var_date.set("")
        self.var_atten.set("Select Status")



if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()