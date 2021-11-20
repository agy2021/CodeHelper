from tkinter import *
import os

def main_todo():
    window = Tk()
    window.title("To-do list")
    window.geometry("500x750")

    def add():
        a = val.get()

        if a.isupper():
            a[0].upper()

        os.system("clear")

        Label(window, text="").pack()

        element = Label(window, text=a)
        element.pack()
        this = Button(window, text=f"Delete Element \"{a}\"", command=lambda:element.pack_forget() + this.pack_forget() + os.system("clear"))
        this.pack()

        os.system("clear")

    val = Entry(window)
    val.pack()

    Button(window, text="Add", command=lambda:add()).pack()

    window.mainloop()