import customtkinter as ctk
from datetime import date
import sqlite3
from Dictionary import Word
import council_one

def page():
    class_no = Word["classification_num"]
    File = 'DataBase.db'
    connection = sqlite3.connect(File)
    cursor = connection.cursor()

    def accept():
        def yes():
            class_no = Word["classification_num"]
            user_name = Word["User_Name"]
            current_date = date.today()
            cursor.execute("""UPDATE ranktemp SET council_flag = 1, technical_affairs_offices = 0  where Classification_Number = ?""", (class_no,))
            connection.commit()
            cursor.execute("""select * from Final_Decision""")
            find = cursor.fetchall()
            final_decision = "Approved"

            if len(find) == 0:
                session_num = 10005
            else:
                session_num = 0
                for row in find:
                    session_num = row[0]
                session_num = session_num + 1

            cursor.execute("""insert into Final_Decision values(?,?,?,?)""",(session_num,current_date,final_decision,user_name,))
            connection.commit()
            cursor.execute("""insert into Office_Final values(?,?)""",(session_num,class_no,))
            connection.commit()
            connection.close()
            acceptPage.destroy()
            rootPage.destroy()
            council_one.page()

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
                                   width=160,command = yes)
        yesButton.place(x = 200,y = 140)

        noButton = ctk.CTkButton(acceptPage, font=font, text_color="#fff", text="No", fg_color="red",
                                   hover_color="#AE0000", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command = no)
        noButton.place(x = 400,y = 140)

 
        acceptPage.mainloop()

    def reject():
        def yes():
            class_no = Word["classification_num"]
            user_name = Word["User_Name"]
            current_date = date.today()
            cursor.execute("""UPDATE ranktemp SET council_flag = -1, technical_affairs_offices = 0  where Classification_Number = ?""", (class_no,))
            connection.commit()
            cursor.execute("""select * from Final_Decision""")
            find = cursor.fetchall()
            final_decision = "Not approved"

            if len(find) == 0:
                session_num = 10005
            else:
                session_num = 0
                for row in find:
                    session_num = row[0]
                session_num = session_num + 1

            cursor.execute("""insert into Final_Decision values(?,?,?,?)""",(session_num,current_date,final_decision,user_name,))
            connection.commit()
            cursor.execute("""insert into Office_Final values(?,?)""",(session_num,class_no,))
            connection.commit()
            connection.close()
            rejectPage.destroy()
            rootPage.destroy()
            council_one.page()

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
                                   width=160,command = yes)
        yesButton.place(x = 200,y = 140)

        noButton = ctk.CTkButton(rejectPage, font=font, text_color="#fff", text="No", fg_color="red",
                                   hover_color="#AE0000", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command = no)
        noButton.place(x = 400,y = 140)

 
        rejectPage.mainloop()

    rootPage = ctk.CTk()
    rootPage.title("The Council of Engineering Offices and Companies Authority(2)")
    window_width = 1000
    window_height = 450
    screen_width = rootPage.winfo_screenwidth()
    screen_height = rootPage.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    rootPage.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    rootPage.config(bg="#161C25")
    rootPage.resizable(False, False)
    font = ("Arial", 20, "bold")

    cursor.execute("""select * from Office where Classification_Number = ?""", (class_no,))
    find = cursor.fetchone()
    
    cursor.execute("""select enteredRank from ranktemp where Classification_Number = ?""", (class_no,))
    new_rank = cursor.fetchone()

    cursor.execute("""select Specialization from Specialization_MV where Classification_Number = ?""", (class_no,))
    specials = cursor.fetchall()
    specials_text = ''
    specials_text = ''
    for row in specials:
        specials_text += row[0] + '\n '

    officeNameLabel = ctk.CTkLabel(rootPage, text=f"Office name :", font=font,text_color="yellow", bg_color="#161C25")
    officeNameLabel.place(x = 40, y = 40)  

    officeNameText = ctk.CTkLabel(rootPage, text=find[0], font=font,text_color="white", bg_color="#161C25")
    officeNameText.place(x = 200, y = 40) 

    classificationNumberLabel = ctk.CTkLabel(rootPage, text=f"Classification number :", font=font,text_color="yellow", bg_color="#161C25")
    classificationNumberLabel.place(x = 550, y = 40) 

    classificationNumberText = ctk.CTkLabel(rootPage, text=class_no, font=font,text_color="white", bg_color="#161C25")
    classificationNumberText.place(x = 800, y = 40) 

    currentRankLabel = ctk.CTkLabel(rootPage, text=f"Current rank :", font=font,text_color="yellow", bg_color="#161C25")
    currentRankLabel.place(x = 40, y = 130) 

    currentRankText = ctk.CTkLabel(rootPage, text=find[2], font=font,text_color="white", bg_color="#161C25")
    currentRankText.place(x = 200, y = 130) 
 

    establishmentLabel = ctk.CTkLabel(rootPage, text="Date of establishment :", font=font,text_color="yellow", bg_color="#161C25")
    establishmentLabel.place(x = 550, y = 130)

    establishmentText = ctk.CTkLabel(rootPage, text=find[3], font=font,text_color="white", bg_color="#161C25")
    establishmentText.place(x = 800, y = 130) 


    NewRankLabel = ctk.CTkLabel(rootPage, text=f"New rank :", font=font,text_color="yellow", bg_color="#161C25")
    NewRankLabel.place(x = 40, y = 220)

    NewRankText = ctk.CTkLabel(rootPage, text=new_rank[0], font=font,text_color="white", bg_color="#161C25")
    NewRankText.place(x = 200, y = 220) 

    specializationLabel = ctk.CTkLabel(rootPage, text="Specialization/s :", font=font,text_color="yellow", bg_color="#161C25")
    specializationLabel.place(x = 550, y = 220)

    specializationText = ctk.CTkLabel(rootPage, text=specials_text, font=font,text_color="white", bg_color="#161C25")
    specializationText.place(x = 720, y = 220) 


    #=================

    acceptButton = ctk.CTkButton(rootPage, font=font, text_color="#fff", text="Accept", fg_color="#05A312",
                                   hover_color="#00850B", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command=accept)
    acceptButton.place(x = 620,y = 400)

    rejectButton = ctk.CTkButton(rootPage, font=font, text_color="#fff", text="Reject", fg_color="red",
                                   hover_color="#AE0000", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                   width=160,command=reject)
    rejectButton.place(x = 820,y = 400)

    rootPage.mainloop()    


    