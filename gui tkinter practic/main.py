from tkinter import *


def click():
    print("Button was clicked")


window = Tk()
window.geometry("400x400")
window.title("Textbook Value Calculator")

label = Label(window, text="Click me window!", font=("Arial", 10, "bold"))
label.place(x=0, y=100)

button_01 = Button(window, text="click me", command=click, font=("Arial", 10, "bold"))
button_01.pack()

window.mainloop()
