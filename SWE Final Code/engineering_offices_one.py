import customtkinter as ctk
import sqlite3
from Dictionary import Word
import engineering_offices_two


def page():
    
    list = []
    rootPage = ctk.CTk()
    rootPage.title("The Director of the Engineering Offices Department(1)")
    window_width = 700
    window_height = 495
    screen_width = rootPage.winfo_screenwidth()
    screen_height = rootPage.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    rootPage.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    rootPage.config(bg="#161C25")
    rootPage.resizable(False, False)

    # Create a scrollable frame
    scrollable_frame = ctk.CTkScrollableFrame(rootPage, bg_color="#161C25", fg_color="#161C25", height=300, width=600)
    scrollable_frame.place(x=50, y=100)

    font = ("Arial", 20, "bold")
    requsetsLabel = ctk.CTkLabel(rootPage, text="Requests:", font=font, text_color="yellow", bg_color="#161C25")
    requsetsLabel.place(x=260, y=40)

    def open_page(index):

        Class_Number = list[index]
        Word["classification_num"] =  Class_Number
        rootPage.destroy()
        engineering_offices_two.page()


    File = 'DataBase.db'
    connection = sqlite3.connect(File)
    cursor = connection.cursor()
    cursor.execute(""" select ainancial_affairs_flag, Classification_Number from ranktemp""")
    results = cursor.fetchall()
    i = 0

    if results != None:
        for row in results:
            if row[0] == 1:
                reqLabel = ctk.CTkLabel(scrollable_frame, text=f"Request {i+1}:", font=font, text_color="yellow", bg_color="#161C25")
                reqLabel.grid(row=i, column=1, pady=30, padx=40)  # Increased vertical and horizontal padding 
                openButton = ctk.CTkButton(scrollable_frame, font=font, text_color="#fff", text="Open", fg_color="#05A312",
                                       hover_color="#00850B", bg_color="#161C25", cursor="hand2", corner_radius=15,
                                       width=160, command=lambda index=i: open_page(index))  # Pass index as argument
                openButton.grid(row=i, column=2, pady=30, padx=200)  # Increased vertical and horizontal padding
                list.append(row[1])
                i = i + 1
    rootPage.mainloop()
#page()