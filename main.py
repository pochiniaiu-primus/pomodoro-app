from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TEXT_TYPEFACE = "bold"
TEXT_SIZE = 24
BUTTON_FG = "black"
FONT_SIZE = 35
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(2 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    sec_in_one_min = 60
    count_min = math.floor(count / sec_in_one_min)
    count_sec = count % sec_in_one_min
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

fg = GREEN
text = "✔"
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, FONT_SIZE, TEXT_TYPEFACE))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, TEXT_SIZE, TEXT_TYPEFACE))
# timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, TEXT_SIZE, TEXT_TYPEFACE))
timer_label.grid(column=1, row=0)
timer_label.config(background=YELLOW, foreground=GREEN)


start_button = Button(text="Start", font=("Arial", 12, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
start_button.config(background=YELLOW, foreground=BUTTON_FG)

reset_button = Button(text="Reset", font=("Arial", 12, "bold"), highlightthickness=0)
reset_button.grid(column=2, row=2)
reset_button.config(background=YELLOW, foreground=BUTTON_FG)

check_marks_label = Label(text="✔", font=("Arial", 12, "bold"), highlightthickness=0)
check_marks_label.grid(column=1, row=2)
check_marks_label.config(background=YELLOW, foreground=GREEN)
window.mainloop()
