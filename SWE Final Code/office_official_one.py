import tkinter as tk
import customtkinter as ct
import office_official_two
from Dictionary import Word
from tkinter import messagebox
from datetime import date
import sqlite3
def page():
    rootWindow = ct.CTk()
    window_width = 777
    window_height = 600
    screen_width = rootWindow.winfo_screenwidth()
    screen_height = rootWindow.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    rootWindow.geometry(f"{window_width}x{window_height}+{x_position}+{y_position - 15}")
    rootWindow.config(bg='#161C25')
    def callPage():
        File = 'DataBase.db'
        connection = sqlite3.connect(File)
        cursor = connection.cursor()
        user_id = Word["User_ID"]
        cursor.execute(""" select Classification_Number from Office_Login where Login_ID = ?""" , (user_id,))
        find = cursor.fetchone()
        Word["classification_num"] = find[0]
        cursor.execute(""" select * from ranktemp where Classification_Number = ?""" , (find[0],))
        find = cursor.fetchone()
        
        if find == None:
            rootWindow.destroy()
            office_official_two.page()  
        
        elif find[6] == 1:
            cursor.execute(""" select Session_Number from Office_Final where Classification_Number = ?""" , (find[1],))
            session_num = cursor.fetchone()
            
            cursor.execute(""" select Session_Date from Final_Decision where Session_Number = ?""" , (session_num[0],))
            session_date = cursor.fetchone()
            date_string = session_date[0]
            day, month, year = date_string.split("-")
            year = str(int(year) + 1)
            today_date = date.today()
            day2, month2, year2 = date_string.split("-")
            if day == day2 and month == month2 and year == year2:
                cursor.execute(""" DELETE from ranktemp where Classification_Number = ?""" , (find[0],))
                connection.commit()
                connection.close()
                rootWindow.destroy()
                office_official_two.page()
            else:
                date_next = '' + year + '-' +  month + '-' + day
                messagebox.showerror(title='Access denied', message=f'You must wait until one year has passed since the time of the previous application {date_next}' )
                return

        elif find[3] == -1:
            cursor.execute(""" DELETE from ranktemp where Classification_Number = ?""" , (find[0],))
            messagebox.showerror(title='Request Rejected', message='You must check the financial matters of your office or employees and then re-enter the request' )
            connection.commit()
            connection.close()
            rootWindow.destroy()
            office_official_two.page()
        elif find[4] == -1:
            cursor.execute(""" DELETE from ranktemp where Classification_Number = ?""" , (find[0],))
            messagebox.showerror(title='Request Rejected', message='You must verify the office information entered')
            connection.commit()
            connection.close()
            rootWindow.destroy()
            office_official_two.page()
        elif find[5] == -1:
            cursor.execute(""" DELETE from ranktemp where Classification_Number = ?""" , (find[0],))
            messagebox.showerror(title='Request Rejected', message='You must verify the information of the office and engineers so that it meets the requirements for the desired classification' )
            connection.commit()
            connection.close()
            rootWindow.destroy()
            office_official_two.page()
        elif find[6] == -1:
            cursor.execute(""" DELETE from ranktemp where Classification_Number = ?""" , (find[0],))
            messagebox.showerror(title='Request Rejected', message='the council authority does not approve the request Check all the request information.' )
            connection.commit()
            connection.close()
            rootWindow.destroy()
            office_official_two.page()
        elif find[2] == 0 or find[2] == 1:
            messagebox.showerror(title='Access denied', message='Your request still being processed.')
            return

    font1 = ("Arial", 20, "bold")
    font2 = ("Arial", 12, "bold")
    #===============
    
    userNameLabel = ct.CTkLabel(rootWindow,text="User Name: ",font=font1, text_color="yellow", bg_color="#161C25")
    userNameLabel.place(x=40,y=40)
    
    name = Word["User_Name"]
    userNameansEntry = ct.CTkLabel(rootWindow,text=name,font=font1, text_color="red", bg_color="#161C25" )
    userNameansEntry.place(x = 160, y = 40)
    #===============
    
    userIDLabel = ct.CTkLabel(rootWindow,text="User Class: ",font=font1, text_color="yellow", bg_color="#161C25")
    userIDLabel.place(x=450,y=40)
    
    classs = Word["User_Class"]
    userIDLabelansLabel = ct.CTkLabel(rootWindow,text=classs,font=font1, text_color="red", bg_color="#161C25")
    userIDLabelansLabel.place(x = 570, y = 40)

    #================
    x = ["Request Renwing Form", "Add an Enginner Form"]

    requestsLabel = ct.CTkLabel(rootWindow,text="Services:",font=font1, text_color="yellow", bg_color="#161C25" )
    requestsLabel.place(x = 40, y = 160)

    i = 0
    column = 250
    officeNameLabel = ct.CTkLabel(rootWindow,text=x[i],font=font1, text_color="#fff", bg_color="#161C25" )
    officeNameLabel.place(x = 40, y = column)
    checkButton = ct.CTkButton(rootWindow,font=font1, text_color="white", text="Open", fg_color="#ff0000", hover_color="#00850B" , bg_color="#161C25" , cursor = "hand2", corner_radius=15, width=160, command = callPage)
    checkButton.place(x = 600, y = column)
    column += 80
    i = i + 1
    officeNameLabe2 = ct.CTkLabel(rootWindow,text=x[i],font=font1, text_color="#fff", bg_color="#161C25" )
    officeNameLabe2.place(x = 40, y = column)
    checkButton2 = ct.CTkButton(rootWindow,font=font1, text_color="white", text="coming\nsoon", fg_color="black", hover_color="#00850B" , bg_color="#161C25" , cursor = "hand2", corner_radius=15, width=160)
    checkButton2.place(x = 600, y = column)
    checkButton2.configure(state="disabled") 
    
    rootWindow.mainloop()