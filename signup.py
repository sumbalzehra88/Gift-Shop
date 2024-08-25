from PIL import Image, ImageDraw, ImageTk
from tkinter import Tk, PhotoImage, Label, Frame, Button
from signup import open_create_wind
from signin import open_login_wind


def open_main_wind():

    # Create the main window
    window = Tk()
    window['background'] = '#F5F5DC'
    window.title('S&K Gift Shop')
    window.geometry('530x600+20+50')

    # Set a frame for all the widgets
    frame1 = Frame(window, bg='#F5F5DC', highlightbackground='#800000', highlightthickness=3)
    frame1.pack(padx=10, pady=10)

    # Open the image
    img = Image.open("Shopping cart logo.png")
    # resize image to 500x500
    resized_img = img.resize((300, 300))

    # Create a circular mask
    mask = Image.new('L', resized_img.size)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, resized_img.size[0], resized_img.size[1]), fill=255)

    # Apply the mask to the original image
    circular_img= Image.new('RGB', resized_img.size, '#F5F5DC')
    circular_img.paste(resized_img, mask=mask)

    # Draw a border around the circular image
    border_width = 3  # Set the border width
    border_color = (128, 0, 0)  # Set the border color to maroon (#800000)
    draw = ImageDraw.Draw(circular_img)
    draw.ellipse((0, 0, resized_img.size[0], resized_img.size[1]),
                 outline=border_color, width=border_width)

    # Convert PIL Image to Tkinter PhotoImage
    photo_image = ImageTk.PhotoImage(circular_img)

    # Create a label to display the image
    image_label = Label(frame1, image=photo_image, bg='#F5F5DC')
    image_label.pack()

    # Keep a reference to the PhotoImage object to prevent garbage collection
    image_label.image = photo_image

    # Welcome label
    lab2 = Label(frame1, text='WELCOME TO S&K VIRTUAL GIFT SHOP!', font=('Open Sans', 18, 'bold'), fg='#800000', bg='#F5F5DC')
    lab2.pack(padx=10, pady=10)

    # Advertising label
    L = Label(frame1, text='Do you wish to buy your favourite gifts? Shop now!', bg='#fcb542', fg="black", font=("Bold", 12), relief='raised')
    L.pack(padx=10, pady=20)

    # Create a frame for the login button
    frame2 = Frame(frame1, bg='#F5F5DC')
    frame2.pack()

    # Login button
    L1 = Label(frame2, text='Already have an account?', font=("Times", 14), fg='black', bg='#F5F5DC')
    L1.pack(side="left", padx=10, pady=10)


    B1 = Button(frame2, text='Signin', bg='#F5F5DC', fg='#292724', relief='raised', font="Times",
                command=lambda: open_login_wind(window))
    B1.pack(side="right", padx=5, pady=5)

    # Create a frame for the signin button
    frame3 = Frame(frame1, bg='#F5F5DC')
    frame3.pack()

    # Create account button
    L2 = Label(frame3, text='New? Let\'s create an account.', font=("Times", 14), fg='black', bg='#F5F5DC')
    L2.pack(side="left", padx=5, pady=5)

    B2 = Button(frame3, text='Signup', bg='#F5F5DC', fg='#292724', relief='raised', font="Times",
                command=lambda: open_create_wind(window))
    B2.pack(side="right", padx=5, pady=5)

    # Run the window
    window.mainloop()


open_main_wind()
