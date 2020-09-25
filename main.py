
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="linen",fg="navy")
        title.pack(side=TOP,fill=X)

        #==========All Variables================================
        self.Roll_var=StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()
        self.Address_var = StringVar()

        self.SearchBy=StringVar()
        self.searchtxt=StringVar()



        #=========Manage Frame==================================

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="navy")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Students",bg="navy",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_Roll=Label(Manage_Frame,text="Roll",bg="navy",fg="white",font=("times new roman",20,"bold"))
        lbl_Roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_Name = Label(Manage_Frame, text="Name", bg="navy", fg="white", font=("times new roman", 20, "bold"))
        lbl_Name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame,textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame,text="Email",bg="navy",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Email = Entry(Manage_Frame,textvariable=self.Email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="navy", fg="white", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",13,"bold",),state="readonly")
        combo_Gender['values']=("Male","Female","Other")
        combo_Gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_Contact = Label(Manage_Frame, text="Contact", bg="navy", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame,textvariable=self.Contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D.O.B", bg="navy", fg="white", font=("times new roman", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_DOB= Entry(Manage_Frame,textvariable=self.DOB_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address", bg="navy", fg="white", font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame,width=26,height=4,font=(" ",10),bd=5,relief=GROOVE)
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #=======Button frame===================================

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="navy")
        btn_Frame.place(x=10, y=520, width=420)

        Addbtn = Button(btn_Frame,text="Add",width=10,command=self.add_Students).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(btn_Frame, text="Update", width=10,command=self.Update_data).grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.Delete_data).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=10,command=self.Clear).grid(row=0, column=3, padx=10, pady=10)

        #==========Detail Frame=================================

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="navy")
        Detail_Frame.place(x=500,y=100,width=830,height=580)

        lbl_search = Label(Detail_Frame, text="Search By", bg="navy", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.SearchBy,width=10, font=("times new roman", 13, "bold",), state="readonly")
        combo_search['values'] = ("Roll", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(Detail_Frame,textvariable=self.searchtxt,width=23, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10,pady=4,command=self.Search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10,pady=4,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        #===========Table Frame===================================

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="navy")
        Table_Frame.place(x=10,y=70,width=800,height=500)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll",text="Roll")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact", text="Contact")
        self.Student_table.heading("DOB", text="DOB")
        self.Student_table.heading("Address", text="Address")
        self.Student_table["show"]="headings"
        self.Student_table.column("Roll",width=100)
        self.Student_table.column("Name", width=100)
        self.Student_table.column("Email", width=100)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("Contact", width=100)
        self.Student_table.column("DOB", width=100)
        self.Student_table.column("Address", width=170)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_Students(self):
        if self.Roll_var.get()=="" or self.Name_var.get()=="":

            messagebox.showerror("Error","Roll and Name fields are required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into studentss values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),
                                                                              self.Name_var.get(),
                                                                              self.Email_var.get(),
                                                                              self.Gender_var.get(),
                                                                              self.Contact_var.get(),
                                                                              self.DOB_var.get(),
                                                                              self.txt_Address.get('1.0',END)))

            con.commit()
            self.fetch_data()
            self.Clear()
            con.close()
            messagebox.showinfo("success","Record has been inserted")



    def fetch_data(self):

        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from studentss")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def Clear(self):
        self.Roll_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.txt_Address.delete("1.0",END)
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END,row[6])

    def Update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update studentss set Name=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s where Roll=%s", ( self.Name_var.get(), self.Email_var.get(), self.Gender_var.get(), self.Contact_var.get(),self.DOB_var.get(), self.txt_Address.get('1.0', END),self.Roll_var.get()))
        con.commit()
        self.fetch_data()
        self.Clear()
        con.close()

    def Delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from studentss where Roll=%s",self.Roll_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.Clear()

    def Search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()

        cur.execute("select * from studentss where " +str(self.SearchBy.get())+" LIKE '%"+str(self.searchtxt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
            con.close()


root=Tk()
ob=Student(root)
root.mainloop()



