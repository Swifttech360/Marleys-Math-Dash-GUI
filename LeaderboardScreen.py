"""
Reads the names and scores the user adds to 'ADD_SCORES_HERE.txt'
#this is intended to be a teacher, who would get the best scores of all their students and add them to the txt file
"""

import tkinter as tk

def load_scores():
    scores = []
    try:
        with open('ADD_SCORES_HERE.txt', 'r') as file:
            for line in file:
                try:
                    name, score = line.strip().split(': ')
                    scores.append((name, int(score)))
                except Exception:
                    pass
    except FileNotFoundError:
        print("The file 'scores.txt' was not found.")
    return scores

def display_leaderboard(root):
    scores = load_scores()
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:10]

    for i, (name, score) in enumerate(sorted_scores):
        if  i != 9:
            rank_text = f"       {i + 1}.            {name}: {score}"
        else:
            rank_text = f"     {i + 1}.            {name}: {score}"
        rank_label = tk.Label(root, text=rank_text, bg=root.cget('bg'), fg='red', font=('Arial', 60, 'bold'))
        rank_label.grid(row=i + 1, column=1, padx=20, pady=5, sticky='w')
        

        if i == 0:
            rank_label.config(fg='orange')
        elif i == 1:
            rank_label.config(fg='#D1CFC9')
        elif i == 2:
            rank_label.config(fg='#B87333')
        
            




def open_leaderboard():
    leaderboard = tk.Toplevel()
    leaderboard.title("Leaderboard")
    #leaderboard.attributes('-fullscreen', False)
    leaderboard.attributes('-topmost', True)
    leaderboard.attributes('-topmost', False)
    leaderboard.config(bg='#1f1f1f')
    leaderboard.geometry('1920x1080')

    title_label = tk.Label(leaderboard, text="Top 10 Leaderboard", bg='#1f1f1f', fg='white', font=('Arial', 80, 'bold'))
    title_label.grid(row=0, column=1, padx=20, pady=40)

    display_leaderboard(leaderboard)

    exit_button = tk.Button(leaderboard, text="Exit", command=leaderboard.destroy, font=('Arial', 60), bg='#1f1f1f', fg='white')
    exit_button.grid(row=12, column=1, pady=20)

    for i in range(13):
        leaderboard.grid_rowconfigure(i, weight=1)
    leaderboard.grid_columnconfigure(0, weight=1)
    leaderboard.grid_columnconfigure(1, weight=1)
    leaderboard.grid_columnconfigure(2, weight=1)

    leaderboard.mainloop()


if __name__ == "__main__":
    open_leaderboard()