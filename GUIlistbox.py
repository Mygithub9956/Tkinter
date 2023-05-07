from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("FOOD MENU")
root.minsize(500,300)
root.maxsize(900,600)


label = Label(text="FOOD ITEMS",font=("Arial",14))
label.pack()


listbox = Listbox(font=("Arial", 19), fg="yellow", bg="gray")
listbox.pack()


listbox.insert(END, "Pizza")
listbox.insert(END, "Burger")
listbox.insert(END, "Sandwich")
listbox.insert(END, "Nachos")
listbox.insert(END, "Garlic Bread")
listbox.insert(END, "Dhokla")
listbox.insert(END, "Litti Chowkha")
listbox.insert(END, "Masala dosa")

root.mainloop()
