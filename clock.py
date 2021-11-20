from tkinter import *
from turtle import *
import datetime
import time
import os

def main_clock():
    window = Tk()
    window.title("Select Option")
    window.geometry("500x250")

    STYLE = ("Courier", 70, "bold")

    def clock():
        title("Clock")

        while True:
            hideturtle()
            reset()
            write(datetime.datetime.now().strftime("%H:%M:%S"), font=STYLE, align="center")
            time.sleep(1)

    def stopwatch():
        title("Stopwatch")

        s = 0
        m = 0
        h = 0

        while True:
            hideturtle()
            reset()

            s = s + 1

            write(str(h) + ":" + str(m) + ":" + str(s), font=STYLE, align="center")

            if s == 60:
                s = 0
                m = m + 1
                write(str(h) + ":" + str(m) + ":" + str(s), font=STYLE, align="center")
            elif m == 60:
                m = 0
                h = h + 1
                write(str(h) + ":" + str(m) + ":" + str(s), font=STYLE, align="center")
            
            time.sleep(1)

    def timer():
        title("Timer")

        hideturtle()

        def hours():
            amount_hours = int(textinput("Enter amount", "Enter amount of hours:"))

            while True:
                hideturtle()
                reset()

                write(amount_hours, font=STYLE, align="center")

                time.sleep(3600)
            
                amount_hours = amount_hours - 1

                if amount_hours == 0:
                    break


            reset()        
            write("Time is up!", font=STYLE, align="center")
            done()
        
        def minutes():
            amount_minutes = int(textinput("Enter amount", "Enter amount of minutes:"))

            while True:
                hideturtle()
                reset()

                write(amount_minutes, font=STYLE, align="center")

                time.sleep(60)
                amount_minutes = amount_minutes - 1


                if amount_minutes == 0:
                    break
            
            reset()
            write("Time is up!", font=STYLE, align="center")
            time.sleep(3)
            bye()
        
        def seconds():
            amount_seconds = int(textinput("Enter amount", "Enter amount of seconds:"))

            while True:
                hideturtle()
                reset()

                write(amount_seconds, font=STYLE, align="center")

                time.sleep(1)

                amount_seconds = amount_seconds - 1


                if amount_seconds == 0:
                    break

            reset()
            write("Time is up!", font=STYLE, align="center")
            time.sleep(3)
            bye()

        smh = textinput("Choose time amount:", "(1)Hours, (2)Minutes or (3)Seconds?")

        if smh == "1":
            hours()
        elif smh == "2":
            minutes()
        elif smh == "3":
            seconds()
        elif smh == "4":
            write("Invalid.", font=STYLE, align="center")
            time.sleep(1)
            timer()

    Button(window, text="Clock", command=lambda:clock()).pack()
    Button(window, text="Stopwatch", command=lambda:stopwatch()).pack()
    Button(window, text="Timer", command=lambda:timer()).pack()

    Label(window, text="\n").pack()

    def closeAll():
        bye()
        os.system("clear")

    Button(window, text="Close All Turtle Windows", command=lambda:closeAll()).pack()
    Button(window, text="Close This Window", command=lambda:window.destroy()).pack()

    window.mainloop()