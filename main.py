from tkinter import *
from clock import main_clock
from todo_list import main_todo
from open_github import main_github
from open_stackoverflow import main_stackoverflow
from help import main_help

mainWin = Tk()
mainWin.title("Choose an option")
mainWin.geometry("500x250")

def open_help():
    win = Tk()
    win.title("Note")
    win.geometry("500x250")

    Label(win, text="Note: the FPS of the video may vary based on your Mac or PC.").pack()
    Button(win, text="Play Video", command=lambda:win.destroy + main_help()).pack()
    
    win.mainloop()


Button(mainWin, text="Time", command=lambda:main_clock()).pack()
Button(mainWin, text="Todo-list", command=lambda:main_todo()).pack()
Button(mainWin, text="Github", command=lambda:main_github()).pack()
Button(mainWin, text="Stack Overflow", command=lambda:main_stackoverflow()).pack()
Button(mainWin, text="Need Help?", command=lambda:open_help()).pack()

Label(mainWin, text="\n").pack()

Button(mainWin, text="Close", command=lambda:mainWin.destroy()).pack()

mainWin.mainloop()