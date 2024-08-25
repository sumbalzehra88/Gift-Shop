from tkinter import Tk, Label,PhotoImage, Frame, Button, Entry
from PIL import Image, ImageTk
from Buttons import back
from products_menu import prd_menu

def open_login_wind(main_wind):
    main_wind.destroy()

    # create a new window when user click on login button
    login_wind = Tk()
    login_wind['background'] = '#F5F5DC'
    login_wind.title('S&K Gift Shop-Login')
    login_wind.geometry('500x550+20+50')


    # set title image
    img = Image.open('GIFT SHOP (4).png')
    img = img.resize((200, 200))
    img1 = ImageTk.PhotoImage(img)

    lab1 = Label(login_wind, image=img1, bg='#F5F5DC')
    lab1.pack(padx=25, pady=25)

    # create a frame to manage other frames
    frame1 = Frame(login_wind, highlightbackground="#800000", bg='#F5F5DC', highlightthickness=2)
    frame1.pack()

    # create frame for username
    frame2 = Frame(frame1, bg='#F5F5DC')
    frame2.pack()

    # create label and entry box for username
    lab2 = Label(frame2, text='Username:',font="Times", bg='#F5F5DC')
    lab2.pack(side='left',padx=10, pady=10)
    entry_username = Entry(frame2, width=30, bg='#F5F5DC')
    entry_username.pack(side='right', padx=10, pady=10)

    error_frame1 = Frame(frame1, bg='#F5F5DC')
    error_frame1.pack()
    empty_name_error_lab = Label(error_frame1, text='Please, enter your name', bg='#F5F5DC', fg='red')

    # create frame for password
    frame3 = Frame(frame1, bg='#F5F5DC')
    frame3.pack()

    # create label and entry box for password
    lab3 = Label(frame3, text='Password:', font="Times",  bg='#F5F5DC')
    lab3.pack(side='left',padx=10, pady=10)
    password_entry = Entry(frame3, width=30,show='*', bg='#F5F5DC')
    password_entry.pack(side='right',padx=10, pady=10)

    error_frame2 = Frame(frame1, bg='#F5F5DC')
    error_frame2.pack()
    empty_pass_error_lab = Label(error_frame2, text='Please, enter your password', bg='#F5F5DC', fg='red')

    error_frame3 = Frame(frame1, bg='#F5F5DC')
    error_frame3.pack()
    invalid_info = Label(error_frame3,text='please enter valid credentials',bg='#F5F5DC',fg='red')

    # create frame for buttons
    frame4 = Frame(frame1, bg='#F5F5DC')
    frame4.pack()

    # create a button if user wants to signup instead of login
    B1 = Button(frame4, text='Back', relief='raised', font="Times",
                command=lambda: back(login_wind), bg='#F5F5DC')
    B1.pack(side='left', padx=10, pady=10)

    # create a button if user wants to step towards next step
    B2 = Button(frame4, text='Next', relief='raised', font="Times",
                command=lambda: retain_info(entry_username, password_entry, empty_name_error_lab, empty_pass_error_lab, invalid_info, login_wind), bg='#F5F5DC')
    B2.pack(side='right', padx=10, pady=10)

    # to run the window
    login_wind.mainloop()


def retain_info(entry_username, password_entry, empty_name_error_lab, empty_pass_error_lab, invalid_info, login_wind):

    username = entry_username.get()
    password = password_entry.get()

    if not username:
        empty_name_error_lab.pack()
        empty_pass_error_lab.pack_forget()  # Hide password error if shown
        return False
    elif not password:
        empty_pass_error_lab.pack()
        empty_name_error_lab.pack_forget()  # Hide username error if shown
        return False
    else:
        authentication = False  # Initialize authentication
        with open('user_history.txt', 'r') as file:
            # Read all user records from history
            user_records = [line.strip().split(",") for line in file]

            for record in user_records:
                if username == record[0] and password == record[1].strip():  # Compare values, not widgets
                    authentication = True
                    prd_menu(username, login_wind)
                    break

            if not authentication:
                invalid_info.pack()
                empty_pass_error_lab.pack_forget()  # Hide password error if shown

# open_login_wind('window')
