import tkinter as tk
from sys import maxsize
import random as ran
from tkinter import TclError


def menuScreen():
    """
    Initially sets the menu screen widgets on the screen
    
    :return: None
    """

    screen1.grid_rowconfigure(0, weight=200)
    screen1.grid_rowconfigure(1, weight=1)
    screen1.grid_rowconfigure(2, weight=1)

    screen1.grid_columnconfigure(0, weight=10)
    screen1.grid_columnconfigure(1, weight=10)

    playButton.grid(row=1, column=1, sticky='wsn', padx=20, pady=0)
    leaderboardButton.grid(row=2, column=1, sticky='nsw', padx=20, pady=20)
    exitButton.grid(row=3, column=1, sticky='nws', padx=20, pady=0)
    spacer.grid(row=4, column=1, sticky='nws')
    titleLabel.grid(row=1, rowspan=3, column=0, pady=0, sticky='nes')
    
def setMenuScreen():
    """
    Clears all widgets, gridlines, and .after processes before placing
    all menu widgets back on the screen.
    This is intended for the menuButton
    :return:
    """
    global gameIsPlaying
    global gameStartProcesses
    gameIsPlaying = False
    gameEntry.unbind('<Return>')
    for widget in gameWidgets:
        widget.grid_forget()
    for i in range(101):
        screen1.grid_rowconfigure(i, weight=0)
        screen1.grid_columnconfigure(i, weight=0)
    menuScreen()
    
    try:
        for process in gameStartProcesses:
            screen1.after_cancel(process)
    except ValueError:
        print('An error would have occured')

def getEquation(event=None):
    """
    Generates a new randomized math equation, then set's an answer
     variable to answer of the new equation.
    Also uses a detailed algorithm to determine how many points the question will be worth
     depending on the difficulty of the math problem.
    Finally, the new equation is displayed in the "questionBox" widget.
    :param event: None
    :return: None
    """
    global currentEquation
    global answer
    global wager
    global additionalWager
    wager = 1
    additionalWager = 0
    simpleOperatorList = ('+', '-')
    advancedOperatorList = ('*', '/')
    questionTypeChoice = ran.choices((simpleOperatorList, advancedOperatorList), weights=(1, 5), k=1)[0]
    if questionTypeChoice is advancedOperatorList:
        randomOperator = ran.choices(questionTypeChoice, weights=(1, 5), k=1,)[0]
    else: randomOperator = ran.choice(questionTypeChoice)
    if questionTypeChoice == simpleOperatorList:
        randNum1 = ran.randint(0, 200)
        randNum2 = ran.randint(0, 200)
    elif questionTypeChoice == advancedOperatorList and randomOperator == '/':
        randNum1 = ran.randint(0, 100)
        randNum2 = ran.choice((1, 2, 4, 5, 10, 20, 25, 50, 100))
    elif questionTypeChoice == advancedOperatorList and randomOperator == '*':
        randNum1 = ran.randint(0, 100)
        randNum2 = ran.randint(0, 100)
    equationDisplay = f'{randNum1} {randomOperator} {randNum2}'
    answer = eval(equationDisplay)
    if answer%1 != 0:
        getEquation()
    else:
        equationDisplay = equationDisplay.replace('/','÷')
        questionBox.config(text=equationDisplay)
        wager = 1
        if questionTypeChoice == advancedOperatorList:
            additionalWager = 1
            if randNum1 not in (1, 0):
                if randNum2 not in (1, 0):
                    if randNum1 == randNum2 and randomOperator == '/':
                        pass
                    else:
                        additionalWager += ((max(randNum1, randNum2) + abs(randNum1 - randNum2))/15)
                    if randNum1%10 != 0 and randNum2%10 != 0:
                            additionalWager += 4
                    elif randNum1%10 == 0 and randNum2%10 == 0:
                        additionalWager -= 1
        else:
            if randNum1%10 != 0 or randNum2%10 !=0:
                additionalWager += (abs(max(randNum1, randNum2) - answer + abs(randNum1 - randNum2))/85)
            else: additionalWager = 1.5
            if randNum1 <=10 or randNum2 <= 10: additionalWager = 1
    if additionalWager < 0: additionalWager = 1
    

def answerCheck(event):
    global currentScore
    
    enteredAnswer = float(gameEntry.get())
    if enteredAnswer == answer:
        currentScore += (wager + additionalWager)
        labelAboveEntry.config(fg='green', text='Correct!')
    elif enteredAnswer != answer:
        currentScore -= 1.5
        labelAboveEntry.config(fg='red', text='Incorrect!')
    screen1.after(2020, lambda :labelAboveEntry.config(text=''))
    gameEntry.delete(0, 'end')
    
    scoreLabel.config(text=f'Score: {currentScore:.2f}')
    getEquation()


def gameStart():
    global gameIsPlaying
    global gameStartProcesses, afterID_01, afterID_02, afterID_03, afterID_04, afterID_05, timerCountProcessID
    gameIsPlaying = True
    questionBox.config(text='')
    labelAboveEntry.config(text='Ready?', fg='green')
    afterID_01 = screen1.after(1000, lambda: labelAboveEntry.config(text='Set...'))
    afterID_02 = screen1.after(2001, lambda: labelAboveEntry.config(text='Go!'))
    afterID_03 = screen1.after(2002, lambda: gameEntry.bind('<Return>', answerCheck))
    afterID_04 = screen1.after(2003, lambda: getEquation(None))
    afterID_05  = screen1.after(3000, lambda: labelAboveEntry.config(text=''))
    afterID_06 = screen1.after(2004, timerCount)
    gameStartProcesses = [afterID_01, afterID_02, afterID_03, afterID_04, afterID_05, timerCountProcessID]

def gameEnd():
    global gameIsPlaying
    gameIsPlaying = False
    




    
    

def playButtonClick():
    
    global clicked
    clicked = False
    for widget in menuWidgets:
        widget.grid_forget()
    
    playScreenGrid()
    
    score = 0
    scoreLabel.config(text="Score: 0")
    
    gameEntry.delete(0, 'end')
    gameEntry.insert(0, "Enter Answers Here")
    
    gameEntry.grid(row=57, rowspan=6, column=46, sticky='news', columnspan=9)
    questionBox.grid(row=49, column=45, rowspan=2, columnspan=11, sticky='nsew')
    labelAboveEntry.grid(row=54, column=45, rowspan=2, columnspan=11)
    timeLabel.grid(row=49, column=57, columnspan=8,sticky='sew')
    scoreLabel.grid(row=50, column=57, columnspan=8, sticky='sew')
    menuButton.grid(row=54, column =57, columnspan=8, sticky='new', padx=15)
    screen1.focus_set()
    gameEntry.bind('<Button-1>', gameEntryFocusIn)
    gameStart()
    


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

        
def timeDecrement():
    global currentTime
    currentTime -= 1
    
def timerCount():
    global currentTime
    if gameIsPlaying and (currentTime > 0):
        timeDecrement()
        timeLabel.config(text=f'Time: {currentTime}')
        if currentTime > 0:
            timerCountProcessID = screen1.after(1000, timerCount)
    else:
        currentTime= 60
        timeLabel.config(text= f"Time: {currentTime}")


clicked = False
gameIsPlaying = False
currentTime = 60
currentEquation = None
enteredAnswer = None
currentScore = 0
answer = None
firstQuestion=False
wager = 1
additionalWager=None
[afterID_01, afterID_02, afterID_03, afterID_04, afterID_05, timerCountProcessID] = [None, None, None, None, None, None]
gameStartProcesses = [afterID_01, afterID_02, afterID_03, afterID_04, afterID_05, timerCountProcessID]

#screen1 creation


screen1 = tk.Tk()
screen1.config(background='#1f1f1f')
screen1.geometry(f"{screen1.winfo_screenwidth()}x{screen1.winfo_screenheight()}")
screen1.title("Marly's Math Dash")
windowIcon = tk.PhotoImage(file = 'sprites/chillFish.png')
screen1.iconphoto(True, windowIcon)
screen1.attributes('-fullscreen', False )


#screen buttons
playSprite = tk.PhotoImage(file='sprites/PerfectlyCroppedPlayButton.png')
playSprite = playSprite.subsample(4, 4)
playButton = tk.Button(screen1)




playButton.config(
    command = playButtonClick,
    text='START',
    font=('arial', 50, 'bold'),
    borderwidth=2,
    relief='flat',
    bg='#c40000',
    activebackground='#940000',
    width=7,
    height = 1
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
    width=14,
    height = 1,
)
spacer = tk.Label(
    bg=f'{screen1.cget('bg')}',
    height=20
)
titleLabel = tk.Label(
    text = 'Welcome to\n Marly\'s math dash!',
    bg = 'orange',
    fg='black',
    font=('arial', 45, 'bold' ),
    
)

menuScreen()


#Game running screen_____________________________________________________

gameEntry=tk.Entry(
    font=('arial', 30, 'bold'),
    bg='#f5f5f5',
    fg='black',
    justify='center'
)


questionBox = tk.Label(
    text='',
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
menuButton = tk.Button(
    command = setMenuScreen,
    text='Menu',
    
    font=('arial', 50, 'bold'),
    bg='#c40000',
    activebackground='orange',
    #height=6
)
endGameScreen = tk.label(
    bg='orange',
    fg='black',
    
)




menuWidgets = [
    playButton,
    leaderboardButton,
    exitButton,
    spacer,
    titleLabel
]

gameWidgets = [
    gameEntry,
    questionBox,
    labelAboveEntry,
    timeLabel,
    scoreLabel,
    menuButton
]





screen1.mainloop()

