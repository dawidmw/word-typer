import tkinter as tk
from generator import WordGenerator

TIMER = None
SCORE = 0


def start_game():
    global TIMER, SCORE
    start_button.config(text="RESET")
    if TIMER:
        window.after_cancel(TIMER)
    TIMER = 60
    SCORE = 0
    time_to_count = TIMER
    set_count(time_to_count)
    score_label.config(text=f"Score: {SCORE}")
    entry_field.config(state='normal')
    new_word()
    entry_field.focus_set()


def set_count(count):
    global TIMER
    if count > 0:
        TIMER = window.after(1000, set_count, count - 1)
        welcome_label.config(text=f"{count} seconds left")
    if count == 0:
        end_game()


def new_word():
    generated_word = word_generator.return_random_word()
    word_label.config(text=generated_word)
    success_label.config(text="")


def word_check(event):
    global SCORE
    checked_word = word_label['text']
    if checked_word == entry_field.get():
        SCORE += 1
        score_label.config(text=f"Score: {SCORE}")
        reset_entry()
        new_word()
    else:
        success_label.config(text="INCORRECT", fg='red')
        reset_entry()


def reset_entry():
    entry_field.delete(0, 'end')
    entry_field.focus_set()


def end_game():
    reset_entry()
    success_label.config(text="")
    entry_field.config(state='disabled')
    if SCORE > 0:
        welcome_label.config(text=f"Game Finished\n\n Congratulations. Your typing speed: {SCORE} words per minute.")
    else:
        welcome_label.config(text=f"Game Finished\n\n You have not typed any words.")

def quit_game():
    exit()


# ---------------- INITIALIZE WINDOW ----------------- #
window = tk.Tk()
window.title("Speed Typer")
window.geometry("500x500")
window.maxsize(500, 500)

# --------------- INITIALIZE WIDGETS ----------------- #
score_label = tk.Label(text=f"Score: {SCORE}")

welcome_label = tk.Label(
    text=f"Welcome to the Speed Typer. This app will check how many words you can type in just one"
         f"minute.\n\nPress the START button to begin playing.\n\nEach word has to be confirmed by"
         f" ENTER key.",
    wraplength=400)

word_label = tk.Label(text="", font=("Arial", 25))

start_button = tk.Button(text="START", command=start_game, padx=5, pady=5)

entry_field = tk.Entry(width=40, state='disabled')
entry_field.bind('<Return>', word_check)

success_label = tk.Label(text="")
quit_button = tk.Button(text="QUIT", command=quit_game, padx=10, pady=5)
# ---------------- PACK WIDGETS ---------------------- #
# packs all widgets into the main window
score_label.pack(pady=(10, 20))
welcome_label.pack(pady=(20, 20))
word_label.pack(pady=(30, 30))
success_label.pack(pady=(10, 10))
entry_field.pack(pady=(10, 20))
start_button.pack(pady=(3, 3))
quit_button.pack(pady=(3, 3))

word_generator = WordGenerator()

window.mainloop()
