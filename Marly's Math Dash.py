import tkinter as tk
from tkinter import PhotoImage
import time
switchColor = lambda: screen.config(background='red')
switchColor2 = lambda: screen.config(background='tomato')
switchColor3 = lambda: screen.config(background='orange')
switchColor4 = lambda: screen.config(background='gold')
switchColor5 = lambda: screen.config(background='yellow')
switchColor6 = lambda: screen.config(background='chartreuse')
switchColor7 = lambda: screen.config(background='green')
switchColor8 = lambda: screen.config(background='teal')
switchColor9 = lambda: screen.config(background='cyan')
switchColor10 = lambda: screen.config(background='lightBlue')
switchColor11 = lambda: screen.config(background='blue')
switchColor12 = lambda: screen.config(background='indigo')
switchColor13 = lambda: screen.config(background='violet')
switchColor14 = lambda: screen.config(background='magenta')
switchColor15= lambda: screen.config(background='crimson')


screen = tk.Tk()
screen.geometry("889x500")
screen.title("Marly's Math Dash")
windowIcon = PhotoImage(file= 'sprites/chillFish.png')
screen.iconphoto(True, windowIcon)
screen.config(background="red")


screen.mainloop()