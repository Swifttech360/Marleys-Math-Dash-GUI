import tkinter as tk
from sys import maxsize
from tkinter import PhotoImage, Button
def playButtonClick():
    for i in range(5):
        print("You Pressed The Button")



#screen1 creation


screen1 = tk.Tk()
screen1.config(background='#1f1f1f')
screen1.geometry(f"{1920}x{1080}")
screen1.title("Marly's Math Dash")
windowIcon = PhotoImage(file = 'sprites/chillFish.png')
screen1.iconphoto(True, windowIcon)



screen1.grid_rowconfigure(0, weight=440, minsize=440)
screen1.grid_rowconfigure(1, weight=200, minsize=200)
screen1.grid_rowconfigure(2, weight=440, minsize=440)

screen1.grid_columnconfigure(0, weight=1, minsize=640)
screen1.grid_columnconfigure(1, weight=1, minsize=640)
screen1.grid_columnconfigure(2, weight=1, minsize=640)

#screen buttons
playSprite = PhotoImage(file='sprites/PerfectlyCroppedPlayButton.png')
playSprite = playSprite.subsample(4, 4)
playButton = Button(screen1)
#playButton.pack()



playButton.config(
    command = playButtonClick,
    text='START',
    font=('arial', 50, 'bold'),
    borderwidth=2,
    relief='flat',
    bg='#c40000',
    activebackground='#940000',
    width=7
    )

playButton.grid(row=0, column=1,sticky='ews', pady=0 )

leaderboardButton = tk.Button(screen1)

leaderboardButton.config(
    command = None,
    text='Leaderboard',
    font=('arial', 50, 'bold'),
    borderwidth=0,
    relief='flat',
    bg='#c40000',
    activebackground='#940000',
    width=10
)

leaderboardButton.grid(row=1, column=1, sticky='we',)


exitButton = tk.Button(screen1)

exitButton.config(
    command = exit,
    text='QUIT',
    font=('arial', 50, 'bold'),
    borderwidth=0,
    relief='flat',
    bg='#c40000',
    activebackground='#940000',
    width=7
)
exitButton.grid(row=2, column=1,sticky='wen', pady=0)



#playButton.config(
 #   command = playButtonClick,
  #  image=playSprite,
   # borderwidth=0,
    #relief='flat',
    #bg='#a80000',
    #activebackground='#a80000'
    #)
# NOTE: PlaySprite's dimensions are 1916x814
#playButton.place(x=(2560-450) // 2,y= 500)




screen1.mainloop()