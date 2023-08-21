from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
PURE_RED = "#FF0000"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
count_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(count_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="", fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def exit_program():
    window.destroy()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_seconds)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_seconds)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global count_timer
        count_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "🍎"
        checkmark_label.config(text=mark, fg=PURE_RED)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)
# create a canvas and place image inside
canvas = Canvas(width=276, height=184, bg=YELLOW, highlightthickness=0)
work_image = PhotoImage(file="./images/image_work.png")
canvas.create_image(138, 92, image=work_image)
timer_text = canvas.create_text(190, 40, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=3, column=2)
# create  timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW,)
timer_label.config(padx=10, pady=20)
timer_label.grid(row=2, column=2)
# create a button to start the timer
start_button = Button(text="Start", font=FONT_NAME, command=start_timer)
start_button.grid(row=4, column=1)
# create a button to reset the timer
reset_button = Button(text="Reset", font=FONT_NAME, command=reset_timer)
reset_button.grid(row=4, column=3)
# create a button to quit the app
quit_button = Button(text="Exit", font=FONT_NAME, bg=PURE_RED, command=exit_program)
quit_button.grid(row=1, column=4)
# create a checkmark
checkmark_label = Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW,)
checkmark_label.grid(row=5, column=2)
window.mainloop()
