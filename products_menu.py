import tkinter as tk
from tkinter import ttk, Label, messagebox
from update_user_info import update_info
from Buttons import more_menu_btns

# Cart management
cart = {}


def update_cart():
    with open('temporary cart.txt', 'w') as cart_file:
        cart_file.write("name price x1: quantity\n\n")
        for item, qty in cart.items():
            cart_file.write(f"{item}: {qty}\n")


def add_to_cart(item_name):
    if item_name in cart:
        if cart[item_name] >= 50:
            messagebox.showinfo('Cart', f"sorry! we don't have more than 50 {item_name}")
        else:
            cart[item_name] += 1
    else:
        cart[item_name] = 1
    update_cart()
    update_quantity_label(item_name)


def remove_from_cart(item_name):
    if item_name in cart:
        if cart[item_name] > 1:
            cart[item_name] -= 1
        else:
            del cart[item_name]
    update_cart()
    update_quantity_label(item_name)

def update_quantity_label(item_name):
    # Update the quantity label based on the cart contents
    if item_name in item_labels:
        quantity = cart.get(item_name, 0)
        item_labels[item_name].config(text=str(quantity))


def prd_menu(username,window):
    # window.withdraw()
    window.destroy()

    menu = tk.Tk()
    menu.title('Gift Shop-Menu')
    menu['background'] = '#F5F5DC'
    menu.geometry('600x710+150+0')


    # Frame for the top section (header)
    f1 = tk.Frame(menu, bg='#F5F5DC')
    f1.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=10, pady=5)

    # Frame for the notebook
    f2 = tk.Frame(menu, bg='#F5F5DC')
    f2.grid(row=1, column=0, columnspan=2, pady=5, sticky='nsew')

    # Frame for the bottom image
    f3 = tk.Frame(menu, bg='#F5F5DC')
    f3.grid(row=2, column=0, columnspan=2, sticky='nsew')

    # Image and labels in the header (f1)
    img1 = tk.PhotoImage(file='GIFT SHOP (4).png')
    img_lab = tk.Label(f1, image=img1, bg='#F5F5DC')
    img_lab.grid(row=0, column=0, padx=(0, 50), sticky='w')

    f1_lab = tk.Frame(f1, bg='#F5F5DC')
    f1_lab.grid(row=0, column=1, sticky='n')

    sk_label = tk.Label(f1_lab, text='S&K', font=('Times', 20, 'italic'), fg='navy', bg='#F5F5DC')
    sk_label.grid(row=0, column=0)

    gift_shop_label = tk.Label(f1_lab, text=' gift shop', font=('Times', 15, 'italic'), fg='navy', bg='#F5F5DC')
    gift_shop_label.grid(row=1, column=0)

    advertising_label = tk.Label(f1_lab, text='hurry up, fill your basket!', font=("verdana", 10), fg='navy', bg='#F5F5DC')
    advertising_label.grid(row=2, column=0, pady=10)

    # Frame for buttons
    f_btn = tk.Frame(f1, bg='#F5F5DC')
    f_btn.grid(row=0, column=2, sticky='ne', padx=10)

    # Buttons in the header (f1)
    btn_view_cart = tk.Button(f_btn, text="view cart", relief='raised', font=('Times', 10), bg='pink', fg='black', command=lambda w=menu: view_cart(w))
    btn_view_cart.grid(row=0, column=0, sticky='e', padx=(10, 0))

    down_arrow = "\u25BC"
    more_btn = tk.Menubutton(f_btn, text=' more ' + down_arrow, relief='raised', font=('Times', 10), bg='pink', fg='black')
    more_btn.grid(row=0, column=1, sticky='e')

    # Dropdown menu for the "more" button
    more_menu = tk.Menu(more_btn, tearoff=False)
    more_btn.configure(menu=more_menu)

    view_cart, view_history, about_us, logout, update_credentials, delete_account = more_menu_btns(username)

    more_menu.add_command(label="Order(s) History", command=lambda w=menu : view_history(w))
    more_menu.add_command(label="About Us", command=about_us)
    more_menu.add_command(label="Logout", command=lambda m=menu : logout(m))
    more_menu.add_command(label="Update Account Info", command=lambda u=username, m=menu: update_info(u,m))
    more_menu.add_command(label="Delete Account", command=lambda: delete_account(menu))

    # Notebook in f2
    notebook = ttk.Notebook(f2)

    # Configure styles
    style = ttk.Style()
    style.configure('TNotebook', background='pink')  # Set notebook background color
    style.configure('TNotebook.Tab', background='pink', foreground='black', padding=[10, 5])
    style.map('TNotebook.Tab', background=[('selected', 'pink')])

    tabs = [
        (f'perfumes ', '#000080'),
        ('dresses ', '#000080'),
        ('watches ', '#000080'),
        ('jewellery  ', '#000080'),
        ('decor pieces ', '#000080'),
        ('books', '#000080'),
        ('stationary', '#000080'),
        ('others', '#000080')
    ]

    global item_labels
    item_labels = {}  # Dictionary to keep track of item quantity labels

    for tab_text, tab_color in tabs:
        tab = ttk.Frame(notebook)
        notebook.add(tab, text=tab_text)

        items_frame = tk.Frame(tab, bg='#F5F5DC')
        items_frame.pack(fill='both', padx=10, pady=10)

        def create_item(frame, item_name):
            parent_frame = tk.Frame(frame, bg='#F5F5DC')
            parent_frame.pack(fill='x', pady=5, padx=100)

            item_frame = tk.Frame(parent_frame, bg='#F5F5DC')
            item_frame.pack(side='left')

            btn_frame = tk.Frame(parent_frame, bg='#F5F5DC')
            btn_frame.pack(side='right', padx=50)

            # Label
            item_label = Label(item_frame, text=item_name, bg='pink', fg='black')
            item_label.pack(side='left')

            # Quantity buttons
            plus_button = tk.Button(btn_frame, text='+', bg='pink', fg='black',
                                    command=lambda name=item_name: add_to_cart(name))
            plus_button.pack(side='right', padx=(10, 0))

            quantity = cart.get(item_name, 0)
            quantity_label = tk.Label(btn_frame, text=str(quantity), bg='pink', fg='black')
            quantity_label.pack(side='right', padx=(10, 0))

            item_labels[item_name] = quantity_label  # Save the label for future updates

            minus_button = tk.Button(btn_frame, text='-', bg='pink', fg='black',
                                     command=lambda name=item_name: remove_from_cart(name))
            minus_button.pack(side='right', padx=(10, 0))

        if tab_text.strip() == "perfumes":
            # Create perfume items
            create_item(items_frame, "Smoky   Pkr 3000")
            create_item(items_frame, "Acorn   Pkr 3000")
            create_item(items_frame, "Musk    Pkr 2400")
            create_item(items_frame, "Dusk    Pkr 1200")
            create_item(items_frame, "Dawn    Pkr 2500")

        if tab_text.strip() == "dresses":
            # Create dress items
            create_item(items_frame, "Jeans  Pkr 5000")
            create_item(items_frame, "Shirt Pkr 6000")
            create_item(items_frame, "Shoes   Pkr 7000")
            create_item(items_frame, "Joggers   Pkr 4000")
            create_item(items_frame, "Denim   Pkr 9000")

        if tab_text.strip() == "watches":
            # Create watch items
            create_item(items_frame, "Blue Crystal  Pkr 5000")
            create_item(items_frame, "Round Clock Pkr 6000")
            create_item(items_frame, "Big Bang   Pkr 7000")
            create_item(items_frame, "Big Ben   Pkr 4000")
            create_item(items_frame, "Pluto  Pkr 9000")

        if tab_text.strip() == "jewellery":
            # Create jewellery items
            create_item(items_frame, "Bracelets  Pkr 5000")
            create_item(items_frame, "Amulets Pkr 6000")
            create_item(items_frame, "Chains   Pkr 7000")
            create_item(items_frame, "Rings   Pkr 4000")
            create_item(items_frame, "Silver Ring   Pkr 9000")

        if tab_text.strip() == "decor pieces":
            # Create decor pieces items
            create_item(items_frame, "Vase  Pkr 5000")
            create_item(items_frame, "Abstract Pkr 6000")
            create_item(items_frame, "Elevase   Pkr 7000")
            create_item(items_frame, "Glow   Pkr 4000")
            create_item(items_frame, "Blue Bird  Pkr 9000")

        if tab_text.strip() == "books":
            # Create book items
            create_item(items_frame, "Gone with the Wind  Pkr 5000")
            create_item(items_frame, "Sherlock Holmes Pkr 6000")
            create_item(items_frame, "The Shadow of the Wind   Pkr 7000")
            create_item(items_frame, "Harry Potter Series   Pkr 4000")
            create_item(items_frame, "Jane Eyre   Pkr 9000")

        if tab_text.strip() == "stationary":
            # Create stationary items
            create_item(items_frame, "Pencil Box  Pkr 5000")
            create_item(items_frame, "Highlighters Set  Pkr 6000")
            create_item(items_frame, "Glue   Pkr 7000")
            create_item(items_frame, "Erasers   Pkr 4000")
            create_item(items_frame, "Correction Pen   Pkr 9000")

        if tab_text.strip() == "others":
            # Create other items
            create_item(items_frame, "Sneakers  Pkr 5000")
            create_item(items_frame, "Sandals Pkr 6000")
            create_item(items_frame, "Customized Notebooks   Pkr 7000")
            create_item(items_frame, "Gift Baskets   Pkr 4000")
            create_item(items_frame, "Customized T-Shirts   Pkr 9000")

    notebook.pack(expand=1, fill='both')

    # Bottom images in f3
    img2 = tk.PhotoImage(file='S&K (1).png')
    img_lab2 = tk.Label(f3, image=img2, bg='#F5F5DC')
    img_lab2.grid(row=0, column=0, sticky='e')

    img3 = tk.PhotoImage(file='ORDER (5 x 1.5 cm).png')
    img_lab3 = tk.Label(f3, image=img3, bg='#F5F5DC')
    img_lab3.grid(row=1, column=0, sticky='e')

    menu.mainloop()

# prd_menu('khadija')
