import tkinter as tk
from tkinter import PhotoImage, Button
def playButtonClick():
    for i in range(5):
        print("You Pressed The Button")
x = 0
#screen1 creation
screen1 = tk.Tk()
screen1.config(background='red')
screen1.geometry(f"{screen1.winfo_screenwidth()}x{screen1.winfo_screenheight()}")
screen1.title("Marly's Math Dash")
windowIcon = PhotoImage(file = 'sprites/chillFish.png')
screen1.iconphoto(True, windowIcon)

#screen buttons
playSprite = PhotoImage(file='sprites/PerfectlyCroppedPlayButton.png')
playSprite = playSprite.subsample(4, 4)
playButton = Button(screen1)
playButton.pack()

playButton.config(
    command = playButtonClick,
    image=playSprite,
    borderwidth=0,
    relief='flat',
    bg='red',
    activebackground='red'
    )
# NOTE: PlaySprite's dimensions are 1916x814
#playButton.place(x=(2560-450) // 2,y= 500)
playButton.place(relx=0.495, rely=0.68, anchor='center')




screen1.mainloop()