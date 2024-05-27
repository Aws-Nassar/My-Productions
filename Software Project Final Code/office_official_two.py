import customtkinter as ctk
import office_official_three
from tkinter import *
from Dictionary import Word
from tkinter import messagebox
import sqlite3
def page():
    root = ctk.CTk()
    window_width = 1300
    window_height = 495
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    def validate_input_with_dot(action, value):
        # Check if the input is empty or if it's a digit
        if action == '1':  # Insertion or deletion (1 means the text is being inserted/deleted)
            return value.isdigit() or value == "" or value == "."
        return True
    def validate_input(action, value):
        # Check if the input is empty or if it's a digit
        if action == '1':  # Insertion or deletion (1 means the text is being inserted/deleted)
            return value.isdigit() or value == ""
        return True
    validation = root.register(validate_input)
    validation_with_dot = root.register(validate_input_with_dot)
    root.config(bg='#161C25')
    root.resizable(False,False)
    root.title("Office Informaion")
    font1 = ("Arial", 20, "bold")
    ofnameLabel = ctk.CTkLabel(root,text="office name:",font=font1, text_color="yellow", bg_color="#161C25" )
    ofnameLabel.place(x=120,y=10)
    ofname = ctk.CTkEntry(master=root,font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300)
    ofname.place(x=250,y=10)
    Classification_NumberLabel = ctk.CTkLabel(root,text="classification number:",font=font1, text_color="yellow", bg_color="#161C25" )
    Classification_NumberLabel.place(x=26,y=60)
    Classification_Number = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300,validate="key", validatecommand=(validation, '%d', '%S'))
    Classification_Number.place(x = 250 , y = 60)
    rankLabel = ctk.CTkLabel(root,text="rank to be classified by:",font=font1, text_color="yellow", bg_color="#161C25" )
    rankLabel.place(x=10,y=110)
    options = ['consultive', 'first class', 'second class', 'third class']
    variable1 = StringVar()
    rank_options = ctk.CTkComboBox(root, font = font1, text_color= 'red', fg_color= '#fff',bg_color='black', dropdown_hover_color='yellow', button_color='#FFFF4D', button_hover_color='yellow', border_color='#FFFF4D', width = 180, variable = variable1, values=options, state = 'readonly')
    #rank_options.set('third class')
    rank_options.place(x = 250,y = 110)
    Date_of_EstablishmentLabel = ctk.CTkLabel(root,text="date of establishment:",font=font1, text_color="yellow", bg_color="#161C25" )
    Date_of_EstablishmentLabel.place(x=27,y=160)
    Date_of_Establishment = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300)
    Date_of_Establishment.place(x = 250,y = 160 )
    Office_AreaLabel = ctk.CTkLabel(root,text="office area:",font=font1, text_color="yellow", bg_color="#161C25")
    Office_AreaLabel.place(x=130,y=210)
    Office_Area = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300, validate="key", validatecommand=(validation_with_dot, '%d', '%S'))
    Office_Area.place(x = 250,y = 210 )
    cityLabel = ctk.CTkLabel(root,text="city/town:",font=font1, text_color="yellow", bg_color="#161C25" )
    cityLabel.place(x=145,y=260)
    city = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300)
    city.place(x = 250,y = 260 )
    streetLabel = ctk.CTkLabel(root,text="street/building:",font=font1, text_color="yellow", bg_color="#161C25")
    streetLabel.place(x=92,y=310)
    street = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300)
    street.place(x = 250,y = 310 )
    tnumberLabel = ctk.CTkLabel(root,text="telephone number:",font=font1, text_color="yellow", bg_color="#161C25")
    tnumberLabel.place(x=58,y=360)
    tnumber = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300,validate="key", validatecommand=(validation, '%d', '%S'))
    tnumber.place(x = 250,y = 360 )
    
    cnumberLabel = ctk.CTkLabel(root,text="cellular number:",font=font1, text_color="yellow", bg_color="#161C25")
    cnumberLabel.place(x=800,y=10)
    cnumber = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300,validate="key", validatecommand=(validation, '%d', '%S'))
    cnumber.place(x = 970,y = 10 )

    faxLabel = ctk.CTkLabel(root,text="fax number:",font=font1, text_color="yellow", bg_color="#161C25" )
    faxLabel.place(x= 841,y=60)
    fax = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300,validate="key", validatecommand=(validation, '%d', '%S'))
    fax.place(x = 970,y = 60 )

    pcodeLabel = ctk.CTkLabel(root,text="postal code:",font=font1, text_color="yellow", bg_color="#161C25" )
    pcodeLabel.place(x=837,y=110)
    pcode = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300)
    pcode.place(x = 970,y = 110 )

    emailLabel = ctk.CTkLabel(root,text="email:",font=font1, text_color="yellow", bg_color="#161C25" )
    emailLabel.place(x=897,y=160)
    email = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300)
    email.place(x = 970,y = 160 )

    Request_Renewing_YearLabel = ctk.CTkLabel(root,text="request renewing year:",font=font1, text_color="yellow", bg_color="#161C25" )
    Request_Renewing_YearLabel.place(x=737,y=210)
    Request_Renewing_Year = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300,validate="key", validatecommand=(validation, '%d', '%S'))
    Request_Renewing_Year.place(x = 970,y = 210 )

    # Office_Annual_subscriptionLabel = ctk.CTkLabel(root,text="office annual subscription:",font=font1, text_color="yellow", bg_color="#161C25" )
    # Office_Annual_subscriptionLabel.place(x=601,y=260)
    # Office_Annual_subscription = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300, validate="key", validatecommand=(validation_with_dot, '%d', '%S'))
    # Office_Annual_subscription.place(x = 870,y = 260 )

    # Office_Outstanding_loansLabel = ctk.CTkLabel(root,text="office outstanding loans:",font=font1, text_color="yellow", bg_color="#161C25" )
    # Office_Outstanding_loansLabel.place(x=619,y=310)
    # Office_Outstanding_loans = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300, validate="key", validatecommand=(validation_with_dot, '%d', '%S'))
    # Office_Outstanding_loans.place(x = 870,y = 310 )

    # Other_financial_receivablesLabel = ctk.CTkLabel(root,text="other financial receivables:",font=font1, text_color="yellow", bg_color="#161C25" )
    # Other_financial_receivablesLabel.place(x=596,y=360)
    # Other_financial_receivables = ctk.CTkEntry(master=root, font = font1 ,text_color = 'red' , bg_color ='#161C25', border_color='#161C25', width=300, validate="key", validatecommand=(validation_with_dot, '%d', '%S'))
    # Other_financial_receivables.place(x = 870,y = 360 )

    Office_SpecializationLabel = ctk.CTkLabel(root,text="Specializations to be classified into:",font=font1, text_color="yellow", bg_color="#161C25" )
    Office_SpecializationLabel.place(x=615,y=260)
    ar = ctk.CTkCheckBox(root, text = 'architectural engineering', font = font1, text_color='yellow', bg_color ='#161C25', border_color='yellow')
    ar.place(x =637 , y =314 )
    c = ctk.CTkCheckBox(root, text = 'civil engineering', font = font1, text_color='yellow', bg_color ='#161C25', border_color='yellow')
    c.place(x = 637 , y =364 )

    e = ctk.CTkCheckBox(root, text = 'electrical engineering', font = font1, text_color='yellow', bg_color ='#161C25', border_color='yellow')
    e.place(x = 970, y = 314)
    mh = ctk.CTkCheckBox(root, text = 'mechanical engineering', font = font1, text_color='yellow', bg_color ='#161C25', border_color='yellow')
    mh.place(x = 970, y = 364)
    def nextFunction():
        name = ofname.get()
        class_no_temp = Classification_Number.get()
        r = rank_options.get()
        dat = Date_of_Establishment.get()
        Office_Area_temp = Office_Area.get()
        city_ = city.get()
        street_ = street.get()
        tnumber_temp = tnumber.get()
        cnumber_temp = cnumber.get()
        fax_temp = fax.get()
        postal_code = pcode.get()
        email_ = email.get()
        Request_Renewing_Year_temp = Request_Renewing_Year.get()
        #Office_Annual_subscription_temp = Office_Annual_subscription.get()
        #Office_Outstanding_loans_temp = Office_Outstanding_loans.get()
        #Other_financial_receivables_temp = Other_financial_receivables.get()
        if name == '' or class_no_temp == '' or r == '' or dat == '' or Office_Area_temp == '' or city_ == '' or street_ == '' or cnumber_temp == '' or postal_code == '' or email_ == '' or Request_Renewing_Year_temp == '' or (ar.get() == 0 and c.get() == 0 and e.get() == 0 and mh.get() == 0):
            messagebox.showwarning(title='Empty Field', message='There is a field(s) missing, please fill them in')
            return
        else:
            class_no = int(class_no_temp)
            off_area = float(Office_Area_temp)
            if tnumber_temp != '':
                tell_number = int(tnumber_temp)
            cell_number = int(cnumber_temp)
            if fax_temp != '':
                fax_num = int(fax_temp)
            req_ren_year = int(Request_Renewing_Year_temp)
            '''
            if Office_Annual_subscription_temp != '':
                off_annual_sub = float(Office_Annual_subscription_temp)
            if Office_Outstanding_loans_temp != '':
                off_out_loans = float(Office_Outstanding_loans_temp)
            if Other_financial_receivables_temp != '':
                other_financ_rec = float(Other_financial_receivables_temp)
            '''
            File = 'DataBase.db'
            connection = sqlite3.connect(File)
            cursor = connection.cursor()
            cursor.execute("""select * from Office where Classification_Number = ?""", (class_no,))
            find = cursor.fetchone()

            if find == None:
                messagebox.showerror(title='Invalid input', message='please check your classification number')
                return

            elif find[0] != name:
                messagebox.showerror(title='Invalid input', message='please check your office name')
                return
            
            elif find[3] != dat:
                messagebox.showerror(title='Invalid input', message='please check your date of establishemnt')
                return

            elif find[4] != req_ren_year:
                messagebox.showerror(title='Invalid input', message='please check your request renewing year')
                return

            elif find[8] != city_:
                messagebox.showerror(title='Invalid input', message='please check your city/town')
                return
            
            elif find[9] != street_:
                messagebox.showerror(title='Invalid input', message='please check your street/bulding')
                return

            elif find[11] != cell_number:
                messagebox.showerror(title='Invalid input', message='please check your cellalr number')
                return

            elif find[13] != postal_code:
                messagebox.showerror(title='Invalid input', message='please check your postal code')
                return

            elif find[14] != email_:
                messagebox.showerror(title='Invalid input', message='please check your email address')
                return

            if tnumber_temp != '':
                if find[10] != tell_number:
                    messagebox.showerror(title='Invalid input', message='please check your telephone number')
                    return

            if fax_temp != '':
                if find[12] != fax_num:
                    messagebox.showerror(title='Invalid input', message='please check your fax number')
                    return
            
            if Office_Area_temp != '':
                if float(find[15]) != off_area:
                    messagebox.showerror(title='Invalid input', message='please check your office area')
                    return
            #ar c e mh

            cursor.execute("""select Specialization from Specialization_MV where Classification_Number = ?""", (class_no,))
            find = cursor.fetchall()

            specialization = []
            for row in find:
                specialization.append(row[0])

            clickat = []

            if ar.get() == 1:
                clickat.append(ar.cget("text"))

            if c.get() == 1:
                clickat.append(c.cget("text"))

            if e.get() == 1:
                clickat.append(e.cget("text"))

            if mh.get() == 1:
                clickat.append(mh.cget("text"))

            count = 0
            for i in range(len(specialization)):
                count = 0
                for j in range(len(clickat)):
                    if specialization[i]==clickat[j]:
                        break
                    count = count + 1 
                if count == len(clickat):
                    messagebox.showerror(title='Invalid input', message='please check your input')
                    return
            cursor.execute("""select * from ranktemp where Classification_Number = ?""", (class_no,))
            find = cursor.fetchone()
            if find == None:
                cursor.execute("""insert into ranktemp values(?,?,0,0,0,0,0)""", (r,class_no))
                connection.commit()
            print(find)
            root.destroy()
            office_official_three.page()    

    def on_enter(event):
        next_button.invoke()
    next_button = ctk.CTkButton(root, font = font1, text_color='#fff', text = 'Next Page', fg_color='#161C25', hover_color='#FF5002', bg_color='#161C25',border_color='#F15704',border_width=2, cursor = 'hand2', corner_radius=15, width = 260, command = nextFunction)
    next_button.place(x = 630,y = 550)
    next_button.place(x = 1010,y = 450)
    root.bind("<Return>", on_enter)
    def close_window():
        root.destroy()
    #close_button = ctk.CTkButton(root, font = font1, text_color='#fff', text = 'Close', fg_color='#E40404', hover_color='#AE0000', bg_color='#161C25',border_color='#E40404',border_width=2, cursor = 'hand2', corner_radius=15, width = 260,command = close_window)
    #close_button.place(x = 910,y = 550)
    root.mainloop()   