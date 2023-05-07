from tkinter import *

root = Tk()
root.geometry("350x250")
root.title("My Web")
label = Label(text="This is Button and Checkbox")
label.pack()

button1 = Button(root, text="Button 1")
button1.place(relx=0.25, rely=0.2, anchor=CENTER)

button2 = Button(root, text="Button 2")
button2.place(relx=0.75, rely=0.2, anchor=CENTER)

checkbox1 = Checkbutton(root, text="Checkbox 1")
checkbox1.place(relx=0.25, rely=0.3, anchor=CENTER)

checkbox2 = Checkbutton(root, text="Checkbox 2")
checkbox2.place(relx=0.25, rely=0.4, anchor=CENTER)

root.mainloop()




