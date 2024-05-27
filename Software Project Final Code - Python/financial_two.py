import tkinter as tk
import customtkinter as ct
import sqlite3
from Dictionary import Word
import financial_one

def page():
    def show():
        #=======================
        class_no = Word["classification_num"]
        File = 'DataBase.db'
        connection = sqlite3.connect(File)
        cursor = connection.cursor()
        cursor.execute("""select * from Office where Classification_Number = ?""", (class_no,))
        find = cursor.fetchone()

        officeAnnualSubscriptionLabel = ct.CTkLabel(rootWindow,font=font1, text = '1.Office Annual Subscription', text_color="yellow", bg_color="#161C25") 
        officeAnnualSubscriptionLabel.place(x=20,y=300)

        if find[5] == 0:
            out = "The office paid the annual subscription"

        else: 
            out = "The office has an annual subscription = "
            out = out + find[5]

        officeAnnualSubscriptionLabe2 = ct.CTkLabel(rootWindow,font=font1, text = out, text_color="white", bg_color="#161C25") 
        officeAnnualSubscriptionLabe2.place(x=20,y=340)

        #================

        officeOutstandingLoansLabel = ct.CTkLabel(rootWindow,font=font1, text = '2. Office Outstanding Loans', text_color="yellow", bg_color="#161C25") 
        officeOutstandingLoansLabel.place(x=20,y=380)

        if find[6] == 0:
            out = "The office has no outstanding loans"

        else: 
            out = "The office has an outstanding loans = "
            out = out + find[6]

        officeOutstandingLoans = ct.CTkLabel(rootWindow,font=font1, text = out, text_color="white", bg_color="#161C25") 
        officeOutstandingLoans.place(x=20,y=420)

        #================

        officeFinancialReceivablesLabel = ct.CTkLabel(rootWindow,font=font1, text = '3.Office Financial Receivables', text_color="yellow", bg_color="#161C25") 
        officeFinancialReceivablesLabel.place(x=20,y=460)

        if find[7] == 0:
            out = "The office has no other financial receivables"

        else: 
            out = "The office has other financial receivables = "
            out = out + find[7]

        officeFinancialReceivables = ct.CTkLabel(rootWindow,font=font1, text = out, text_color="white", bg_color="#161C25") 
        officeFinancialReceivables.place(x=20,y=500)

        #================

        engineersAnnualSubscriptLabel = ct.CTkLabel(rootWindow,font=font1, text = "4.Engineers financial information", text_color="yellow", bg_color="#161C25") 
        engineersAnnualSubscriptLabel.place(x=480,y=300)

        scroll_frame = ct.CTkScrollableFrame(rootWindow, bg_color="#161C25", fg_color="#161C25", height=150, width=600)
        scroll_frame.place(x=440, y=340)

        cursor.execute("""select * from Engineers where Classification_Number = ?""", (class_no,))
        find = cursor.fetchall()
        i = 0  
        for row in find:
            if row[6] == 0 and row[7] == 0:
                out = "has no financial dues"

            else: 
                out = "has financial dues = "
                value = row[6] + row[7]
                out = out + value
            
            name = row[1] + ' ' + row[2] + ' ' + row[3]
            reqLabel = ct.CTkLabel(scroll_frame, text= name, font=font1,
                                text_color="white", bg_color="#161C25")
            reqLabel.grid(row=i, column=1, pady=30, padx=40) 
                 
            label = ct.CTkLabel(scroll_frame, text= out, font=font1,
                                text_color="white", bg_color="#161C25")
            label.grid(row=i, column=2, pady=30, padx=40) # Increased vertical and horizontal padding
            i = i + 1  

        
    def accept():
        def yes():
            acceptWindow.destroy()
            rootWindow.destroy()
            File = 'DataBase.db'
            connection = sqlite3.connect(File)
            cursor = connection.cursor()
            cursor.execute("""UPDATE ranktemp SET ainancial_affairs_flag = 1, office_official_flag = 0 where Classification_Number = ?""", (class_no,))
            connection.commit()
            connection.close()
            financial_one.page()

        def no():
            acceptWindow.destroy()   
        
        acceptWindow = ct.CTk()
        acceptWindow.geometry("600x200+350+200")
        acceptWindow.config(bg='#161C25')
        acceptWindow.resizable(False,False)
        #========
        acceptLabel = ct.CTkLabel(acceptWindow,font=font1, text = 'are you sure you have accept this?', text_color="#fff", bg_color="#161C25")
        acceptLabel.place(x = 150,y = 50)
        #==========
        yesButton = ct.CTkButton(acceptWindow,font=font1, text="Yes", text_color="#fff",  fg_color="#05A312", hover_color="#00850B" , bg_color="#161C25" , border_width=2, border_color="#E40404",cursor = "hand2", corner_radius=15, width=160, command= yes)
        yesButton.place(x = 200,y = 140)

        noButton = ct.CTkButton(acceptWindow,font=font1, text="No", text_color="#fff",  fg_color="#E40404", hover_color="#AE0000" , bg_color="#161C25" , border_width=2, border_color="#E40404",cursor = "hand2", corner_radius=15, width=160, command= no)
        noButton.place(x = 400,y = 140)

        acceptWindow.mainloop()  
    def refucce():
        def yes():
            refucceWindow.destroy()
            rootWindow.destroy()
            File = 'DataBase.db'
            connection = sqlite3.connect(File)
            cursor = connection.cursor()
            cursor.execute("""UPDATE ranktemp SET ainancial_affairs_flag = -1, office_official_flag = 0 where Classification_Number = ?""", (class_no,))
            connection.commit()
            connection.close()
            financial_one.page()
            
        def no():
            refucceWindow.destroy()

        refucceWindow = ct.CTk()
        refucceWindow.geometry("600x200+350+200")
        refucceWindow.config(bg='#161C25') # give a background color to window
        refucceWindow.resizable(False,False)
        #========
        acceptLabel = ct.CTkLabel(refucceWindow,font=font1, text = 'are you sure you have refucce this?', text_color="#fff", bg_color="#161C25")
        acceptLabel.place(x = 150,y = 50)
        #==========
        yesButton = ct.CTkButton(refucceWindow,font=font1, text="Yes", text_color="#fff",  fg_color="#05A312", hover_color="#00850B" , bg_color="#161C25" , border_width=2, border_color="#E40404",cursor = "hand2", corner_radius=15, width=160, command= yes)
        yesButton.place(x = 200,y = 140)

        noButton = ct.CTkButton(refucceWindow,font=font1, text="No", text_color="#fff",  fg_color="#E40404", hover_color="#AE0000" , bg_color="#161C25" , border_width=2, border_color="#E40404",cursor = "hand2", corner_radius=15, width=160, command= no)
        noButton.place(x = 400,y = 140)

        refucceWindow.mainloop()

    rootWindow = ct.CTk()
    rootWindow.title("The Director of the Financial Affairs Department(2)")
    #rootWindow.geometry('1100x655 + 150 + -10') # give a size to window
    window_width = 1100
    window_height = 655
    screen_width = rootWindow.winfo_screenwidth()
    screen_height = rootWindow.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    rootWindow.geometry(f"{window_width}x{window_height}+{x_position}+{y_position-30}")
    rootWindow.config(bg='#161C25') # give a background color to window
    rootWindow.resizable(True,True) # can't resize the window 
    font1 = ("Arial", 20, "bold")


    #=====================

    class_no = Word["classification_num"]
    File = 'DataBase.db'
    connection = sqlite3.connect(File)
    cursor = connection.cursor()
    cursor.execute("""select * from Office where Classification_Number = ?""", (class_no,))
    find = cursor.fetchone()

    officeNameLabel = ct.CTkLabel(rootWindow,font=font1, text = 'Office name: ', text_color="yellow", bg_color="#161C25") 
    officeNameLabel.place(x=20,y=80)
    officeName = ct.CTkLabel(rootWindow,font=font1, text = find[0], text_color="white", bg_color="#161C25") 
    officeName.place(x=148,y = 80)
    #===================
    officeClassificationLabel = ct.CTkLabel(rootWindow,font=font1, text = 'Classification: ', text_color="yellow", bg_color="#161C25") 
    officeClassificationLabel.place(x=520,y=80)

    officeClassification = ct.CTkLabel(rootWindow,font=font1, text = class_no, text_color="white", bg_color="#161C25") 
    officeClassification.place(x=660,y = 80)
    #====================

    showButton = ct.CTkButton(rootWindow,font=font1, text_color="#fff", text="Show", fg_color="#05A312", hover_color="#00850B" , bg_color="#161C25" , cursor = "hand2", corner_radius=15, width=260, command=show) # creat a button
    showButton.place(x = 20, y = 180)

    #================

    acceptButton = ct.CTkButton(rootWindow,font=font1, text_color="#fff", text="Accept", fg_color="#05A312", hover_color="#00850B" , bg_color="#161C25" , cursor = "hand2", corner_radius=15, width=160, command=accept)
    acceptButton.place(x = 370, y = 620)

    refucceButton = ct.CTkButton(rootWindow,font=font1, text_color="#fff", text="Refucce", fg_color="#E40404", hover_color="#AE0000" , bg_color="#161C25" , border_width=2, border_color="#E40404",cursor = "hand2", corner_radius=15, width=160, command= refucce)
    refucceButton.place(x = 560, y = 620)


    rootWindow.mainloop()