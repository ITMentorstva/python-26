
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("1024x720")
window.title("Lista proizvoda")


fruit_info = {
    "Apple": "Apples are sweet, crunchy fruits. They come in many colors.",
    "Banana": "Bananas are rich in potassium and great for energy.",
    "Cherry": "Cherries are small, round, and often red or black.",
    "Date": "Dates are sweet fruits from date palms, popular in Middle East.",
    "Elderberry": "Elderberries are used in syrups and have immune-boosting properties."
}

fruit_images = {
    "Apple": "apple.jpeg",
    "Banana": "banana.jpg",
}


def show_item_info(event):
    selection = listbox.curselection() #current selection - trenutna selekcija
    name = listbox.get(selection)

    product_info.configure(state='normal')

    image = Image.open(fruit_images[name]) # Image.open("Apple.jpeg")
    image = image.resize((50, 50))

    photo = ImageTk.PhotoImage(image)

    product_info.delete('1.0', tk.END)
    product_info.insert(tk.END, fruit_info[name])

    image_label.config(image=photo)
    image_label.image = photo

    product_info.configure(state='disabled')



product_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

listbox = tk.Listbox(window, height=50)
listbox.pack(side="left", padx=10)

for item in product_list:
    listbox.insert(tk.END, item)


listbox.bind("<<ListboxSelect>>", show_item_info)


product_info = tk.Text(window, width=50, height=50, font=("Arial", 14))
product_info.pack(side="left")

image_label = tk.Label(window, bg="white", width=50, height=50)
image_label.pack(side="left", padx=20)


window.mainloop()