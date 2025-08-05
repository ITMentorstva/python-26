
import tkinter as tk
import re

window = tk.Tk() # Napravio je novi prozor (window)
window.geometry("1024x720")
window.title("Moj program")

is_dark_mode = True

window.configure(bg="black")

# Creating a main label
tk.Label(window,
         text="Hello how are you doing?",
         font=("Arial", 16),
         fg="darkblue",
         bg="orange"
).pack()


#============ Sign Up Button ==============

def on_click():

    email = email_entry.get()

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(pattern, email) is None:
        print("Uneti email nije u dobrom formatu")

    if email == "admin@admin.com" and password_entry.get() == "123456":
        print("Dobrosao")
    else:
        print("Pogresni kredencijali!")


tk.Button(window,
          text="Sign up!",
          font=("Arial", 16),
          bg="darkblue",
          fg="white",
          command=on_click
).pack(pady=15)


def toggle_dark_mode():
    global is_dark_mode

    if is_dark_mode:
        is_dark_mode = False
        window.configure(bg="white")
    else:
        is_dark_mode = True
        window.configure(bg="black")

tk.Button(window,
          text="Dark Mode",
          font=("Arial", 16),
          bg="orange",
          fg="white",
          command=toggle_dark_mode
).pack(pady=15)

#=============== Entry ===============
password_entry = tk.Entry(window, width=50)
password_entry.pack()

#================ Email Entry ==========
# - Mora biti email (regex) (ako nije ispisite u konzoli gresku)
# - ako je email "admin@admin.com" i sifra "123456" print("Dobrodosao!")

email_entry = tk.Entry(window, width=50)
email_entry.pack()

window.mainloop()