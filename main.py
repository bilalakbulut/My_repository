from tkinter import *
from random import *
import time

GRAY = "#606060"
PURPLE = "#000099"


def get_rock():
    computer_choice = "Scissors"
    if computer_choice == "Paper":
        lose()
    elif computer_choice == "Rock":
        draw()
    else:
        win()


def get_paper():
    computer_choice = "Scissors"
    if computer_choice == "Scissors":
        lose()
    elif computer_choice == "Paper":
        draw()
    else:
        win()


def get_scissors():
    computer_choice = "Scissors"
    if computer_choice == "Rock":
        lose()
    elif computer_choice == "Scissors":
        draw()
    else:
        win()


def changing_image(image_name):
    global rock_paper_scissor_img
    rock_paper_scissor_img = PhotoImage(file=image_name)
    canvas.create_image(800, 600, image=rock_paper_scissor_img)
    canvas.config(bg=GRAY, highlightthickness=0)

    rock_button.destroy()
    paper_button.destroy()
    scissors_button.destroy()


def win():
    global user_wins, restart_button, quit_button
    user_wins += 1
    win_boards()
    print("you won")
    changing_image("you_win.png")
    restart_button = Button(text="Play again", command=restart, highlightbackground=GRAY)
    restart_button.place(x=750, y=900)
    quit_button = Button(text="Quit", command=quit_game, highlightbackground=GRAY)
    quit_button.place(x=750, y=100)


def draw():
    global restart_button, quit_button
    print("you draw")
    changing_image("you_tied.png")
    win_boards()
    restart_button = Button(text="Play again", command=restart, highlightbackground=GRAY)
    restart_button.place(x=750, y=900)
    quit_button = Button(text="Quit", command=quit_game, highlightbackground=GRAY)
    quit_button.place(x=750, y=100)


def lose():
    global computer_wins, restart_button, quit_button
    computer_wins += 1
    win_boards()
    print("you lost")
    changing_image("you_lost.png")
    restart_button = Button(text="Play again", command=restart, highlightbackground=GRAY)
    restart_button.place(x=750, y=900)
    quit_button = Button(text="Quit", command=quit_game, highlightbackground=GRAY)
    quit_button.place(x=750, y=100)


def win_boards():
    comp_win_label = Label(text=f"Comp wins {computer_wins}", highlightbackground=GRAY, font=("Courier", 35, "bold"))
    comp_win_label.place(x=0, y=0)

    user_win_label = Label(text=f"User wins {user_wins}", highlightbackground=GRAY, font=("Courier", 35, "bold"))
    user_win_label.place(x=1360, y=0)


def restart():
    global rock_paper_scissor_img, rock_button, paper_button, scissors_button
    rock_paper_scissor_img = PhotoImage(file="rps_image.png")
    canvas.create_image(800, 600, image=rock_paper_scissor_img)
    canvas.pack()

    rock_button = Button(text="Rock", highlightbackground=PURPLE, highlightthickness=0, command=get_rock)
    rock_button.place(x=285, y=900)

    paper_button = Button(text="Paper", highlightbackground=PURPLE, highlightthickness=0, command=get_paper)
    paper_button.place(x=750, y=900)

    scissors_button = Button(text="Scissors", highlightbackground=PURPLE, highlightthickness=0, command=get_scissors)
    scissors_button.place(x=1200, y=900)


def quit_game():
    quit()


window = Tk()
window.title("Rock paper scissors")
options = ["Rock", "Paper", "Scissors"]
user_wins = 0
computer_wins = 0

canvas = Canvas(width=1600, height=1200, bg=GRAY, highlightthickness=0)


rock_paper_scissor_img = PhotoImage(file="rps_image.png")
canvas.create_image(800, 600, image=rock_paper_scissor_img)
canvas.pack()

rock_button = Button(text="Rock", highlightbackground=PURPLE, command=get_rock)
rock_button.place(x=285, y=900)

paper_button = Button(text="Paper", highlightbackground=PURPLE, command=get_paper)
paper_button.place(x=750, y=900)

scissors_button = Button(text="Scissors", command=get_scissors, highlightbackground=PURPLE)
scissors_button.place(x=1200, y=900)

restart_button = Button()
quit_button = Button()

window.mainloop()
