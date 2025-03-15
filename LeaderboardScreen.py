"""
Reads the names and scores the user adds to 'ADD_SCORES_HERE.txt'
#this is intended to be used by a teacher or host, who would get the best scores of all their students and add them
to their local 'ADD_SCORES_HERE.txt' file.
"""

import tkinter as tk

def load_scores():
    """
    opens the file to read it, strips any whitespace,
     and splits each line into two a tuple with a name and a score.
     
    In the case that the file doesn't exist, an error messge will appear
     in the console and nothing else will happen.
     
    :return: A list of tupples with names and scores.
    """
    #initializes a local 'scores' variable as a list that will contain all the scores and names as tuples
    
    scores = []
    
    try:
        with open('ADD_SCORES_HERE.txt', 'r') as file:
            for line in file:
                try:
                    name, score = line.strip().split(': ')
                    scores.append((name, float(score)))
                except Exception:
                    pass
    except FileNotFoundError:
        print("The file 'scores.txt' was not found.")
    return scores


def displayLeaderboard(root):
    """
    Gets the list of score tuples from the scores variable, sorts the tuples,
    and creates a widget to hold each tuples contents
    
    :param root: References the screen in which the leaderboard is displayed.
    
    :return: None
    """
    #sets the local variable "scores" to the before mentioned list of names and scores,
    # then uses the sorted function to sort them all and set the return to the 'sortedScores' variable
    scores = load_scores()
    sortedScores = sorted(scores, key=lambda x: x[1], reverse=True)[:10]
    
    # Writes in the aproopriate name and score for every score holder label, adjusting for the 10th rank
    #  ensure that all the labels line up properly.
    for i, (name, score) in enumerate(sortedScores):
        if  i != 9:
            rank_text = f"       {i + 1}.            {name}: {score:.2f}"
        else:
            rank_text = f"     {i + 1}.            {name}: {score:.2f}"
        rankHolderLabel = tk.Label(root, text=rank_text, bg=root.cget('bg'), fg='red', font=('Arial', 40, 'bold'))
        rankHolderLabel.grid(row=i + 1, column=1, padx=20, pady=5, sticky='w')
        
        #makes the top three scores orange(which is meant to be gold, but I like this color palet),
        # silver, and bronze.
        if i == 0:
            rankHolderLabel.config(fg='orange')
        elif i == 1:
            rankHolderLabel.config(fg='#D1CFC9')
        elif i == 2:
            rankHolderLabel.config(fg='#B87333')
        
            




def openLeaderboard():
    """
    I essentialy made this variable sequentially run the whole module and all the functions in it.
    It also assures that the meaderboard appears in from of all other windows. Just to specify, this function really
    only contains the displayLeaderboard and the mmainloop, but these two functions cause all functions in this
    submodule to run.
    
    This module also initializes the leaderboard screen, sets it to be at the top level, configures the screen,
     Configures the grid, initializes the title label, and configures the title label.
    
    :return: None
    """
    
    #sets up the screen
    LeaderBoard = tk.Toplevel()
    LeaderBoard.title("Leaderboard")
    #LeaderBoard.attributes('-fullscreen', False)
    LeaderBoard.attributes('-topmost', True)
    LeaderBoard.attributes('-topmost', False)
    LeaderBoard.config(bg='#1f1f1f')
    LeaderBoard.geometry('1920x1080')
    
    #creates andd configures the screen title label
    titleLabel = tk.Label(LeaderBoard, text="Top 10 Leaderboard", bg='#1f1f1f', fg='white', font=('Arial', 80, 'bold'))
    titleLabel.grid(row=0, column=1, padx=20, pady=40)

    #Displays the leaderboard on the LeaderBoard screen.
    displayLeaderboard(LeaderBoard)
    
    #Creates and configures the exit button with a collback function so it only kills the LeaderBoard screen
    # and not the whole program.
    exitButton = tk.Button(LeaderBoard, text="Exit", command=LeaderBoard.destroy, font=('Arial', 50), bg='#1f1f1f', fg='white')
    #exitButton.grid(row=12, column=1, pady=20)

    #Configures 13 rows ans 3 columns (only 3 columns because I found that it makes centering widgets much easier
    for i in range(13):
        LeaderBoard.grid_rowconfigure(i, weight=1)
    LeaderBoard.grid_columnconfigure(0, weight=1)
    LeaderBoard.grid_columnconfigure(1, weight=1)
    LeaderBoard.grid_columnconfigure(2, weight=1)

    #Runs the mainloop so the LeaderBoard screen opens and runs properly.
    LeaderBoard.mainloop()


#Allows the submodule to run alone as needed, and for a nice play button to appear in pycharm (and visual studio as
# well I think)
if __name__ == "__main__":
    openLeaderboard()
    
