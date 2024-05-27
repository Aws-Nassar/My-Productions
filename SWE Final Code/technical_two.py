import customtkinter as ctk
import sqlite3
from Dictionary import Word
import technical_one

def page():
    class_no = Word["classification_num"]
    File = 'DataBase.db'
    connection = sqlite3.connect(File)
    cursor = connection.cursor()
  
    def accept():
        def yes():
            class_no = Word["classification_num"]
            cursor.execute("""UPDATE ranktemp SET technical_affairs_offices = 1, engineering_offices_flag = 0 where Classification_Number = ?""", (class_no,))
            connection.commit()
            connection.close()
            acceptPage.destroy()
            rootPage.destroy()
            technical_one.page()

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
            cursor.execute("""UPDATE ranktemp SET technical_affairs_offices = -1, engineering_offices_flag = 0 where Classification_Number = ?""", (class_no,))
            connection.commit()
            connection.close()
            rejectPage.destroy()
            rootPage.destroy()
            technical_one.page() 
            
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
    rootPage.title("The Director of Technical Affairs(2)")
    window_width = 1000
    window_height = 700
    screen_width = rootPage.winfo_screenwidth()
    screen_height = rootPage.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    rootPage.geometry(f"{window_width}x{window_height-15}+{x_position}+{y_position-30}")
    rootPage.config(bg="#161C25")
    rootPage.resizable(False, False)
    font = ("Arial", 20, "bold")

    cursor.execute("""select * from Office where Classification_Number = ?""", (class_no,))
    find = cursor.fetchone()
    
    cursor.execute("""select Specialization from Specialization_MV where Classification_Number = ?""", (class_no,))
    specials = cursor.fetchall()
    specials_text = ''
    specials_text = ''
    for row in specials:
        specials_text += row[0] + '\n '

    #specials_text = specials_text.rstrip(', ')

    cursor.execute("""select enteredRank from ranktemp where Classification_Number = ?""", (class_no,))
    new_rank = cursor.fetchone()

    officeNameLabel = ctk.CTkLabel(rootPage, text="Office name:", font=font, text_color="yellow", bg_color="#161C25")
    officeNameLabel.place(x=40, y=40)

    officeName = ctk.CTkLabel(rootPage, text=find[0], font=font, text_color="white", bg_color="#161C25")
    officeName.place(x=170, y=40)   

    classficationNumberLabel = ctk.CTkLabel(rootPage, text="Classification number:", font=font, text_color="yellow", bg_color="#161C25")
    classficationNumberLabel.place(x=520, y=40)

    classficationNumber = ctk.CTkLabel(rootPage, text=class_no, font=font, text_color="white", bg_color="#161C25")
    classficationNumber.place(x=740, y=40)

    dateOfEstablishmentLabel = ctk.CTkLabel(rootPage, text="Date of establishment:", font=font, text_color="yellow", bg_color="#161C25")
    dateOfEstablishmentLabel.place(x=40, y=130)

    dateOfEstablishment = ctk.CTkLabel(rootPage, text=find[3], font=font, text_color="white", bg_color="#161C25")
    dateOfEstablishment.place(x=260, y=130)

    officeSpecializationLabel = ctk.CTkLabel(rootPage, text="Office specialization/s:", font=font, text_color="yellow", bg_color="#161C25")
    officeSpecializationLabel.place(x=520, y=130)

    officeSpecialization = ctk.CTkLabel(rootPage, text=specials_text, font=font, text_color="white", bg_color="#161C25")
    officeSpecialization.place(x=740, y=130)

    currentRankLabel = ctk.CTkLabel(rootPage, text="Current rank:", font=font, text_color="yellow", bg_color="#161C25")
    currentRankLabel.place(x=40, y=220)

    currentRank = ctk.CTkLabel(rootPage, text=find[2], font=font, text_color="white", bg_color="#161C25")
    currentRank.place(x=180, y=220)

    newRankLabel = ctk.CTkLabel(rootPage, text="New rank:", font=font, text_color="yellow", bg_color="#161C25")
    newRankLabel.place(x=520, y=220)

    currentRank = ctk.CTkLabel(rootPage, text=new_rank[0], font=font, text_color="white", bg_color="#161C25")
    currentRank.place(x=620, y=220)
    #===============

    dataLabel = ctk.CTkLabel(rootPage, text="Information about heads of specialities:", font=font, text_color="yellow", bg_color="#161C25")
    dataLabel.place(x=270, y=300)

    scrollable_frame = ctk.CTkScrollableFrame(rootPage, bg_color="#161C25", fg_color="#161C25", height=200, width=920)
    scrollable_frame.place(x=20, y=400)

    competenceLabel = ctk.CTkLabel(rootPage, text="Engineer Name", font=font,
                                text_color="yellow", bg_color="#161C25")
    competenceLabel.place(x = 90, y = 360)  # Increased vertical and horizontal padding

    yearsOfExperienceLabel = ctk.CTkLabel(rootPage, text=f"Graduation year", font=font,
                                 text_color="yellow", bg_color="#161C25")
    yearsOfExperienceLabel.place(x = 390, y = 360)

    spetializationLabel = ctk.CTkLabel(rootPage, text=f"Spetialization", font=font,
                                 text_color="yellow", bg_color="#161C25")
    spetializationLabel.place(x = 620, y = 360)
    
    cursor.execute("""select * from Engineers where Classification_Number  = ? AND Job_title = 'Head of speciality'""", (class_no,))
    find = cursor.fetchall()
    i = 0  
    for row in find:
        name = row[1] + ' ' + row[2] + ' ' + row[3]
        year = row[5]
        specialization = row[4]
        competenceLabel = ctk.CTkLabel(scrollable_frame, text=name, font=font,
                                text_color="white", bg_color="#161C25")
        competenceLabel.grid(row=i, column=1, pady=30, padx=40)  # Increased vertical and horizontal padding

        yearsOfExperienceLabel = ctk.CTkLabel(scrollable_frame, text=year, font=font,
                                text_color="white", bg_color="#161C25")
        yearsOfExperienceLabel.grid(row=i, column=2, pady=30, padx=140) 

        spetializationLabel = ctk.CTkLabel(scrollable_frame, text=specialization, font=font,
                                text_color="white", bg_color="#161C25")
        spetializationLabel.grid(row=i, column=3, pady=30, padx=10)
        i = i + 1 

    acceptButton = ctk.CTkButton(rootPage, font=font, text_color="#fff", text="Accept", fg_color="#05A312",
                                   hover_color="#00850B", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command=accept)
    acceptButton.place(x = 500,y = 650)

    rejectButton = ctk.CTkButton(rootPage, font=font, text_color="#fff", text="Reject", fg_color="red",
                                   hover_color="#AE0000", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command=reject)
    rejectButton.place(x = 700,y = 650) 


    rootPage.mainloop()