import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps=0
work=[1,3,5,7]
short_break=[2,4,6]
time=""
timer_on=""
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer_on
    window.after_cancel(timer_on)
    time="00:00"
    canvas.itemconfig(timer,text=time)
    ticks.config(text="")
    t.config("Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps,work,short_break,tick
    reps+=1
    if reps in work :
        countdown(WORK_MIN*60)
        t.config(text="Work", bg=YELLOW, fg=GREEN,highlightthickness=0)


    if reps in short_break:
        countdown(SHORT_BREAK_MIN*60)
        t.config(text="Break", bg=YELLOW,fg=PINK,highlightthickness=0)
    if reps%2==0 and reps%8==0:
        countdown(LONG_BREAK_MIN*60)
        t.config(text="Break", bg=YELLOW,fg=RED,highlightthickness=0)
        reps=0



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global time
    sec=round(count%60)
    minute=math.floor(count / 60)

    if sec<10:
        sec=f"0{sec}"
    if minute<10:
        minute=f"0{minute}"

    time= f"{minute}:{sec}"
    global timer_on
    canvas.itemconfig(timer,text=time)
    if count>0:
        timer_on=window.after(1000,countdown,count-1)
    else:
        start()
        global tick
        ticks.config(text=tick)
        tick += " ✔"

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


canvas= Canvas(width=208,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(103,112, image=tomato)
timer=canvas.create_text(100,135,text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


t=Label(text="Timer",fg=GREEN, font=(FONT_NAME,50,"normal"),bg=YELLOW,highlightthickness=0)
t.grid(row=0,column=1)

s=Button(text="Start",width=10, command=start)
s.grid(row=2,column=0)

r=Button(text="Reset",width=10,command=reset)
r.grid(row=2,column=2)

tick= "✔"

ticks=Label(fg=GREEN, font=(FONT_NAME,10,"bold"),anchor="w",bg=YELLOW,highlightthickness=0)
ticks.grid(row=2, column=1)





window.mainloop()