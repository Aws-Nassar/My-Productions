import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import office_official_one
from Dictionary import Word
import sqlite3
from datetime import date

def page():
    global counter
    counter = 0
    app = ctk.CTk()
    app.title('Workers Information')
    #app.geometry('900x345')
    window_width = 1115
    window_height = 390
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    app.config(bg = '#161C25')
    app.resizable(False , False)
    def validate_input(action, value):
        # Check if the input is empty or if it's a digit
        if action == '1':  # Insertion or deletion (1 means the text is being inserted/deleted)
            return value.isdigit() or value == ""
        return True
    validation = app.register(validate_input)
    font1 = ('Arial' , 20 , 'bold')
    font2 = ('Arial' , 16 , 'bold')
    name_label = ctk.CTkLabel(app, font = font1, text = 'Name:', text_color='yellow', bg_color='#161C25')
    name_label.place(x = 20 , y = 20)
    name_entry = ctk.CTkEntry(app, font = font1, text_color = 'red' , bg_color ='#161C25', border_color='#161C25', border_width=2, width = 180)
    name_entry.place(x = 180 , y = 20)
    worker_id_label = ctk.CTkLabel(app, font = font1, text = 'Worker-ID:', text_color='yellow', bg_color='#161C25')
    worker_id_label.place(x = 20 , y = 80)
    worker_id_entry = ctk.CTkEntry(app, font = font1, text_color = 'red' , bg_color ='#161C25', border_color='#161C25', border_width=2, width = 180, validate="key", validatecommand=(validation, '%d', '%S'))
    worker_id_entry.place(x = 180 , y = 80)
    Scientific_Qualification_label = ctk.CTkLabel(app, font = font1, text = 'Scientific qualification:', text_color='yellow', bg_color='#161C25')
    Scientific_Qualification_label.place(x = 461 , y = 20)
    Scientific_Qualification_entry = ctk.CTkEntry(app, font = font1, text_color = 'red' , bg_color ='#161C25', border_color='#161C25', border_width=2, width = 180)
    Scientific_Qualification_entry.place(x = 700 , y = 20)
    Job_title_label = ctk.CTkLabel(app, font = font1, text = 'Job title:', text_color='yellow', bg_color='#161C25')
    Job_title_label.place(x = 595 , y = 80)
    Job_title_entry = ctk.CTkEntry(app, font = font1, text_color = 'red' , bg_color ='#161C25', border_color='#161C25', border_width=2, width = 180)
    Job_title_entry.place(x = 700 , y = 80)
    def add_to_treeview():
        nm = name_entry.get()
        sq = Scientific_Qualification_entry.get()
        wi = worker_id_entry.get()
        jt = Job_title_entry.get()
        item_ids = tree.get_children()
        for item_id in item_ids:
            # Retrieve the values from the specified columns ('worker ID')
            worker_id = tree.item(item_id, 'values')[1]  # index 2 corresponds to the 'registration number' column
            if (worker_id == wi):
                messagebox.showerror(title='Registered Worker', message='Worker already exists!')
                return 
        global counter
        counter = counter + 1
        tree.insert('', "end", values=(nm,wi,sq,jt))
        name_entry.delete(0,'end')
        Scientific_Qualification_entry.delete(0,'end')
        worker_id_entry.delete(0,'end')
        Job_title_entry.delete(0,'end')
    def insert_button_function():
        name = name_entry.get()
        wid_temp = worker_id_entry.get()
        sq = Scientific_Qualification_entry.get()
        jt = Job_title_entry.get()

        if name == '' or wid_temp == '' or jt == '':
            messagebox.showerror(title='Empty Field', message='There is a field(s) missing, please fill them in')
            return
        wid = int(wid_temp)
        File = 'DataBase.db'
        connection = sqlite3.connect(File)
        cursor = connection.cursor()
        cursor.execute("""select * from Workers where W_ID = ?""",(wid,))
        find = cursor.fetchone()
        if find == None:
            messagebox.showerror(title='Invalid input', message='please check the entered Worker ID')
            return
        fname = find[0] + ' ' + find[1] + ' ' + find[2]
        if fname != name:
            messagebox.showerror(title='Invalid input', message='please check the entered name')
            return
        elif find[4] != jt:
            messagebox.showerror(title='Invalid input', message='please check the job title')
            return
        if sq == '':
            if find[5] != None:
                messagebox.showerror(title='Invalid input', message='please check the entered scientific qualification')
                return  
        elif sq != '':
            if find[5] != sq:
                messagebox.showerror(title='Invalid input', message='please check the entered scientific qualification')
                return    
        

        add_to_treeview()
    def on_enter(event):
        insert_button.invoke()
    insert_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Insert Data', fg_color='#05A312', hover_color='#00850B', bg_color='#161C25', cursor = 'hand2', corner_radius=15,width = 260, command = insert_button_function)
    insert_button.place(x =17 ,y =350)
    app.bind("<Return>", on_enter)
    def nextPage():
        class_no = Word["classification_num"]
        File = 'DataBase.db'
        connection = sqlite3.connect(File)
        cursor = connection.cursor()
        cursor.execute("""select * from Workers where Classification_Number = ? """,(class_no,))
        find = cursor.fetchall()
        if counter < len(find):
            messagebox.showwarning(title='Incomplete entry', message='You need to enter all of your office workers')
            return
        
        cursor.execute("""UPDATE ranktemp SET office_official_flag = 1 where Classification_Number = ?""", (class_no,))
        connection.commit()

        cursor.execute("""select * from Bill""")
        find = cursor.fetchall()
        Fees_paid = 200

        if len(find) == 0:
            Bill_Number = 565
        else:
            Bill_Number = 0
            for row in find:
                Bill_Number = row[0]
            Bill_Number = Bill_Number + 1
        
        current_date = date.today()

        cursor.execute("""insert into Bill values(?,?,?,?)""",(Bill_Number,current_date,Fees_paid,class_no,))
        connection.commit()
        cursor.execute("""select * from ranktemp where Classification_Number = ? """,(class_no,))
        print(cursor.fetchone())
        cursor.execute("""select * from Bill where Bill_Number = ? """,(Bill_Number,))
        print(cursor.fetchone())
        connection.close()
        
        app.destroy()
        office_official_one.page()
    next_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Next Page', fg_color='#161C25', hover_color='#FF5002', bg_color='#161C25',border_color='#F15704',border_width=2, cursor = 'hand2', corner_radius=15, width = 260, command = nextPage)
    next_button.place(x =320 ,y =350)
    def finishing():
        app.destroy()
    close_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Close', fg_color='#E40404', hover_color='#AE0000', bg_color='#161C25',border_color='#E40404',border_width=2, cursor = 'hand2', corner_radius=15, width = 260, command = finishing)
    close_button.place(x =623 ,y =350)
    style = ttk.Style(app)
    style.theme_use('clam')
    style.configure('Treeview', font = font2, foreground = '#fff', background = '#000',fieldbackground = '#313837', rowheight=40)# Increase font size for Treeview structure via rowheight
    style.configure('Treeview.Heading', font=('Arial', 18))# Increase the font size for column names
    style.map('Treeview', background = [('selected', '#1A8F2D')])
    tree = ttk.Treeview(app,height = 3)
    tree['columns'] = ('name', 'Worker-ID' , 'Scientific_Qualification', 'Job title')
    tree.column('#0', width = 0, stretch= tk.NO) # to hide the default first column of the treeview
    tree.column('name', anchor = tk.CENTER, width = 269)
    tree.column('Worker-ID', anchor = tk.CENTER, width = 269)
    tree.column('Scientific_Qualification', anchor = tk.CENTER, width = 269)
    tree.column('Job title', anchor = tk.CENTER, width = 269)
    tree.heading('name',text = 'name')
    tree.heading('Worker-ID',text = 'Worker-ID')
    tree.heading('Scientific_Qualification',text = 'Scientific_Qualification')
    tree.heading('Job title',text = 'Job title')
    tree.place(x =22, y = 180 )
    app.mainloop()