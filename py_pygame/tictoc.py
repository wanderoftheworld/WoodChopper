from tkinter import *

def player1_click(event):
    if event.widget.cget('text') == ' ':
        event.widget.config(text='X')
        event.widget.cget('text')
    return

def player2_click(event):
    if event.widget.cget('text') == ' ':
        event.widget.config(text='O')
        event.widget.cget('text')
    return

def check_row():
    # check rows
    for i in range(3):
        if ((top[i * 3].cget('text') == top[i * 3 + 1].cget('text') == top[i * 3 + 2].cget('text') == 'X') |
                top[i * 3].cget('text') == top[i * 3 + 1].cget('text') == top[i * 3 + 2].cget('text') == 'O'):
            game_won = True

def check_column():
    for i in range(3):
        if ((top[i].cget('text') == top[i + 3].cget('text') == top[i + 6].cget('text') == 'X') |
                top[i].cget('text') == top[i + 3].cget('text') == top[i + 6].cget('text') == 'O'):
            game_won = True

def check_diagonal():
    if (top[0].cget('text') == top[4].cget('text') == top[8].cget('text') == 'X' |
            top[2].cget('text') == top[4].cget('text') == top[6].cget('text') == 'O'):
        game_won = True

def reset():
    for i in range(10):
        top[i].config(text=' ')

# Main function

top = Tk()
top.title('Tic-Tac-Toe')

# Creating buttons
b = []

for i in range(10):
    b.append(Button(top, width = 5, font = ('arial', 40)))
    b[i].grid(row=int(i/3)+1, column=i%3+1)

# Clicking buttons
for i in range(10):
    b[i].bind('<Button-1>', player1_click)
    b[i].bind('<Button-2>', player2_click)

check_for_winner = Label(top, fg = 'blue', text = '')
check_for_winner.grid(row = 4, column = 1)

continue_game = Label(top, fg = 'blue', text = '')
continue_game.grid(row = 5, column = 1)

game_won = False
won = Label(top, fg = 'green', text = '')
won.grid(row = 4, column = 4)

# calling function to check the winner in every click
for i in range(10):
    b[i].bind('<Button-1>', lambda x: check_row())
    b[i].bind('<Button-2>', lambda x: check_column())
    b[i].bind('<Button-1>', lambda x: check_diagonal())

reset_game = Button(top, width = 10, text = 'Reset Game', command = reset)
reset_game.grid(row = 5, column = 4)

top.mainloop()
