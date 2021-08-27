from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import random

def main():
    root=Tk()
    app=SalesLogin(root)

class SalesLogin:
    def __init__(self,master):
        self.master=master
        self.master.title("Database Login System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='lightgreen')
        self.frame=Frame(self.master,bg='lightgreen')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        self.lblTitle=Label(self.frame,text="Community Management Login System",font=("arial",50,'bold'),bg='blue',fg='white')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=20)

        #=================================================================================================================

        self.LoginFrame1=LabelFrame(self.frame,width=1250,height=300,fg='white',text="Login",font=('arial',20,'bold'),relief='ridge',bg='blue',bd=15)
        self.LoginFrame1.grid(row=1,column=0,pady=40)

        self.LoginFrame2=LabelFrame(self.frame,width=900,height=130,fg='white',text="Log",font=('arial',20,'bold'),relief='ridge',bg='blue',bd=15)
        self.LoginFrame2.grid(row=2,column=0)

        
        #=================================================================================================================

        self.lblUsername=Label(self.LoginFrame1,text="Username",font=("arial",15,'bold'),bd=10,bg='blue',fg='white')
        self.lblUsername.grid(row=0,column=0)

        self.txtUsername=Entry(self.LoginFrame1,font=("arial",15,'bold'),bd=7,textvariable=self.Username,width=23)
        self.txtUsername.grid(row=0,column=1,padx=120)

        self.lblPassword=Label(self.LoginFrame1,text="Password",font=("arial",15,'bold'),bd=10,bg='blue',fg='white')
        self.lblPassword.grid(row=1,column=0)

        self.txtPassword=Entry(self.LoginFrame1,font=("arial",15,'bold'),show='*',bd=7,textvariable=self.Password,width=23)
        self.txtPassword.grid(row=1,column=1,columnspan=2,pady=30)




            
        #=================================================================================================================

        self.btnLogin=Button(self.LoginFrame2,text='Login',width=15,font=('arial',20,'bold'),bg='red',fg='white',command=self.Login_System)
        self.btnLogin.grid(row=3,column=0,pady=10,padx=8)

        self.btnReset=Button(self.LoginFrame2,text='Reset',width=15,font=('arial',20,'bold'),bg='red',fg='cornsilk',command=self.iReset)
        self.btnReset.grid(row=3,column=1,pady=10,padx=8)

        self.btnExit=Button(self.LoginFrame2,text='Exit',width=15,font=('arial',20,'bold'),bg='red',fg='cornsilk',command=self.iExit)
        self.btnExit.grid(row=3,column=2,pady=10,padx=8)

 


        
        #=================================================================================================================
    def Login_System(self):
        user=(self.Username.get())
        pas=(self.Password.get())
        if(user==str(147258) and pas==str(123456)):
            self.Login_window()
        elif(user==str(12345678) and pas==str(123456)):
            self.Login_details()
        else:
            tkinter.messagebox.askyesno("Community Management System","Invalid Login details")
            self.Username.set("")
            self.Password.set("")

    def iReset(self):
        self.Username.set("")
        self.Password.set("")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Community Management System","Confirm if you want to Exit")
        if self.iExit>0:
            self.master.destroy()
            return
            

        

    def Login_window(self):
        self.SaleWindow=Toplevel(self.master)
        self.app=SalesManagement(self.SaleWindow)

    def Login_details(self):
        self.SaleWindow=Toplevel(self.master)
        self.app=Details(self.SaleWindow)
        

class SalesManagement:
    def __init__(self,root):
        self.root=root
        self.root.title("Model Comunity Database")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Model Community Database",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="blue",fg="lightgreen")
        title.pack(side=TOP,fill=X)
    #======================================ALL VARIABLES====================================================
        self.aadhar_no_var=StringVar()
        self.name_var=StringVar()
        self.age_var=StringVar()
        self.gender_var=StringVar()
        self.nationality_var=StringVar()
        self.state_var=StringVar()
        self.area_pincode_var=StringVar()
        self.marital_var=StringVar()
        self.religion_var=StringVar()
        self.occupation_var=StringVar()
        self.annual_income_var=StringVar()
        self.contact_var=StringVar()
        self.Mother_tongue_var=StringVar()
        self.medical_record_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        
    #======================================MANAGE FRAME====================================================


        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgreen")
        Manage_Frame.place(x=20,y=100,width=410,height=580)


        m_title=Label(Manage_Frame,text="Manage Details",bg="lightgreen",fg="white",font=("times new roman",15,"bold"))
        m_title.grid(row=0,columnspan=2,pady=7)

        lbl_aadhar=Label(Manage_Frame,text="Aadhar No.",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_aadhar.grid(row=1,column=0,pady=4,padx=20,sticky="w")

        txt_aadhar=Entry(Manage_Frame,textvariable=self.aadhar_no_var,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_aadhar.grid(row=1,column=1,pady=4,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_name.grid(row=2,column=0,pady=4,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=4,padx=20,sticky="w")

        lbl_age=Label(Manage_Frame,text="Age",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_age.grid(row=3,column=0,pady=4,padx=20,sticky="w")

        txt_age=Entry(Manage_Frame,textvariable=self.age_var,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_age.grid(row=3,column=1,pady=4,padx=20,sticky="w")

        lbl_gender=Label(Manage_Frame,text="Gender",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_gender.grid(row=4,column=0,pady=4,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",10,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=4,padx=20)

        lbl_nationality=Label(Manage_Frame,text="Nationality",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_nationality.grid(row=5,column=0,pady=4,padx=20,sticky="w")

        txt_nationality=Entry(Manage_Frame,textvariable=self.nationality_var,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_nationality.grid(row=5,column=1,pady=4,padx=20,sticky="w")

        lbl_state=Label(Manage_Frame,text="State",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_state.grid(row=6,column=0,pady=4,padx=20,sticky="w")

        txt_state=Entry(Manage_Frame,textvariable=self.state_var,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_state.grid(row=6,column=1,pady=4,padx=20,sticky="w")


        lbl_area_pincode=Label(Manage_Frame,text="Area_Pincode",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_area_pincode.grid(row=7,column=0,pady=4,padx=20,sticky="w")

        txt_area_pincode=Entry(Manage_Frame,textvariable=self.area_pincode_var,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_area_pincode.grid(row=7,column=1,pady=4,padx=20,sticky="w")

        lbl_marital=Label(Manage_Frame,text="Marital status",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_marital.grid(row=8,column=0,pady=4,padx=20,sticky="w")

        combo_marital=ttk.Combobox(Manage_Frame,textvariable=self.marital_var,font=("times new roman",10,"bold"),state='readonly')
        combo_marital['values']=("Yes","No")
        combo_marital.grid(row=8,column=1,pady=4,padx=20)

        lbl_religion=Label(Manage_Frame,text="religion",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_religion.grid(row=9,column=0,pady=4,padx=20,sticky="w")

        txt_religion=Entry(Manage_Frame,textvariable=self.religion_var,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_religion.grid(row=9,column=1,pady=4,padx=20,sticky="w")

        lbl_occupation=Label(Manage_Frame,text="Occupation",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_occupation.grid(row=10,column=0,pady=4,padx=20,sticky="w")

        txt_occupation=Entry(Manage_Frame,textvariable=self.occupation_var,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_occupation.grid(row=10,column=1,pady=4,padx=20,sticky="w")

        lbl_annual_income=Label(Manage_Frame,text="Annual Income",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_annual_income.grid(row=11,column=0,pady=4,padx=20,sticky="w")

        combo_annual_income=ttk.Combobox(Manage_Frame,textvariable=self.annual_income_var,font=("times new roman",10,"bold"),state='readonly')
        combo_annual_income['values']=("Lower(<70,069)","Low-middle(70,137 to 2,73,098","Upper-middle(2,73,167 to 8,45,955)","High(>8,46,023)")
        combo_annual_income.grid(row=11,column=1,pady=4,padx=20)

        lbl_contact=Label(Manage_Frame,text="Contact No.",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_contact.grid(row=12,column=0,pady=4,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_contact.grid(row=12,column=1,pady=4,padx=20,sticky="w")

        lbl_Mother_Tongue=Label(Manage_Frame,text="Mother Tongue",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_Mother_Tongue.grid(row=13,column=0,pady=4,padx=20,sticky="w")

        txt_Mother_Tongue=Entry(Manage_Frame,textvariable=self.Mother_tongue_var,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_Mother_Tongue.grid(row=13,column=1,pady=4,padx=20,sticky="w")

        lbl_medical_record=Label(Manage_Frame,text="Medical_Record",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_medical_record.grid(row=14,column=0,pady=4,padx=20,sticky="w")

        txt_medical_record=Entry(Manage_Frame,textvariable=self.medical_record_var,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_medical_record.grid(row=14,column=1,pady=4,padx=20,sticky="w")

        



    #======================================BUTTON FRAME=====================================================

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="lightgreen")
        btn_Frame.place(x=15,y=500,width=370)


        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_comunity).grid(row=0,column=0,padx=5,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=5,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=5,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=5,pady=10)
        
        
    #======================================DETAILS FRAME====================================================


        Details_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgreen")
        Details_Frame.place(x=450,y=100,width=880,height=580)

        lbl_search=Label(Details_Frame,text="Search By",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Details_Frame,textvariable=self.search_by,font=("times new roman",10,"bold"),state='readonly')
        combo_search['values']=("aadhar_no","name","contact","religion","state","nationality","marital","occupation","gender","area_pincode")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search=Entry(Details_Frame,textvariable=self.search_txt,width=25,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Details_Frame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=8,pady=10)
        showallbtn=Button(Details_Frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=8,pady=10)

    #=====================================TABLE FRAME=========================================================

        Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="lightgreen")
        Table_Frame.place(x=10,y=70,width=850,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.comunity_table=ttk.Treeview(Table_Frame,columns=("aadhar_no","name","age","gender","nationality","state","area_pincode","marital","religion","occupation","annual_income","contact","Mother_tongue","medical_record"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.comunity_table.xview)
        scroll_y.config(command=self.comunity_table.yview)
        self.comunity_table.heading("aadhar_no",text="Aadhar No.")
        self.comunity_table.heading("name",text="Name")
        self.comunity_table.heading("age",text="Age")
        self.comunity_table.heading("gender",text="Gender")
        self.comunity_table.heading("nationality",text="Nationality")
        self.comunity_table.heading("state",text="State")
        self.comunity_table.heading("area_pincode",text="Area Pincode")
        self.comunity_table.heading("marital",text="Marital status")
        self.comunity_table.heading("religion",text="Religion")
        self.comunity_table.heading("occupation",text="Occupation")
        self.comunity_table.heading("annual_income",text="Annual Income")
        self.comunity_table.heading("contact",text="Contact No.")
        self.comunity_table.heading("Mother_tongue",text="Mother Tongue")
        self.comunity_table.heading("medical_record",text="Medical Record")
        
        self.comunity_table['show']='headings'
        self.comunity_table.column("aadhar_no",width=150)
        self.comunity_table.column("name",width=150)
        self.comunity_table.column("age",width=150)
        self.comunity_table.column("gender",width=150)
        self.comunity_table.column("nationality",width=190)
        self.comunity_table.column("state",width=190)
        self.comunity_table.column("area_pincode",width=190)
        self.comunity_table.column("marital",width=150)
        self.comunity_table.column("religion",width=150)
        self.comunity_table.column("occupation",width=150)
        self.comunity_table.column("annual_income",width=200)
        self.comunity_table.column("contact",width=150)
        self.comunity_table.column("Mother_tongue",width=190)
        self.comunity_table.column("medical_record",width=190)
        
        self.comunity_table.pack(fill=BOTH,expand=1)
        self.comunity_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.comunity_table.pack()

    def add_comunity(self):
        if self.aadhar_no_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields sre required!!!")
        else:
            conn=mysql.connector.connect(host='localhost',database='std',user='root',password='root')
            cur=conn.cursor()
            cur.execute("insert into comunity values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.aadhar_no_var.get(),
                                                                                           self.name_var.get(),
                                                                                           self.age_var.get(),
                                                                                           self.gender_var.get(),
                                                                                           self.nationality_var.get(),
                                                                                           self.state_var.get(),
                                                                                           self.area_pincode_var.get(),
                                                                                           self.marital_var.get(),
                                                                                           self.religion_var.get(),
                                                                                           self.occupation_var.get(),
                                                                                           self.annual_income_var.get(),
                                                                                           self.contact_var.get(),
                                                                                           self.Mother_tongue_var.get(),
                                                                                           self.medical_record_var.get()))
        
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',database='std',user='root',password='root')
        cur=conn.cursor()
        cur.execute("select * from comunity")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.comunity_table.delete(*self.comunity_table.get_children())
            for row in rows:
                self.comunity_table.insert("",END,values=row)
                conn.commit()
            conn.close()
    def clear(self):
        self.aadhar_no_var.set("")
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.nationality_var.set("")
        self.state_var.set("")
        self.area_pincode_var.set("")
        self.marital_var.set("")
        self.religion_var.set("")
        self.occupation_var.set("")
        self.annual_income_var.set("")
        self.contact_var.set("")
        self.Mother_tongue_var.set("")
        self.medical_record_var.set("")

    def get_cursor(self,ev):
        cursor_row=self.comunity_table.focus()
        contents=self.comunity_table.item(cursor_row)
        row=contents['values']
        self.aadhar_no_var.set(row[0])
        self.name_var.set(row[1])
        self.age_var.set(row[2])
        self.gender_var.set(row[3])
        self.nationality_var.set(row[4])
        self.state_var.set(row[5])
        self.area_pincode_var.set(row[6])
        self.marital_var.set(row[7])
        self.religion_var.set(row[8])
        self.occupation_var.set(row[9])
        self.annual_income_var.set(row[10])
        self.contact_var.set(row[11])
        self.Mother_tongue_var.set(row[12])
        self.medical_record_var.set(row[13])
        
    def update_data(self):
        conn=mysql.connector.connect(host='localhost',database='std',user='root',password='root')
        cur=conn.cursor()
        cur.execute("update comunity set name=%s,age=%s,gender=%s,nationality=%s,state=%s,area_pincode=%s,marital=%s,religion=%s,occupation=%s,annual_income=%s,contact=%s,Mother_tongue=%s,medical_record=%s where aadhar_no=%s",(
                                                                                                                                                                                                                self.name_var.get(),
                                                                                                                                                                                                                self.age_var.get(),
                                                                                                                                                                                                                self.gender_var.get(),
                                                                                                                                                                                                                self.nationality_var.get(),
                                                                                                                                                                                                                self.state_var.get(),
                                                                                                                                                                                                                self.area_pincode_var.get(),
                                                                                                                                                                                                                self.marital_var.get(),
                                                                                                                                                                                                                self.religion_var.get(),
                                                                                                                                                                                                                self.occupation_var.get(),
                                                                                                                                                                                                                self.annual_income_var.get(),
                                                                                                                                                                                                                self.contact_var.get(),
                                                                                                                                                                                                                self.Mother_tongue_var.get(),
                                                                                                                                                                                                                self.medical_record_var.get(),
                                                                                                                                                                                                                self.aadhar_no_var.get()
                                                                                                                                                                                                                ))
        
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()

    def delete_data(self):
        conn=mysql.connector.connect(host='localhost',database='std',user='root',password='root')
        cur=conn.cursor()
        cur.execute("delete from comunity where aadhar_no="+str(self.aadhar_no_var.get()))
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        conn=mysql.connector.connect(host='localhost',database='std',user='root',password='root')
        cur=conn.cursor()
        cur.execute("select * from comunity where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")      
        rows=cur.fetchall()
        if len(rows)!=0:
            self.comunity_table.delete(*self.comunity_table.get_children())
            for row in rows:
                self.comunity_table.insert("",END,values=row)
                conn.commit()
            conn.close()
       
    



class Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Model Community Database")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Model Community Database",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
    #======================================ALL VARIABLES====================================================
        self.aadhar_no_var=StringVar()
        self.name_var=StringVar()
        self.age_var=StringVar()
        self.gender_var=StringVar()
        self.nationality_var=StringVar()
        self.state_var=StringVar()
        self.area_pincode_var=StringVar()
        self.marital_var=StringVar()
        self.religion_var=StringVar()
        self.occupation_var=StringVar()
        self.annual_income_var=StringVar()
        self.contact_var=StringVar()
        self.Mother_tongue_var=StringVar()
        self.medical_record_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()
                                                                      
    #======================================DETAILS FRAME====================================================


        Details_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgreen")
        Details_Frame.place(x=50,y=100,width=1250,height=580)

        lbl_search=Label(Details_Frame,text="Search By",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Details_Frame,textvariable=self.search_by,font=("times new roman",10,"bold"),state='readonly')
        combo_search['values']=("aadhar_no","name","contact","religion","maritual","occupation","gender","Mother_Tongue","area_pincode")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search=Entry(Details_Frame,textvariable=self.search_txt,width=25,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Details_Frame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=8,pady=10)
        showallbtn=Button(Details_Frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=8,pady=10)

    #=====================================TABLE FRAME=========================================================

        Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="lightgreen")
        Table_Frame.place(x=10,y=70,width=1220,height=500)

        lbl_search=Label(Details_Frame,text="Search By",bg="lightgreen",fg="white",font=("times new roman",10,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Details_Frame,textvariable=self.search_by,font=("times new roman",10,"bold"),state='readonly')
        combo_search['values']=("aadhar_no","name","contact","religion","state","nationality","marital","occupation","gender","area_pincode")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search=Entry(Details_Frame,textvariable=self.search_txt,width=25,font=("times new roman",10,"bold"),bd=4,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Details_Frame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=8,pady=10)
        showallbtn=Button(Details_Frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=8,pady=10)

    #=====================================TABLE FRAME=========================================================

        Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="lightgreen")
        Table_Frame.place(x=10,y=70,width=1220,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.comunity_table=ttk.Treeview(Table_Frame,columns=("aadhar_no","name","age","gender","nationality","state","area_pincode","marital","religion","occupation","annual_income","contact","Mother_tongue","medical_record"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.comunity_table.xview)
        scroll_y.config(command=self.comunity_table.yview)
        self.comunity_table.heading("aadhar_no",text="Aadhar No.")
        self.comunity_table.heading("name",text="Name")
        self.comunity_table.heading("age",text="Age")
        self.comunity_table.heading("gender",text="Gender")
        self.comunity_table.heading("nationality",text="Nationality")
        self.comunity_table.heading("state",text="State")
        self.comunity_table.heading("area_pincode",text="Area Pincode")
        self.comunity_table.heading("marital",text="Marital status")
        self.comunity_table.heading("religion",text="Religion")
        self.comunity_table.heading("occupation",text="Occupation")
        self.comunity_table.heading("annual_income",text="Annual Income")
        self.comunity_table.heading("contact",text="Contact No.")
        self.comunity_table.heading("Mother_tongue",text="Mother Tongue")
        self.comunity_table.heading("medical_record",text="Medical Record")
        
        self.comunity_table['show']='headings'
        self.comunity_table.column("aadhar_no",width=150)
        self.comunity_table.column("name",width=150)
        self.comunity_table.column("age",width=150)
        self.comunity_table.column("gender",width=150)
        self.comunity_table.column("nationality",width=190)
        self.comunity_table.column("state",width=190)
        self.comunity_table.column("area_pincode",width=190)
        self.comunity_table.column("marital",width=150)
        self.comunity_table.column("religion",width=150)
        self.comunity_table.column("occupation",width=150)
        self.comunity_table.column("annual_income",width=200)
        self.comunity_table.column("contact",width=150)
        self.comunity_table.column("Mother_tongue",width=190)
        self.comunity_table.column("medical_record",width=190)
        
        self.comunity_table.pack(fill=BOTH,expand=1)
        self.comunity_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.comunity_table.pack()

    def add_comunity(self):
        if self.aadhar_no_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields sre required!!!")
        else:
            conn=mysql.connector.connect(host='localhost',database='std',user='root',password='root')
            cur=conn.cursor()
            cur.execute("insert into comunity values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.aadhar_no_var.get(),
                                                                                           self.name_var.get(),
                                                                                           self.age_var.get(),
                                                                                           self.gender_var.get(),
                                                                                           self.nationality_var.get(),
                                                                                           self.state_var.get(),
                                                                                           self.area_pincode_var.get(),
                                                                                           self.marital_var.get(),
                                                                                           self.religion_var.get(),
                                                                                           self.occupation_var.get(),
                                                                                           self.annual_income_var.get(),
                                                                                           self.contact_var.get(),
                                                                                           self.Mother_tongue_var.get(),
                                                                                           self.medical_record_var.get()))
        
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Success","Record inserted")
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',database='std',user='root',password='root')
        cur=conn.cursor()
        cur.execute("select * from comunity")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.comunity_table.delete(*self.comunity_table.get_children())
            for row in rows:
                self.comunity_table.insert("",END,values=row)
                conn.commit()
            conn.close()
    def clear(self):
        self.aadhar_no_var.set("")
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.nationality_var.set("")
        self.state_var.set("")
        self.area_pincode_var.set("")
        self.marital_var.set("")
        self.religion_var.set("")
        self.occupation_var.set("")
        self.annual_income_var.set("")
        self.contact_var.set("")
        self.Mother_tongue_var.set("")
        self.medical_record_var.set("")

    def get_cursor(self,ev):
        cursor_row=self.comunity_table.focus()
        contents=self.comunity_table.item(cursor_row)
        row=contents['values']
        self.aadhar_no_var.set(row[0])
        self.name_var.set(row[1])
        self.age_var.set(row[2])
        self.gender_var.set(row[3])
        self.nationality_var.set(row[4])
        self.state_var.set(row[5])
        self.area_pincode_var.set(row[6])
        self.marital_var.set(row[7])
        self.religion_var.set(row[8])
        self.occupation_var.set(row[9])
        self.annual_income_var.set(row[10])
        self.contact_var.set(row[11])
        self.Mother_tongue_var.set(row[12])
        self.medical_record_var.set(row[13])
        
    def update_data(self):
        conn=mysql.connector.connect(host='localhost',database='std',user='root',password='root')
        cur=conn.cursor()
        cur.execute("update comunity set name=%s,age=%s,gender=%s,nationality=%s,state=%s,area_pincode=%s,maritual=%s,religion=%s,occupation=%s,annual_income=%s,contact=%s,Mother_tongue=%s,medical_record=%s where aadhar_no=%s",(
                                                                                                                                                                                                                self.name_var.get(),
                                                                                                                                                                                                                self.age_var.get(),
                                                                                                                                                                                                                self.gender_var.get(),
                                                                                                                                                                                                                self.nationality_var.get(),
                                                                                                                                                                                                                self.state_var.get(),
                                                                                                                                                                                                                self.area_pincode_var.get(),
                                                                                                                                                                                                                self.marital_var.get(),
                                                                                                                                                                                                                self.religion_var.get(),
                                                                                                                                                                                                                self.occupation_var.get(),
                                                                                                                                                                                                                self.annual_income_var.get(),
                                                                                                                                                                                                                self.contact_var.get(),
                                                                                                                                                                                                                self.Mother_tongue_var.get(),
                                                                                                                                                                                                                self.medical_record_var.get(),
                                                                                                                                                                                                                self.aadhar_no_var.get()
                                                                                                                                                                                                                ))
        
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()

    def delete_data(self):
        conn=mysql.connector.connect(host='localhost',database='std',user='root',password='root')
        cur=conn.cursor()
        cur.execute("delete from comunity where aadhar_no="+str(self.aadhar_no_var.get()))
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        conn=mysql.connector.connect(host='localhost',database='std',user='root',password='root')
        cur=conn.cursor()
        cur.execute("select * from comunity where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")      
        rows=cur.fetchall()
        if len(rows)!=0:
            self.comunity_table.delete(*self.comunity_table.get_children())
            for row in rows:
                self.comunity_table.insert("",END,values=row)
                conn.commit()
            conn.close()


if __name__ =='__main__':
    main()


