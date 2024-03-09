from tkinter import *
from tkinter import messagebox

FONT = ("Arial", 20, "bold")
FONT_BUTTON = ("Arial", 10, "bold")
GREY_COLOUR = "#808080"
ORANGE_COLOUR = "#b5520b"
window = Tk()
window.title("CALCULATOR")
window.geometry("250x350")
window.resizable(0, 0)
window.config(bg="black")

a = 0
formula = ""


def show(value):
    global a
    global formula
    if value == "%":
        value = "/100"
    formula += value
    display_entry.insert(a, value)
    a = a + 1


def clear():
    global formula
    display_entry.delete(0, END)
    formula = ""


def equal():
    try:
        global formula
        result = ""
        result = eval(formula)
        clear()
        display_entry.insert(0, result)
    except:
        messagebox.showerror(title="ERROR!", message="Enter a valid number.")


display_entry = Entry(width=40, font=FONT, bg="black", highlightthickness=0, fg="white")
display_entry.place(x=0, y=10)

clear_button = Button(command=clear, text="C", font=FONT_BUTTON, width=5, bg=ORANGE_COLOUR, fg="black")
clear_button.place(x=10, y=60)

percent_button = Button(command=lambda: show("%"), text="%", font=FONT_BUTTON, width=5, bg=ORANGE_COLOUR, fg="black")
percent_button.place(x=70, y=60)

div_button = Button(command=lambda: show("/"), text="/", font=FONT_BUTTON, width=5, bg=ORANGE_COLOUR, fg="black")
div_button.place(x=130, y=60)

mul_button = Button(command=lambda: show("*"), text="x ", font=FONT_BUTTON, width=5, bg=ORANGE_COLOUR, fg="black")
mul_button.place(x=190, y=60)

sev_button = Button(command=lambda: show("7"), text="7", font=FONT_BUTTON, width=5, bg=GREY_COLOUR, fg="white")
sev_button.place(x=10, y=120)

eig_button = Button(command=lambda: show("8"), text="8", font=FONT_BUTTON, width=5, bg=GREY_COLOUR, fg="white")
eig_button.place(x=70, y=120)

nin_button = Button(command=lambda: show("9"), text="9", font=FONT_BUTTON, width=5, bg=GREY_COLOUR, fg="white")
nin_button.place(x=130, y=120)

add_button = Button(command=lambda: show("+"), text="+", font=FONT_BUTTON, width=5, bg=ORANGE_COLOUR, fg="black")
add_button.place(x=190, y=120)

fou_button = Button(command=lambda: show("4"), text="4", font=FONT_BUTTON, width=5, bg=GREY_COLOUR, fg="white")
fou_button.place(x=10, y=180)

fiv_button = Button(command=lambda: show("5"), text="5", font=FONT_BUTTON, width=5, bg=GREY_COLOUR, fg="white")
fiv_button.place(x=70, y=180)

six_button = Button(command=lambda: show("6"), text="6", font=FONT_BUTTON, width=5, bg=GREY_COLOUR, fg="white")
six_button.place(x=130, y=180)

sub_button = Button(command=lambda: show("-"), text="-", font=FONT_BUTTON, width=5, bg=ORANGE_COLOUR, fg="black")
sub_button.place(x=190, y=180)

zer_button = Button(command=lambda: show("0"), text="0", font=FONT_BUTTON, width=5, bg=GREY_COLOUR, fg="white")
zer_button.place(x=10, y=240)

one_button = Button(command=lambda: show("1"), text="1", font=FONT_BUTTON, width=5, bg=GREY_COLOUR, fg="white")
one_button.place(x=70, y=240)

two_button = Button(command=lambda: show("2"), text="2", font=FONT_BUTTON, width=5, bg=GREY_COLOUR, fg="white")
two_button.place(x=130, y=240)

thr_button = Button(text="3", font=FONT_BUTTON, width=5, bg=GREY_COLOUR, fg="white")
thr_button.place(x=190, y=240)

dot_button = Button(command=lambda: show("."), text=".", font=FONT_BUTTON, width=5, bg=ORANGE_COLOUR, fg="black")
dot_button.place(x=10, y=300)

equ_button = Button(command=equal, text="=", font=FONT_BUTTON, width=20, bg=ORANGE_COLOUR, fg="black")
equ_button.place(x=70, y=300)

window.mainloop()
