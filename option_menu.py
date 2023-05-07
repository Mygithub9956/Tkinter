from tkinter import *

root = Tk()
root.geometry("300x200")
root.minsize(250,150)
root.maxsize(900,750)
root.title("Salman App")
lable = Label(text = "Choose the weekday from Dropdown menu")
lable.pack()


options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]


selected_option = StringVar(root)
selected_option.set(options[0])  


option_menu = OptionMenu(root, selected_option, *options)
option_menu.pack(pady=20,)


root.mainloop()
