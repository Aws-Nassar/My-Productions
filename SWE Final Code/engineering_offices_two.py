import customtkinter as ctk
import sqlite3
from Dictionary import Word
import engineering_offices_one


def page():
    class_no = Word["classification_num"]
    File = 'DataBase.db'
    connection = sqlite3.connect(File)
    cursor = connection.cursor()

    def accept():
        def yes():
            class_no = Word["classification_num"]
            File = 'DataBase.db'
            connection = sqlite3.connect(File)
            cursor = connection.cursor()
            cursor.execute("""UPDATE ranktemp SET engineering_offices_flag = 1, ainancial_affairs_flag = 0 where Classification_Number = ?""", (class_no,))
            connection.commit()
            connection.close()
            acceptPage.destroy()
            rootPage.destroy()
            engineering_offices_one.page()

        def no():
            acceptPage.destroy()

        acceptPage = ctk.CTk()
        acceptPage.geometry("600x200+350+200")
        acceptPage.config(bg="#161C25")
        acceptPage.resizable(False,False)
     
        label = ctk.CTkLabel(acceptPage, text=f"do you want to accept this?", font=font,
                                text_color="yellow", bg_color="#161C25") 
        label.place(x = 150,y = 50)
   
        #======
        yesButton = ctk.CTkButton(acceptPage, font=font, text_color="#fff", text="Yes", fg_color="#05A312",
                                   hover_color="#00850B", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command=yes)
        yesButton.place(x = 200,y = 140)

        noButton = ctk.CTkButton(acceptPage, font=font, text_color="#fff", text="No", fg_color="red",
                                   hover_color="#AE0000", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command=no)
        noButton.place(x = 400,y = 140)

 
        acceptPage.mainloop()

    def reject():
        def yes():
            class_no = Word["classification_num"]
            File = 'DataBase.db'
            connection = sqlite3.connect(File)
            cursor = connection.cursor()
            cursor.execute("""UPDATE ranktemp SET engineering_offices_flag = -1, ainancial_affairs_flag = 0 where Classification_Number = ?""", (class_no,))
            connection.commit()
            connection.close()
            rejectPage.destroy()
            rootPage.destroy()
            engineering_offices_one.page() 
            
        def no():
            rejectPage.destroy()

        rejectPage = ctk.CTk()
        rejectPage.geometry("600x200+350+200")
        rejectPage.config(bg="#161C25")
        rejectPage.resizable(False,False)
     
        label = ctk.CTkLabel(rejectPage, text=f"do you want to reject this?", font=font,
                                text_color="yellow", bg_color="#161C25") 
        label.place(x = 150,y = 50)
   
        #======
        yesButton = ctk.CTkButton(rejectPage, font=font, text_color="#fff", text="Yes", fg_color="#05A312",
                                   hover_color="#00850B", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command=yes)
        yesButton.place(x = 200,y = 140)

        noButton = ctk.CTkButton(rejectPage, font=font, text_color="#fff", text="No", fg_color="red",
                                   hover_color="#AE0000", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command=no)
        noButton.place(x = 400,y = 140)

 
        rejectPage.mainloop()    
     

    rootPage = ctk.CTk()
    rootPage.title("The Director of the Engineering Offices Department(2)")
    window_width = 1000
    window_height = 600
    screen_width = rootPage.winfo_screenwidth()
    screen_height = rootPage.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    rootPage.geometry(f"{window_width}x{window_height}+{x_position}+{y_position-5}")
    rootPage.config(bg="#161C25")
    rootPage.resizable(False,False)
    font = ("Arial", 20, "bold")

    cursor.execute("""select * from Office where Classification_Number = ?""", (class_no,))
    find = cursor.fetchone()

    officeNameLabel = ctk.CTkLabel(rootPage,text="Office Name: ",font=font, text_color="yellow", bg_color="#161C25" )
    officeNameLabel.place(x = 40, y = 40)
    nameLabel = ctk.CTkLabel(rootPage,text=find[0],font=font, text_color="white", bg_color="#161C25" )
    nameLabel.place(x = 170, y = 40)
    #---------
    classificationNumberLabel = ctk.CTkLabel(rootPage,text="Classification Number: ",font=font, text_color="yellow", bg_color="#161C25" )
    classificationNumberLabel.place(x = 530, y = 40)
    numberLabel = ctk.CTkLabel(rootPage,text=class_no,font=font, text_color="white", bg_color="#161C25" )
    numberLabel.place(x = 750, y = 40)

    
    
    nameLabel = ctk.CTkLabel(rootPage, text=f"Name ", font=font,
                                text_color="yellow", bg_color="#161C25")
    nameLabel.place(x = 165, y = 100)

    graduationYearLabel = ctk.CTkLabel(rootPage, text=f"Graduation Year ", font=font,
                                 text_color="yellow", bg_color="#161C25")
    graduationYearLabel.place(x = 435, y = 100)

    specializationLabel = ctk.CTkLabel(rootPage, text=f"Specialization ", font=font,
                                 text_color="yellow", bg_color="#161C25")
    specializationLabel.place(x = 675, y = 100) 

    # Create a scrollable frame
    scrollable_frame = ctk.CTkScrollableFrame(rootPage, bg_color="#161C25", fg_color="#161C25", height=360, width=900)
    scrollable_frame.place(x=50, y=130)

    #=======
    cursor.execute("""select * from Engineers where Classification_Number = ?""", (class_no,))
    find = cursor.fetchall()
    i = 0  
    for row in find:
        name = row[1] + ' ' + row[2] + ' ' + row[3]
        nameLabel = ctk.CTkLabel(scrollable_frame, text=name, font=font,
                                text_color="white", bg_color="#161C25")
        nameLabel.grid(row=i, column=1, pady=30, padx=20)  # Increased vertical and horizontal padding

        year = row[5]

        graduationYearLabel = ctk.CTkLabel(scrollable_frame, text=year, font=font,
                                text_color="white", bg_color="#161C25")
        graduationYearLabel.grid(row=i, column=2, pady=30, padx=150) 

        specialization = row[4]

        specializationLabel = ctk.CTkLabel(scrollable_frame, text=specialization, font=font,
                                text_color="white", bg_color="#161C25")
        specializationLabel.grid(row=i, column=3, pady=30, padx=5)
        i = i+1

    #=======
    acceptButton = ctk.CTkButton(rootPage, font=font, text_color="#fff", text="Accept", fg_color="#05A312",
                                   hover_color="#00850B", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command=accept)
    acceptButton.place(x = 500,y = 530)

    rejectButton = ctk.CTkButton(rootPage, font=font, text_color="#fff", text="Reject", fg_color="red",
                                   hover_color="#AE0000", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command=reject)
    rejectButton.place(x = 700,y = 530)

        
    rootPage.mainloop()    
        