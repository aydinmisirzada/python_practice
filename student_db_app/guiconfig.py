from tkinter import *
from tkinter import ttk
from dbconfig import database

class Interface:
    headers = ['ID','First Name','Last Name','Email','Street','City','State','Zip','Phone','Birth','Sex','Date Entered']
    student_info = []
    widget_entries = []

    def __init__(self):
        self.tree = None
        self.create_widgets()

    def create_widgets(self):
        sid_label = Label(root,text='ID')
        sid_label.grid(row=0,column=0,padx=5,pady=10,sticky='W')
        self.sid_entry_value = StringVar(root,value="")
        self.sid_entry = ttk.Entry(root,textvariable=self.sid_entry_value)
        self.sid_entry.grid(row=0,column=1,padx=5,pady=10,sticky='W')
        #
        sfn_label = Label(root,text='First Name')
        sfn_label.grid(row=0,column=2,padx=5,pady=10,sticky='W')
        self.sfn_entry_value = StringVar(root,value="")
        self.widget_entries.append(self.sfn_entry_value)
        self.sfn_entry = ttk.Entry(root,textvariable=self.sfn_entry_value)
        self.sfn_entry.grid(row=0,column=3,padx=5,pady=10,sticky='W')
        #
        sln_label = Label(root,text='Last Name')
        sln_label.grid(row=0,column=4,padx=5,pady=10,sticky='W')
        self.sln_entry_value = StringVar(root,value="")
        self.widget_entries.append(self.sln_entry_value)
        self.sln_entry = ttk.Entry(root,textvariable=self.sln_entry_value)
        self.sln_entry.grid(row=0,column=5,padx=5,pady=10,sticky='W')
        #
        se_label = Label(root,text='Email')
        se_label.grid(row=0,column=6,padx=5,pady=10,sticky='W')
        self.se_entry_value = StringVar(root,value="")
        self.widget_entries.append(self.se_entry_value)
        self.se_entry = ttk.Entry(root,textvariable=self.se_entry_value)
        self.se_entry.grid(row=0,column=7,padx=5,pady=10,sticky='W')
        #
        ss_label = Label(root,text='Street')
        ss_label.grid(row=0,column=8,padx=5,pady=10,sticky='W')
        self.ss_entry_value = StringVar(root,value="")
        self.widget_entries.append(self.ss_entry_value)
        self.ss_entry = ttk.Entry(root,textvariable=self.ss_entry_value)
        self.ss_entry.grid(row=0,column=9,padx=5,pady=10,sticky='W')
        #
        sc_label = Label(root,text='City')
        sc_label.grid(row=1,column=0,padx=5,pady=10,sticky='W')
        self.sc_entry_value = StringVar(root,value="")
        self.widget_entries.append(self.sc_entry_value)
        self.sc_entry = ttk.Entry(root,textvariable=self.sc_entry_value)
        self.sc_entry.grid(row=1,column=1,padx=5,pady=10,sticky='W')
        #
        sst_label = Label(root,text='State')
        sst_label.grid(row=1,column=2,padx=5,pady=10,sticky='W')
        self.sst_entry_value = StringVar(root,value="")
        self.widget_entries.append(self.sst_entry_value)
        self.sst_entry = ttk.Entry(root,textvariable=self.sst_entry_value)
        self.sst_entry.grid(row=1,column=3,padx=5,pady=10,sticky='W')
        #
        sz_label = Label(root,text='Zip')
        sz_label.grid(row=1,column=4,padx=5,pady=10,sticky='W')
        self.sz_entry_value = StringVar(root,value="")
        self.widget_entries.append(self.sz_entry_value)
        self.sz_entry = ttk.Entry(root,textvariable=self.sz_entry_value)
        self.sz_entry.grid(row=1,column=5,padx=5,pady=10,sticky='W')
        #
        sph_label = Label(root,text='Phone')
        sph_label.grid(row=1,column=6,padx=5,pady=10,sticky='W')
        self.sph_entry_value = StringVar(root,value="")
        self.widget_entries.append(self.sph_entry_value)
        self.sph_entry = ttk.Entry(root,textvariable=self.sph_entry_value)
        self.sph_entry.grid(row=1,column=7,padx=5,pady=10,sticky='W')
        #
        sb_label = Label(root,text='Birth')
        sb_label.grid(row=1,column=8,padx=5,pady=10,sticky='W')
        self.sb_entry_value = StringVar(root,value="")
        self.widget_entries.append(self.sb_entry_value)
        self.sb_entry = ttk.Entry(root,textvariable=self.sb_entry_value)
        self.sb_entry.grid(row=1,column=9,padx=5,pady=10,sticky='W')
        #
        ssx_label = Label(root,text='Sex')
        ssx_label.grid(row=2,column=0,padx=5,pady=10,sticky='W')
        self.ssx_entry_value = StringVar(root,value="")
        self.widget_entries.append(self.ssx_entry_value)
        self.widget_entries.append(self.sid_entry_value)
        self.ssx_entry = ttk.Entry(root,textvariable=self.ssx_entry_value)
        self.ssx_entry.grid(row=2,column=1,padx=5,pady=10,sticky='W')
        #
        add_button = ttk.Button(root,text='Add Student',command=self.add_student)
        add_button.grid(column=4,row=2,sticky=(W,E))
        #
        update_button = ttk.Button(root,text='Update Student',command=self.update_student)
        update_button.grid(column=5,row=2,sticky=(W,E))
        #
        delete_button = ttk.Button(root,text='Delete Student',command=self.delete_student)
        delete_button.grid(column=6,row=2,sticky=(W,E))
        #
        self.tree = ttk.Treeview(root,height=15,columns=('ID','First Name','Last Name','Email','Street','City','State','Zip','Phone','Birth','Sex','Date Entered'),selectmode='browse')
        self.tree.grid(row=3,column=0,columnspan=17)
        self.tree['show']='headings'
        i = 1
        for col in self.headers:
            num = f'#{i}'
            self.tree.heading(num,text=col)
            self.tree.column(num,width=120)
            i += 1

        self.update_table()

    def update_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        query = "SELECT student_id,first_name,last_name,email,street,city,state,zip,phone,birth_date,sex,date_entered FROM students"
        self.student_info = mydb.execute_query('select',query)
        i = 1
        for stud in self.student_info:
            num = f"#{i}"
            self.tree.insert('','end',values=stud)
            i += 1

    def validate_entries(self,n):
        for i in range(n):
            if len(self.widget_entries[i].get()) == 0:
                return False
        return True

    def add_student(self):
        if not self.validate_entries(10):
            self.popup_msg("Fill all entries")
            return

        student = []
        for i in self.widget_entries:
            if len(i.get()) == 0:
                continue
            student.append(i.get())

        mydb.add_student(student)
        self.update_table()

    def update_student(self):
        if not self.validate_entries(11):
            self.popup_msg("Fill all entries")
            return

        student = []
        for i in self.widget_entries:
            if len(i.get()) == 0:
                continue
            student.append(i.get())

        mydb.update_student(student)
        self.update_table()


    def delete_student(self):
        id = self.widget_entries[10].get()
        if len(id) == 0:
            self.popup_msg("Specify Student ID")
            return

        mydb.delete_student(id)
        self.update_table()


    def popup_msg(self,msg):
        popup = Tk()
        popup.geometry("235x85")
        popup.resizable(width=False,height=False)
        popup.wm_title("Enter All Values")
        err_msg = Text(popup,font=("Verdana",16))
        err_msg.insert(INSERT,msg)
        err_msg.pack()
        ok_button = ttk.Button(popup,text="Close",command=popup.destroy)
        ok_button.place(relx=.5,rely=.8,anchor="center")
        popup.mainloop()


root = Tk()
root.geometry("1400x600")
root.title('Student Database')
mydb = database()
