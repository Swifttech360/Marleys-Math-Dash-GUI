import tkinter as tk
import random as ran
#Imports the LeaderBoardScreen submodule, which reads the names and scores the user adds to 'ADD_SCORES_HERE.txt'
# before displaying the top ten scores on a leaderboard.
#This is intended to be used by a teacher who would get the best scores of all their students and add them to the txt
# file
import LeaderboardScreen

def menuScreen():
    """
    Initially sets the menu screen widgets on the screen
    
    :return: None
    """
#configures the grid for the menu screen
    screen1.grid_rowconfigure(0, weight=200)
    screen1.grid_rowconfigure(1, weight=1)
    screen1.grid_rowconfigure(2, weight=1)

    screen1.grid_columnconfigure(0, weight=10)
    screen1.grid_columnconfigure(1, weight=10)

    #Places all menu screen widgets onto the grid
    playButton.grid(row=1, column=1, sticky='wsn', padx=20, pady=0)
    leaderboardButton.grid(row=2, column=1, sticky='nsw', padx=20, pady=20)
    exitButton.grid(row=3, column=1, sticky='nws', padx=20, pady=0)
    spacer.grid(row=4, column=1, sticky='nws')
    titleLabel.grid(row=1, rowspan=3, column=0, pady=0, sticky='nes')
    
    
    
    
def widgetForget(widget):
    """
    Removes a widget from the grid
    
    :param widget: Determines which widget to remove from the grid
    :return: None
    """
    widget.grid_forget()
    #Removes a widget from the grid
    
def setMenuScreen():
    """
    Clears all widgets, gridlines, and .after processes before placing
    all menu widgets back on the screen.
    
    :return:
    """
    #declares all global variables
    global gameIsPlaying
    global gameStartProcesses
    global currentTime
    global gameStartProcesses
    
    currentTime = 0 #assures that the currentTime variable is set to zero so the timerCount() function stops
    #Uses a function to make sure the timer recursion loop stops if the menu button is pushed
    stopTimer()
#Cancels all .after calls inside the gameStartProcess function
    for i, process in enumerate(gameStartProcesses):
        try:
            screen1.after_cancel(process)
        except Exception:
            pass

    gameIsPlaying = False #sets the gameIsPlaying variable to False, giving the timerCount Function another flag to
    # make sure it stops the recursion loop when it is supposed to.
    
    #Unbinds the 'enter' Button from the gameEntry label so the user can't start entering answers before the game
    # starts
    gameEntry.unbind('<Return>')
    
    #Removes all widgets from the grid from when the game was playing.
    for widget in gameWidgets:
        widget.grid_forget()
        
    #Reconfigures the whole grid to have 101 rows and columns for more precise widget placement
    for i in range(101):
        screen1.grid_rowconfigure(i, weight=0)
        screen1.grid_columnconfigure(i, weight=0)
    
    #Places all menuScreen widgets into the grid
    menuScreen()
    
    #Acts as a second flag to ensure that all .after processes end properly once the menu button is pushed.
    for i, process in enumerate(gameStartProcesses):
        try:
            screen1.after_cancel(process)
        except Exception:
            pass
    
    #Resets the playButton text to it's default
    playButton.config(text='START')

def menuButtonClick():
    """
    runs the setMenuScreen function and ensures that
    all widgets in the endGameScreen are removed from the grid
    :args: None
    :return: None
    """
    #declares function globals
    global endGameWidgets
    
    #Disables the menuButton upon being clicked so it isn't clicked multiple times (which often causes unpredictable
    # behaviour)
    menuButton.config(state='disabled', bg=disabledbackground)
    
    #runs the setMenuScreen Function after one millisecond. I put this in for a particular reason I don't remember,
    # but when I remove the .after function the menuButton just doesn't work /:
    screen1.after(1, setMenuScreen)
    
    #Removes all endGame widgets from the screen.
    for widget in endGameWidgets:
        screen1.after(501, lambda w=widget: widgetForget(w))


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
    
    wager = 1 #acts as the default amount of points the user will get upon answering a question correctly
    additionalWager = 0 #acts as the additional amount of points the user will get upon answering a question correctly
    
    # as the 'random' import selects one of them. If this one is selected, the question will almost always be worth
    # less than its 'advancedOperatorList' counterpart.
    simpleOperatorList = ('+', '-')# A tuple of operators that will determine what kind of equation the user will get
  
    # as the 'random' import selects one of them. If this one is selected, the question will almost always be worth
    # more than its 'simpleOperatorList' counterpart.
    advancedOperatorList = ('*', '/')# A tuple of operators that will determine what kind of equation the user will get

    
   
    #selects one of the two operator lists by random, but with a bias towards picking 'advanceOperatorList'. This was
    # done because the division operator is particularly unlikely to get picked, as I programmed this function to get
    # a new operator in the case that the questions calculated answer isn't an integer number (which may be
    # unnecessarily difficult for younger elementary school students.
    # if the advanced list is selected, the same bias will be applied to the contents of the list. Otherwise,
    # the algorithm will simply choose between the + or - operator
    questionTypeChoice = ran.choices((simpleOperatorList, advancedOperatorList), weights=(1, 7), k=1)[0]
    if questionTypeChoice is advancedOperatorList:
        randomOperator = ran.choices(questionTypeChoice, weights=(1, 13), k=1,)[0]
    else: randomOperator = ran.choice(questionTypeChoice)
    
    
    #selects two random numbers ranged 0 - 200 if questionTypeChoice == simpleOperatorList, otherwise, the integers
    # are ranged from 0 - 200
    if questionTypeChoice == simpleOperatorList:
        randNum1 = ran.randint(0, 200)#the first random number in the upcoming equation
        randNum2 = ran.randint(0, 200)#the second random number in the upcoming equation
    elif questionTypeChoice == advancedOperatorList:
        randNum1 = ran.randint(0, 100)
        randNum2 = ran.randint(0, 100)
    
    #Creates a string using the two random numbers and the operator.
    #This string is used to display the equation to the user, along with
    # determining the answer to the equation using the Eval function
    equationDisplay = f'{randNum1} {randomOperator} {randNum2}'
    try:
        answer = eval(equationDisplay)
    except Exception:
        pass
    
    #get's a new equation using a recursive loop if the answer's remainder isn't an integer.
    if answer%1 != 0:
        getEquation()
    
    #Runs an extensive algorithm to determine what to set the additional
    # wager value to, based on the calculated difficulty of the problem
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
                additionalWager += (abs(max(randNum1, randNum2) - answer + abs(randNum1 - randNum2))/70)
            else: additionalWager = 1.5
            if randNum1 <=10 or randNum2 <= 10: additionalWager = 1
    if additionalWager < 0: additionalWager = 1
    

def answerCheck(event):
    """
    Adds the wager and additional wager to the user's score (currentScore) if the entered
       answer matched the calculated answer. Otherwise, 1.5 points are subtracted from the currentScore value.
    The function then displays green or red text in the 'labelAboveEntry' label (amazing name, I know) to state if
    the answer was correct or incorrect.
    
    Lastly, the function will delete all
    :param event: Only used as a placeholder
    :return: None
    """
    
    global currentScore, questionsAnswered, enteredAnswer
    
    try:
        enteredAnswer = float(gameEntry.get()) #Variable holds the string entered by the user as a floating point number
    except Exception:
        print('invalid Input')
    #I decided to describe this section of text in the docstring.
    if enteredAnswer == answer:
        currentScore += (wager + additionalWager)
        questionsAnswered += 1
        labelAboveEntry.config(fg='green', text='Correct!')
    elif enteredAnswer != answer:
        currentScore -= 1.5
        labelAboveEntry.config(fg='red', text='Incorrect!')
    screen1.after(2020, lambda :labelAboveEntry.config(text=''))
    gameEntry.delete(0, 'end')
    
    scoreLabel.config(text=f'Score: {currentScore:.2f}')
    getEquation()


def gameStart():
    """
    Starts the game by initializing necessary variables, binding events, and starting the timer.
    
    :return: None
    """
    global gameIsPlaying
    global gameStartProcesses, afterID_01, afterID_02, afterID_03, afterID_04, afterID_05, timerCountProcessID
    gameIsPlaying = True # Sets the gameIsPlaying flag to True
    questionBox.config(text='') # Clears the questionBox
    labelAboveEntry.config(text='Ready?', fg='green') # Sets the labelAboveEntry text to 'Ready?'
    
    # Sets up the game start processes with delays, whilst giving each .after process an ID so
    # they can be canceled properly if needed
    afterID_01 = screen1.after(1, lambda: labelAboveEntry.config(text='Set...'))
    afterID_02 = screen1.after(1001, lambda: labelAboveEntry.config(text='Go!'))
    afterID_03 = screen1.after(1002, lambda: gameEntry.bind('<Return>', answerCheck))
    afterID_04 = screen1.after(1003, lambda: getEquation(None))
    afterID_06 = screen1.after(1004, timerCount)
    afterID_05  = screen1.after(2000, lambda: labelAboveEntry.config(text=''))
    
    #initializes a list of all the gameStartProcess
    gameStartProcesses = [afterID_01, afterID_02, afterID_03, afterID_04, afterID_05, timerCountProcessID]


def stopTimer():
    """
    Stops the timer by canceling the .after process.
    
    :return: None
    """
    global timerCountProcessID
    if timerCountProcessID is not None:
        try:
            screen1.after_cancel(timerCountProcessID) # Cancels the timer process
        except Exception:
            pass
        timerCountProcessID = None # Resets the timer process ID to None

    
    

def playButtonClick():
    """
    Stops any previous timer function instances,
     handles the click event for the play button,
      and places all the game variables .
    
    :return: None
    """
    
    global clicked
    global currentTime
    global gameIsPlaying
    global endGameWidgets
    global currentScore, questionsAnswered
    # Stops any existing timer
    stopTimer()
    
    #Assures that the menuButton isn't clicked until at least
    # one second after the gameStart function runs to avoid unpredictable behavior.
    screen1.after(1000, lambda: menuButton.config(state='normal', bg='#c40000'))
    
    clicked = False # Resets the clicked flag
    
    # Resets the timer
    currentTime = 120
    
    # Resets the score and question count
    [currentScore, questionsAnswered] = [0, 0]
    
    #Updates the time label
    timeLabel.config(text="Time: 120")
    
    # Removes all widgets from the menu screen
    try:
        for widget in menuWidgets:
            widget.grid_forget()
    except Exception:
        pass
    # Removes all widgets from the end game screen
    try:
        for widget in endGameWidgets:
            widget.grid_forget()
    except Exception:
        print('endgamewidget Undefined')
    
    # Configures the game screen grid
    playScreenGrid()
    
    # Updates the score label
    scoreLabel.config(text="Score: 0")
    
    #replaces and old or nonexistant text in the gameEntry widget with "Enter Answers Here"
    gameEntry.delete(0, 'end')
    gameEntry.insert(0, "Enter Answers Here")
    
    #places all the game variables into the grid
    gameEntry.grid(row=57, rowspan=6, column=46, sticky='news', columnspan=9)
    questionBox.grid(row=49, column=45, rowspan=2, columnspan=11, sticky='nsew')
    labelAboveEntry.grid(row=54, column=45, rowspan=2, columnspan=11)
    timeLabel.grid(row=49, column=57, columnspan=8,sticky='sew')
    scoreLabel.grid(row=50, column=57, columnspan=8, sticky='sew')
    menuButton.grid(row=54, column =57, columnspan=8, sticky='new', padx=15)
    
    #Unfocuses the gameEntry so assure that it's command functions aren't intervened
    screen1.focus_set()
    
    #binds leftClick to a function that removes the entryFields text when clicked.
    gameEntry.bind('<Button-1>', gameEntryFocusIn)
    
    #clears questionBox of old text, sets the label above the entry to 'ready,
    # runs the gamestart function after one second, sets the gameIsPlaying var to True, and enables the playButton.
    questionBox.config(text='')
    labelAboveEntry.config(text='Ready?')
    screen1.after(1000, gameStart)
    gameIsPlaying = True
    playButton.config(state='normal')
    
    


def playScreenGrid():
    """
    Configures the grid to have 101 rows and columns.
    
    :return: None
    """
    
    for i in range(101):
        screen1.grid_rowconfigure(index=i, weight=1,)
        screen1.grid_columnconfigure(index=i, weight=1,)
        


def gameEntryFocusIn(event):
    """
    deletes all text in the gameEntry Label
    :param event:
    :return:
    """
    global outputLabel
    global gameEntry
    global clicked
    if not clicked:
        gameEntry.delete(0, 'end')
        clicked = True

        
def timeDecrement():
    """
    decrements the currentTime variable if gameIsPlaying is True, otherwise it kills the timerCount recursiveLoop.
    :return: None
    """
    global currentTime, timerCountProcessID
    if gameIsPlaying:
        currentTime -= 1
    else: screen1.cancel(timerCountProcessID)
    
def timerCount():
    """
    Manages the countdown timer for the game.
    
    :return: None
    """
    global currentTime, timerCountProcessID
    global gameStartProcesses
    try:
        if timerCountProcessID is not None:
            screen1.after_cancel(timerCountProcessID)# Cancels the timer process
    except Exception:
            pass
    
    # Decrements the timer after one second if gameIsPlaying is true and the time variable is more than zero.
    if gameIsPlaying and (currentTime > 0):
        timeDecrement()
        timeLabel.config(text=f'Time: {currentTime}')
        if currentTime > 0 and gameIsPlaying:
            timerCountProcessID = screen1.after(1000, timerCount)
            
    # Otherwise, the time is reset and the timer is stopped
    else:
        
        currentTime= 120
        timeLabel.config(text= f"Time: {currentTime}")
        stopTimer()
    #switches to the gameOver screen if the timer reaches 0
    if currentTime == 0:
        gameEnd()

def gameEnd():
    """
    Ends the game, displaying the end game screen and final scores.
    
    :return: None
    """
    
    global gameWidgets
    global gameIsPlaying
    gameIsPlaying = False #Variable used in the flags of other functions, preventing them from
    # running if this variable is set to false.
    
    #removes all gameScreen widgets from the grid before placing the game over screen.
    for widget in gameWidgets:
        widget.grid_forget()
        
    #Places all endGame widgets into the screen, configuring some of them as well
    endGameTitle.grid(row=30, column=36, columnspan=28, rowspan=12, pady=0, padx=0, sticky='sewnews')
    endGameScoreLabel.grid(row=55, column=40, columnspan=8, sticky='w'  )
    endGameScoreLabel.config(text=f'Score: {currentScore:.2f}')
    correctAnswersLabel.grid(row=60, column=40, columnspan=8, sticky='w'  )
    correctAnswersLabel.config(text=f'Correct Answers: {questionsAnswered}')
    playButton.grid(row=80, column=45, sticky='news', padx=20, pady=0)
    playButton.config(text= 'Again?')
    


clicked = False # Flag to track if the entry field has been clicked
gameIsPlaying = False # Flag to track if the game is currently playing
currentTime = 120 # Initial time for the game
currentEquation = None# Stores the equation of the current problem
enteredAnswer = None# Stores the user's entered answer
currentScore = 0# Stores the current score
answer = None# Stores the correct answer
wager = 1# Initial wager for the game
additionalWager=None# Additional wager based on question difficulty
questionsAnswered = 0# Counter for the number of questions answered

# IDs for .after processes
[afterID_01, afterID_02, afterID_03, afterID_04, afterID_05, timerCountProcessID] = [None, None, None, None, None, None]
# List of .after process IDs
gameStartProcesses = [afterID_01, afterID_02, afterID_03, afterID_04, afterID_05, timerCountProcessID]

disabledbackground = '#9C3C3C'# Background color for disabled buttons
enabledBackground = '#c40000'# Background color for enabled buttons



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



#configures all the main menu widgets
playButton.config(
    command = lambda:
        (screen1.after(800, playButtonClick),
        playButton.config(state='disabled', bg=disabledbackground),
        screen1.after(802, playButton.config(bg='#c40000'))
),
    text='START',
    font=('arial', 50, 'bold'),
    borderwidth=2,
    relief='flat',
    bg='#c40000',
    activebackground='#940000',
    disabledforeground='black',
    width=7,
    height = 1
    )


leaderboardButton = tk.Button(screen1)

leaderboardButton.config(
    command = lambda: LeaderboardScreen.openLeaderboard(), #calls the LeaderBoardScreen module and all it's functions
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
    text = 'Welcome to\n Marly\'s Math Dash!',
    bg = 'orange',
    fg='black',
    font=('arial', 45, 'bold' ),
    
)

#initially sets the menu screen, setting all the widgets in place using
# the manuScreen function
menuScreen()


# creates/configures all widgets that appear after the playButton is clicked
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
    command = menuButtonClick,
    text='Menu',
    font=('arial', 50, 'bold'),
    disabledforeground='black',
    bg=disabledbackground,
    state='disabled',
    activebackground='orange',
    #height=6
)


#Creates and configures all widgets that appear
# after the currentScore variable reaches 0
endGameTitle = tk.Label(
    bg='orange',
    #screen1.cget('bg'),
    fg='black',
    text='Time\'s up!',
    font=('arial', 80, 'bold'),
    #height=2,
    
)
endGameScoreLabel = tk.Label(
    text=f'Score: {currentScore}',
    font=('arial', 65, 'bold'),
    bg=screen1.cget('bg'),
    fg='blue'
    
)

correctAnswersLabel= tk.Label(
    text=f'Score: {currentScore}',
    font=('arial', 65, 'bold'),
    bg=screen1.cget('bg'),
    fg='blue'
    )







#stores every screens widgets in lists which can be iterated upon so all
# the widgets can be removed from the screen quickly
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

endGameWidgets = [
    endGameTitle,
    endGameScoreLabel,
    correctAnswersLabel
]



#Starts the main event loop so the GUI can open properly
screen1.mainloop()

