import tkinter as tk
from tkinter import PhotoImage, Button
def playButtonClick():
    for i in range(5):
        print("Joe Biden?")
x = 0
#screen1 creation
screen1 = tk.Tk()
screen1.config(background='red')
screen1.geometry("889x500")
screen1.title("Marly's Math Dash")
windowIcon = PhotoImage(file = 'sprites/chillFish.png')
screen1.iconphoto(True, windowIcon)

#screen buttons
playButton = Button(screen1, text = '     Play▶️', width=5, height=1  )
playButton.pack()
playButton.config(command = playButtonClick,
                  font=('papyrus', 12, 'italic'),
                  bg='#003187')



screen1.mainloop()