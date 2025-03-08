import tkinter as tk
#from tkinter import PhotoImage, Button
import time
from sys import maxsize
import random as ran

def getEquation():
    global currentEquation
    global  enteredAnswer
    operatorList = ['+', '-', '*', '÷' ]
    randnum1 = ran.randint(0, 130)
    randnum2 = ran.randint(0, 130)
    randomOperator1 = ran.choice(operatorList)
    equationDisplay = f'{randnum1} {randomOperator1}, {randnum2}'
    answer = eval(equationDisplay)






def playButtonClick():
    
    for widget in menuWidgetList:
        widget.grid_forget()
    
    playScreenGrid()
    gameEntry.grid(
        row=57,
        rowspan=6,
        column=46, 
        sticky='news', 
        columnspan=9
    )
    gameEntry.insert(0, "Enter Answers Here")
    gameEntry.bind('<Button-1>', gameEntryFocusIn)
    
    questionBox.grid(row=49, column=45, rowspan=2, columnspan=11, sticky='nsew')
    labelAboveEntry.grid(row=54, column=45, rowspan=2, columnspan=11)
    timeLabel.grid(row=49, column=57, columnspan=8,sticky='sew')
    scoreLabel.grid(row=50, column=57, columnspan=8, sticky='sew')


def menuScreen():
    screen1.grid_rowconfigure(0, weight=200)
    screen1.grid_rowconfigure(1, weight=1)
    screen1.grid_rowconfigure(2, weight=1)

    screen1.grid_columnconfigure(0, weight=10)
    screen1.grid_columnconfigure(1, weight=10)
    screen1.grid_columnconfigure(2, weight=1)

    playButton.grid(row=1, column=2, sticky='ews', padx=20, pady=0)
    leaderboardButton.grid(row=2, column=2, sticky='sew', padx=20, pady=20)
    exitButton.grid(row=3, column=2, sticky='new', padx=20, pady=10)
    spacer.grid(row=4, column=1, sticky='news')

def playScreenGrid():
    for i in range(101):
        screen1.grid_rowconfigure(index=i, weight=1,)
        screen1.grid_columnconfigure(index=i, weight=1,)
        

def reset_grid(layout):
    for i in range(51):
        layout.grid_rowconfigure(i, weight=0)
    for i in range(51):
        layout.grid_columnconfigure(i, weight=0)
    menuScreen()

def gameEntryFocusIn(event):
    global outputLabel
    global gameEntry
    global clicked
    if not clicked:
        gameEntry.delete(0, 'end')
        clicked = True

clicked = False
currentTime = 60
currentEquation = None
enteredAnswer = None
currentScore = 0
#screen1 creation
print(f"1: {5.4845 * 2}\n2: {19}")

screen1 = tk.Tk()
screen1.config(background='#1f1f1f')
screen1.geometry(f"{screen1.winfo_screenwidth()}x{screen1.winfo_screenheight()}")
screen1.title("Marly's Math Dash")
windowIcon = tk.PhotoImage(file = 'sprites/chillFish.png')
screen1.iconphoto(True, windowIcon)
screen1.attributes('-fullscreen', True )


#screen buttons
playSprite = tk.PhotoImage(file='sprites/PerfectlyCroppedPlayButton.png')
playSprite = playSprite.subsample(4, 4)
playButton = tk.Button(screen1)
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
spacer = tk.Label(
    bg=f'{screen1.cget('bg')}',
    height=10
)
menuScreen()

menuWidgetList=[playButton, leaderboardButton, exitButton]
#Game running screen_____________________________________________________
gameEntry=tk.Entry(
    font=('arial', 30, 'bold'),
    bg='#f5f5f5',
    fg='black',
    justify='center'
)
questionBox = tk.Label(
    text='87 + 32',
    font=('arial', 85, 'bold'),
    bg=f"{screen1.cget('bg')}",
    fg='#c40000',
    justify='center'
)
labelAboveEntry = tk.Label(
    text='Correct!',
    font=('arial', 85, 'bold'),
    bg=f"{screen1.cget('bg')}",
    fg='green',
    justify='center'
)
timeLabel = tk.Label(
    text=f'Time: {currentTime}',
    font=('arial', 20, 'bold'),
    bg=f'black',
    fg= 'blue'
)
scoreLabel = tk.Label(
    text=f'Score: {currentScore}',
    font=('arial', 20, 'bold'),
    bg=f'black',
    fg= 'blue'
)


print('hi')




screen1.mainloop()