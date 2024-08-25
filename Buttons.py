from tkinter import Tk, Entry, Frame,PhotoImage, Label, Button, messagebox, Radiobutton, StringVar
from update_user_info import update_info
from PIL import Image, ImageTk
from checkout import*


def back(window):

    window.destroy()
    from main import open_main_wind

    open_main_wind()


def more_menu_btns(username):
    # Define functions for different actions

    # Function to view the cart
    def view_cart(window):
        with open('temporary cart.txt', 'r') as file:
            window.withdraw()
            lines = file.readlines()
            file.seek(0)
            file_empty= file.read().strip()

            if not file_empty:
                tk.messagebox.showinfo("GiftShop", "Your cart is empty!")
            else:
                # Create a new Tkinter window
                cart_window = tk.Toplevel()
                cart_window.title('Cart')
                cart_window.geometry('400x600+150+50')

                # Load the background image
                background_image = Image.open('1 (1).png')  # Replace with your image path
                background_image = background_image.resize((400, 600))
                background_image = ImageTk.PhotoImage(background_image)

                # Create a label to display the background image
                background_label = tk.Label(cart_window, image=background_image)
                background_label.image = background_image  # Keep a reference to avoid garbage collection
                background_label.place(x=0, y=0, relwidth=1, relheight=1)

                # Create a frame for the cart content with fixed dimensions
                cart_frame = tk.Frame(cart_window, width=380, height=350)
                cart_frame.pack(expand=True, fill='both', padx=10, pady=10)

                # Create a canvas and scrollbar within the fixed dimensions
                canvas = tk.Canvas(cart_frame, width=360, height=300)
                scrollbar = tk.Scrollbar(cart_frame, orient="vertical", command=canvas.yview)
                scrollable_frame = tk.Frame(canvas)

                # Configure the scrollbar with the canvas
                scrollable_frame.bind(
                    "<Configure>",
                    lambda e: canvas.configure(
                        scrollregion=canvas.bbox("all")
                    )
                )

                canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                canvas.configure(yscrollcommand=scrollbar.set)

                # Packing the canvas and scrollbar
                canvas.pack(side="left", fill="both", expand=True)
                scrollbar.pack(side="right", fill="y")

                # Add a title label
                title_label = tk.Label(scrollable_frame, text="Your Cart", font=('Times', 16, 'bold'))
                title_label.pack(pady=(0, 10), padx=130)

                # Read the cart file and display contents
                try:
                    for line in lines[2:]:  # Skip header lines
                        if line.strip():  # Skip empty lines
                            item, qty = line.split(':')
                            item = item.strip()
                            qty = qty.strip()

                            # Create a label for each item
                            item_label = tk.Label(scrollable_frame, text=f"{item}x1 - Quantity: {qty}",
                                                  font=('Times', 12))
                            item_label.pack(anchor='w', pady=5)

                except FileNotFoundError:
                    # Handle the case where the file doesn't exist
                    error_label = tk.Label(scrollable_frame, text="Cart file not found",
                                           font=('Times', 12, 'italic'))
                    error_label.pack(pady=10)

                # call through button back; to destroy cart window
                def back():
                    cart_window.destroy()
                    window.deiconify()

                # Add a button to close the cart window
                back_button = tk.Button(cart_window, text="Back",width=8, command=back)
                back_button.pack(padx=50, pady=20, side='left')

                # Add a button to proceed to checkout
                proceed_button = tk.Button(cart_window, text="Checkout", width=11, command=lambda w=window: Check_out(username))
                proceed_button.pack(padx=50, pady=20, side='right')


                # Ensure the scrollbar appears if needed
                cart_window.update_idletasks()

    def view_history(window):
        # Open the user's order history file
        try:
            with open(f'{username}.txt', 'r') as file:
                window.withdraw()
                lines = file.readlines()
                file.seek(0)
                file_empty = file.read().strip()

                if not file_empty:
                    tk.messagebox.showinfo("GiftShop", "Your order history is empty!")
                else:
                    # Create a new Tkinter window
                    history_window = tk.Toplevel()
                    history_window.title('Order History')
                    history_window.geometry('750x600+150+50')

                    # Load the background image
                    background_image = Image.open('1 (1).png')  # Replace with your image path
                    background_image = background_image.resize((800, 600))
                    background_image = ImageTk.PhotoImage(background_image)

                    # Create a label to display the background image
                    background_label = tk.Label(history_window, image=background_image)
                    background_label.image = background_image  # Keep a reference to avoid garbage collection
                    background_label.place(x=0, y=0, relwidth=1, relheight=1)

                    # Create a frame for the order history content with fixed dimensions
                    history_frame = tk.Frame(history_window, width=380, height=350)
                    history_frame.pack(expand=True, fill='both', padx=10, pady=10)

                    # Create a canvas and scrollbar within the fixed dimensions
                    canvas = tk.Canvas(history_frame, width=300, height=300)
                    scrollbar = tk.Scrollbar(history_frame, orient="vertical", command=canvas.yview)
                    scrollable_frame = tk.Frame(canvas)

                    # Configure the scrollbar with the canvas
                    scrollable_frame.bind(
                        "<Configure>",
                        lambda e: canvas.configure(
                            scrollregion=canvas.bbox("all")
                        )
                    )

                    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                    canvas.configure(yscrollcommand=scrollbar.set)

                    # Packing the canvas and scrollbar
                    canvas.pack(side="left", fill="both", expand=True)
                    scrollbar.pack(side="right", fill="y")

                    # Add a title label
                    title_label = tk.Label(scrollable_frame, text="Order History", font=('Times', 16, 'bold'))
                    title_label.pack(pady=(0, 10), padx=130)

                    # Read the order history file and display contents
                    for line in lines:
                        if line.strip():  # Skip empty lines
                            # Create a label for each line, keeping the text aligned
                            item_label = tk.Label(scrollable_frame, text=line.strip(), font=('Courier', 12), anchor='w',
                                                  justify='left')
                            item_label.pack(anchor='w', pady=2)

                    # Function to handle the back button
                    def back():
                        history_window.destroy()
                        window.deiconify()

                    # Add a button to go back
                    back_button = tk.Button(history_window, text="Back", width=8, command=back)
                    back_button.pack(padx=50, pady=20)

        except FileNotFoundError:
            messagebox.showinfo('order history', 'You Haven\'t order yet!')


    def about_us():
        # Create a new Tkinter window
        cart_window = tk.Toplevel()
        cart_window.title('About Us')
        cart_window.geometry('500x500')

        # Load and resize the background image
        background_image = Image.open('wallpapersden.com_77118-500x500.jpg')  # Ensure the path is correct
        background_image = background_image.resize((500, 500), Image.LANCZOS)
        background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to display the background image
        background_label = tk.Label(cart_window, image=background_photo)
        background_label.image = background_photo  # Keep a reference to avoid garbage collection
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame to add the pink border
        border_frame = tk.Frame(cart_window, bg="#FFC0CB", bd=5)
        border_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

        # Create another frame inside the border frame to hold content
        content_frame = tk.Frame(border_frame, bg="#F5F5DC")
        content_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.98, relheight=0.98)

        # Add a heading label in the center of the window
        heading_label = tk.Label(content_frame, text="About Us", font=("Arial", 24, "bold"), bg="#F5F5DC", fg="#FF69B4")
        heading_label.pack(pady=20)

        # Add a description label with left-aligned text
        description = tk.Label(content_frame, text=(
            "The S&K Gift Shop is a small online platform that aims to facilitate "
            "its users by providing them with a wide variety of products to choose from. "
            "Our platform is designed to help you find the perfect gifts for your loved ones, "
            "whether it’s for a birthday, anniversary, or just because. Explore our carefully curated "
            "collections to discover unique and thoughtful gifts that are sure to delight."
        ), wraplength=450, justify="left", bg="#F5F5DC", fg="black", font=("Arial", 12))
        description.pack(pady=10)

        # Run the main loop to display the window
        cart_window.mainloop()


    # Function to log out from the current session
    def logout(menu):
        # destroy the current window and open the first window
        logout_question = messagebox.askquestion('', "Are you leaving?")
        if logout_question == 'yes':
            menu.destroy()

            messagebox.showinfo('', 'You\'ve been logout successfully!')

    def update_credentials(menu):
        update_info(username, menu)
        # pass

    # Function to delete the user account
    def delete_account(menu):

        # hide product menu window
        menu.withdraw()

        # Function to handle deletion of the account
        def del_accnt():
            nonlocal line

            entered_password = paswrd.get()

            # Check if the entered password matches the stored password
            if entered_password == password:
                # remove the error label if present
                error_label.pack_forget()

                # hide the del_wind and product menu
                del_wind.withdraw()
                # prd_menu.menu.withdraw()

                # show a messagebox for confirmation
                response = messagebox.askquestion("Confirmation",
                                                  "Are you sure you want to delete your account?")
                if response == 'yes':
                    # If password is correct, delete the account
                    with open('user_history.txt') as file:
                        lines = file.readlines()
                    with open('user_history.txt', 'w') as new_file:
                        for l in lines:
                            if l.strip() != line.strip() and l.strip():  # Skip writing empty lines
                                new_file.write(l)
                    del_wind.destroy()
                    menu.destroy()

                    messagebox.showinfo('', 'Your account has been deleted successfully!')

                else:
                    del_wind.destroy()
                    menu.deiconify()

            else:
                # if error label already exists remove it first
                error_label.pack_forget()

                # If password is incorrect, display an error message
                error_label.pack()

        # Read history to check if the user is in history or not
        with open('user_history.txt') as file:
            for line in file:
                if not line.strip():  # Skip empty lines
                    continue

                history = line.split(',')
                name = history[0].strip()
                password = history[1].strip()

                # If user exists in history, create a window to verify password
                if username == name:
                    del_wind = Tk()
                    del_wind['background'] = '#F5F5DC'
                    del_wind.title('S&K Gift Shop')
                    del_wind.geometry('270x170+250+250')

                    frame = Frame(del_wind, bg='#F5F5DC')
                    frame.pack(pady=10, padx=10)

                    paswrd = Entry(frame, bg='#F5F5DC', show="*")
                    paswrd.pack(side='right')

                    label = Label(frame, text='Password', font='Times', bg='#F5F5DC')
                    label.pack(side='left', pady=10, padx=10)

                    # Error message for incorrect password
                    error_frame = Frame(del_wind, bg='#F5F5DC')
                    error_frame.pack()
                    error_label = Label(error_frame, text='Enter Correct Password', font=('Times', 8), bg='#F5F5DC',
                                        fg='red')

                    btn_frame = Frame(del_wind, bg='#F5F5DC')
                    btn_frame.pack(expand=True, pady=10)
                    button = Button(btn_frame, text='Done', relief='raised', font="Times",
                                    command=del_accnt, bg='#F5F5DC')
                    button.pack(side='right')

                    del_wind.mainloop()

    # Return the functions as a tuple along with the comment
    return view_cart, view_history, about_us, logout, update_credentials, delete_account
