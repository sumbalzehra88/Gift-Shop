from tkinter import Tk,Toplevel, Entry, Frame, Label, Button, Radiobutton, StringVar, messagebox, PhotoImage


def handle_update(selected_option, update_wind):
    """Handle updating user credentials based on the selected option."""
    if selected_option == 'password':
        # Hide the main update window
        update_wind.withdraw()

        # Create a new window for updating password
        update_pass_wind = Toplevel(update_wind)
        update_pass_wind['background'] = '#F5F5DC'
        update_pass_wind.title('S&K Gift Shop - Update Password')
        update_pass_wind.geometry('300x350+350+100')

        update_wind.grab_set()

        # Create frames for layout
        frame = Frame(update_pass_wind, bg='#F5F5DC')
        frame.pack(expand=True)

        Frame1 = Frame(frame, bg='#F5F5DC')
        Frame1.pack(pady=15, padx=10)
        L1 = Label(Frame1, text='Username: ', font=("Times", 14), bg='#F5F5DC')
        L1.pack(side='left')
        E1 = Entry(Frame1, bg='#F5F5DC')
        E1.pack(side='left')

        Frame2 = Frame(frame, bg='#F5F5DC')
        Frame2.pack(pady=15, padx=10)
        L2 = Label(Frame2, text='Password: ', font=("Times", 14), bg='#F5F5DC')
        L2.pack(side='left')
        E2 = Entry(Frame2, bg='#F5F5DC', show='*')
        E2.pack(side='left')

        Frame3 = Frame(frame, bg='#F5F5DC')
        Frame3.pack(pady=15, padx=10)
        L3 = Label(Frame3, text='New Password: ', font=("Times", 14), bg='#F5F5DC')
        L3.pack(side='left')
        E3 = Entry(Frame3, bg='#F5F5DC', show='*')
        E3.pack(side='left')

        # Function for update button after the entries done
        def update_pswrd_btn():
            name = E1.get()
            password = E2.get()
            new_password = E3.get()

            # Read user history from file
            with open('user_history.txt', 'r') as file:
                history = file.readlines()

            updated_history = []
            password_updated = False
            for line in history:
                user = line.strip().split(',')
                if name.strip() == user[0].strip() and password.strip() == user[1].strip():
                    if len(new_password.strip()) < 8:
                        messagebox.showerror('', 'Password must be at least 8 characters long.')
                        return
                    elif not any(char.isdigit() for char in new_password):
                        messagebox.showerror('', 'Password must contain at least one digit.')
                        return
                    else:
                        user[1] = new_password.strip()
                        password_updated = True
                        messagebox.showinfo('', 'Password updated successfully!')
                        # Show the main update window and close the password update window
                        update_pass_wind.destroy()
                        update_wind.deiconify()

                updated_history.append(','.join(user) + '\n')

            if not password_updated:
                messagebox.showerror('', 'Invalid username or password.')

            # Write updated user history back to file
            with open('user_history.txt', 'w') as file:
                file.writelines(updated_history)

        Frame4 = Frame(update_pass_wind, bg='#F5F5DC')
        Frame4.pack(pady=10)
        update_password = Button(Frame4, text='Update', command=update_pswrd_btn, relief='raised', font="Times")
        update_password.pack()

    elif selected_option == 'contact':
        # Hide the main update window
        update_wind.withdraw()

        # Create a new window for updating contact
        update_contact_wind = Toplevel(update_wind)
        update_contact_wind['background'] = '#F5F5DC'
        update_contact_wind.title('S&K Gift Shop - Update Contact Info')
        update_contact_wind.geometry('300x350+350+100')

        # Create frames for layout
        frame = Frame(update_contact_wind, bg='#F5F5DC')
        frame.pack(expand=True)

        frame1 = Frame(frame, bg='#F5F5DC')
        frame1.pack(pady=15, padx=10)
        L1 = Label(frame1, text='Username: ', font=("Times", 14), bg='#F5F5DC')
        L1.pack(side='left')
        E1 = Entry(frame1, bg='#F5F5DC')
        E1.pack(side='left')

        frame2 = Frame(frame, bg='#F5F5DC')
        frame2.pack(pady=15, padx=10)
        L2 = Label(frame2, text='Password: ', font=("Times", 14), bg='#F5F5DC')
        L2.pack(side='left')
        E2 = Entry(frame2, bg='#F5F5DC', show='*')
        E2.pack(side='left')

        frame3 = Frame(frame, bg='#F5F5DC')
        frame3.pack(pady=15, padx=10)
        L3 = Label(frame3, text='Contact: ', font=("Times", 14), bg='#F5F5DC')
        L3.pack(side='left')
        E3 = Entry(frame3, bg='#F5F5DC')
        E3.pack(side='left')

        # Function for update button after the entries done
        def update_contact_btn():
            name = E1.get()
            password = E2.get()
            contact = E3.get()

            # Read user history from file
            with open('user_history.txt', 'r') as file:
                history = file.readlines()

            updated_history = []
            contact_updated = False
            for line in history:
                user = line.strip().split(',')
                if name.strip() == user[0].strip() and password.strip() == user[1].strip():
                    if len(contact.strip()) != 11:
                        messagebox.showerror('', 'Enter Correct Contact Number.')
                        return
                    elif not contact.isdigit():
                        messagebox.showerror('', 'Enter Correct Contact Number.')
                        return
                    else:
                        user[3] = contact.strip()
                        contact_updated = True
                        messagebox.showinfo('', 'Your contact number updated successfully!')
                        # Show the main update window and close the password update window
                        update_contact_wind.destroy()
                        update_wind.deiconify()

                updated_history.append(','.join(user) + '\n')

            if not contact_updated:
                messagebox.showerror('', 'Invalid username or password.')

            # Write updated user history back to file
            with open('user_history.txt', 'w') as file:
                file.writelines(updated_history)

        frame4 = Frame(update_contact_wind, bg='#F5F5DC')
        frame4.pack(pady=10)
        update_contact = Button(frame4, text='Update', command=update_contact_btn, relief='raised', font="Times")
        update_contact.pack()

    elif selected_option == 'address':
        # Hide the main update window
        update_wind.withdraw()

        # Create a new window for updating contact
        update_address_wind = Toplevel(update_wind)
        update_address_wind['background'] = '#F5F5DC'
        update_address_wind.title('S&K Gift Shop - Update Contact Info')
        update_address_wind.geometry('300x350+350+100')

        # Create frames for layout
        frame = Frame(update_address_wind, bg='#F5F5DC')
        frame.pack(expand=True)

        frame1 = Frame(frame, bg='#F5F5DC')
        frame1.pack(pady=15, padx=10)
        L1 = Label(frame1, text='Username: ', font=("Times", 14), bg='#F5F5DC')
        L1.pack(side='left')
        E1 = Entry(frame1, bg='#F5F5DC')
        E1.pack(side='left')

        frame2 = Frame(frame, bg='#F5F5DC')
        frame2.pack(pady=15, padx=10)
        L2 = Label(frame2, text='Password: ', font=("Times", 14), bg='#F5F5DC')
        L2.pack(side='left')
        E2 = Entry(frame2, bg='#F5F5DC', show='*')
        E2.pack(side='left')

        frame3 = Frame(frame, bg='#F5F5DC')
        frame3.pack(pady=15, padx=10)
        L3 = Label(frame3, text='Address: ', font=("Times", 14), bg='#F5F5DC')
        L3.pack(side='left')
        E3 = Entry(frame3, bg='#F5F5DC')
        E3.pack(side='left')

        # Function for update button after the entries done
        def update_address_btn():
            name = E1.get()
            password = E2.get()
            address = E3.get()

            # Read user history from file
            with open('user_history.txt', 'r') as file:
                history = file.readlines()

            updated_history = []
            address_updated = False
            for line in history:
                user = line.strip().split(',')
                if name.strip() == user[0].strip() and password.strip() == user[1].strip():
                    if not any(char.isalpha() for char in address):
                        messagebox.showerror('', 'Enter Correct Address.')
                        return

                    elif not any(digit.isdigit() for digit in address):
                        messagebox.showerror('', 'Enter Correct Address.')
                        return

                    else:
                        user[2] = address.strip()
                        address_updated = True
                        messagebox.showinfo('', 'Your address updated successfully!')
                        # Show the main update window and close the address update window
                        update_address_wind.destroy()
                        update_wind.deiconify()

                updated_history.append(','.join(user) + '\n')

            if not address_updated:
                messagebox.showerror('', 'Invalid username or password.')

            # Write updated user history back to file
            with open('user_history.txt', 'w') as file:
                file.writelines(updated_history)

        frame4 = Frame(update_address_wind, bg='#F5F5DC')
        frame4.pack(pady=10)
        update_address = Button(frame4, text='Update', command=update_address_btn, relief='raised', font="Times")
        update_address.pack()


def update_info(username, menu):
    """Create the main update window for selecting the update option."""

    # hide product menu
    menu.withdraw()
    # Create Window
    update_wind = Toplevel(menu)
    update_wind['background'] = '#F5F5DC'
    update_wind.title('S&K Gift Shop - Update Credentials')
    update_wind.geometry('550x600+20+50')

    update_wind.grab_set()

    gap_lab = Label(update_wind, text='\n', bg='#F5F5DC')
    gap_lab.pack()

    frame = Frame(update_wind, highlightbackground="#800000", bg='#F5F5DC', highlightthickness=2)
    frame.pack()

    frame1 = Frame(frame, bg='#F5F5DC')
    frame1.pack()

    ## IMAGE
    # Set title image
    img1 = PhotoImage(file='GIFT SHOP (4).png')
    img_lab = Label(frame1, image=img1, bg='#F5F5DC')
    img_lab.pack(side='left', anchor='nw', padx=10, pady=10)

    frame2 = Frame(frame, bg='#F5F5DC')
    frame2.pack(expand=True)

    lab2 = Label(frame2, text=f'Hey {username}! What do you want to update?', font=("Times", 14), bg='#F5F5DC')
    lab2.pack(padx=10, pady=20)

    # Initialize radio buttons
    var = StringVar()
    var.set(None)

    # Create radio buttons
    rd_btn_password = Radiobutton(frame2, text='Password', variable=var, value='password', font=('Times', 14),
                                  bg='#F5F5DC')
    rd_btn_contact = Radiobutton(frame2, text='Contact', variable=var, value='contact', font=('Times', 14),
                                 bg='#F5F5DC')
    rd_btn_address = Radiobutton(frame2, text='Address', variable=var, value='address', font=('Times', 14),
                                 bg='#F5F5DC')

    rd_btn_password.pack(anchor='w')
    rd_btn_contact.pack(anchor='w')
    rd_btn_address.pack(anchor='w')

    def handle_update_wrapper():
        selected_option = var.get()
        handle_update(selected_option, update_wind)

    def back():
        update_wind.destroy()
        menu.deiconify()

    # Button to proceed after selecting a radio button
    update_button = Button(frame2, text="Change", command=handle_update_wrapper, relief='raised', font="Times")
    update_button.pack(pady=10, padx=60, side='left')

    done_btn = Button(frame2, text="Back", command=back, relief='raised', font="Times")
    done_btn.pack(pady=10, padx=60, side='right')

    update_wind.mainloop()


# update_info('khadijasehar'
