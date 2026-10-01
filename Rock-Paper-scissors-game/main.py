import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("600x550")
root.configure(bg="#F4F6F8")
root.resizable(False, False)

# Score variables
user_score = 0
computer_score = 0
rounds = 0

choices = ["Rock", "Paper", "Scissors"]

# Game function
def play_game(user_choice):
    global user_score, computer_score, rounds

    computer_choice = random.choice(choices)
    rounds += 1

    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer Choice: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie!"
        result_label.config(fg="#F39C12")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        user_score += 1
        result = "You Win!"
        result_label.config(fg="#27AE60")

    else:
        computer_score += 1
        result = "Computer Wins!"
        result_label.config(fg="#E74C3C")

    result_label.config(text=result)

    score_label.config(
        text=f"Score  |  You: {user_score}    Computer: {computer_score}"
    )

    round_label.config(text=f"Round: {rounds}")


# Reset game
def reset_game():
    global user_score, computer_score, rounds

    user_score = 0
    computer_score = 0
    rounds = 0

    user_label.config(text="Your Choice: -")
    computer_label.config(text="Computer Choice: -")
    result_label.config(text="Choose Rock, Paper or Scissors", fg="#2C3E50")
    score_label.config(text="Score  |  You: 0    Computer: 0")
    round_label.config(text="Round: 0")


# Heading
heading = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 25, "bold"),
    bg="#F4F6F8",
    fg="#2C3E50"
)
heading.pack(pady=20)

# Instructions
instruction = tk.Label(
    root,
    text="Choose one option to play against the computer!",
    font=("Arial", 12),
    bg="#F4F6F8",
    fg="#555555"
)
instruction.pack(pady=5)

# Choice buttons
button_frame = tk.Frame(root, bg="#F4F6F8")
button_frame.pack(pady=25)

rock_button = tk.Button(
    button_frame,
    text="✊ Rock",
    command=lambda: play_game("Rock"),
    width=14,
    height=2,
    font=("Arial", 12, "bold"),
    bg="#3498DB",
    fg="white"
)
rock_button.grid(row=0, column=0, padx=8)

paper_button = tk.Button(
    button_frame,
    text="✋ Paper",
    command=lambda: play_game("Paper"),
    width=14,
    height=2,
    font=("Arial", 12, "bold"),
    bg="#9B59B6",
    fg="white"
)
paper_button.grid(row=0, column=1, padx=8)

scissors_button = tk.Button(
    button_frame,
    text="✌ Scissors",
    command=lambda: play_game("Scissors"),
    width=14,
    height=2,
    font=("Arial", 12, "bold"),
    bg="#E67E22",
    fg="white"
)
scissors_button.grid(row=0, column=2, padx=8)

# Round
round_label = tk.Label(
    root,
    text="Round: 0",
    font=("Arial", 12, "bold"),
    bg="#F4F6F8",
    fg="#34495E"
)
round_label.pack(pady=5)

# User choice
user_label = tk.Label(
    root,
    text="Your Choice: -",
    font=("Arial", 13, "bold"),
    bg="#F4F6F8",
    fg="#2C3E50"
)
user_label.pack(pady=5)

# Computer choice
computer_label = tk.Label(
    root,
    text="Computer Choice: -",
    font=("Arial", 13, "bold"),
    bg="#F4F6F8",
    fg="#2C3E50"
)
computer_label.pack(pady=5)

# Result
result_label = tk.Label(
    root,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 18, "bold"),
    bg="#F4F6F8",
    fg="#2C3E50"
)
result_label.pack(pady=20)

# Score
score_label = tk.Label(
    root,
    text="Score  |  You: 0    Computer: 0",
    font=("Arial", 14, "bold"),
    bg="#FFFFFF",
    fg="#2C3E50",
    padx=20,
    pady=10
)
score_label.pack(pady=10)

# Bottom buttons
bottom_frame = tk.Frame(root, bg="#F4F6F8")
bottom_frame.pack(pady=15)

reset_button = tk.Button(
    bottom_frame,
    text="Play Again / Reset",
    command=reset_game,
    width=18,
    height=2,
    font=("Arial", 11, "bold"),
    bg="#27AE60",
    fg="white"
)
reset_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(
    bottom_frame,
    text="Exit",
    command=root.destroy,
    width=12,
    height=2,
    font=("Arial", 11, "bold"),
    bg="#E74C3C",
    fg="white"
)
exit_button.grid(row=0, column=1, padx=10)

root.mainloop()