from tkinter import *


root = Tk()
root.geometry("300x165")
root.minsize(300,165)
root.maxsize(600,500)
root.title("My First GUI Window")



label = Label(text="Select programming language of your choice:")
label.pack()


checkbox1 = Checkbutton(text="Java")
checkbox1.pack(side=TOP, anchor=W, padx=45)

checkbox2 = Checkbutton(text="C++")
checkbox2.pack(side=TOP, anchor=W, padx=45)

checkbox3 = Checkbutton(text="C")
checkbox3.pack(side=TOP, anchor=W, padx=45)

checkbox4 = Checkbutton(text="Python")
checkbox4.pack(side=TOP, anchor=W, padx=45)


root.mainloop()
