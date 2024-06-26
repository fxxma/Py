import tkinter as tk
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    print(count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = tk.Label(text="Timer", font=(FONT_NAME, 24, "bold"))
label.grid(row=0, column=1)

check_mark = tk.Label(text="V")
check_mark.grid(row=3, column=1)

button1 = tk.Button(text="Start")
button1.grid(row=2, column=0)

button2 = tk.Button(text="Reset")
button2.grid(row=2, column=2)

window.mainloop()
