from tkinter import *
root = Tk()
root.geometry("280x190")
root.minsize(250,150)
root.maxsize(600,500)
lable = Label(text="This is Lable Frame",fg="blue", anchor=W)
lable.pack(side=TOP, pady=5, anchor="nw")

lable1 = Label(text="1.This is a lable.",fg="red")
lable1.pack(side=TOP, pady=10, anchor="nw")

lable2 = Label(text="2.This is another lable.",fg="green")
lable2.pack(side=TOP, pady=10, anchor="nw")

lable3 = Label(text="3.We can add multiple lable.",fg="gray")
lable3.pack(side=TOP, pady=10, anchor="nw")



root = mainloop()