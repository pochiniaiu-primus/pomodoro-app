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
WORK_MIN = 0.25  # 15 seconds for testing
SHORT_BREAK_MIN = 0.3  # 18 seconds for testing
LONG_BREAK_MIN = 1  # 60 seconds for testing
reps = 0
sec_in_one_min = 60
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    global reps
    reps += 1
    global sec_in_one_min
    work_sec = round(WORK_MIN * sec_in_one_min)
    short_break_sec = round(SHORT_BREAK_MIN * sec_in_one_min)
    long_break_sec = round(LONG_BREAK_MIN * sec_in_one_min)

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", foreground=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time", foreground=GREEN)

    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global sec_in_one_min
    count_min = math.floor(count / sec_in_one_min)
    count_sec = count % sec_in_one_min
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, FONT_SIZE, TEXT_TYPEFACE))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, TEXT_SIZE, TEXT_TYPEFACE))
# timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, TEXT_SIZE, TEXT_TYPEFACE))
timer_label.grid(column=1, row=0)
timer_label.config(background=YELLOW, foreground=GREEN)

start_button = Button(text="Start", font=("Arial", 12, "bold"),
                      highlightthickness=0, command=start_timer, state="normal")
start_button.grid(column=0, row=2)
start_button.config(background=YELLOW, foreground=BUTTON_FG)

reset_button = Button(text="Reset", font=("Arial", 12, "bold"),
                      highlightthickness=0, command=reset_timer, state="disabled")
reset_button.grid(column=2, row=2)
reset_button.config(background=YELLOW, foreground=BUTTON_FG)

check_marks_label = Label(font=("Arial", 12, "bold"), highlightthickness=0)
check_marks_label.grid(column=1, row=2)
check_marks_label.config(background=YELLOW, foreground=GREEN)
window.mainloop()
