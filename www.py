from tkinter import *
from tkinter import messagebox

age_app = Tk()

age_app.title("jamal project")


age_app.geometry("400x200")


the_text = Label(age_app, text="write your age", height=2, font=("Arial", 20))
the_text.pack()

age = StringVar()


age.set("00")


age_input = Entry(age_app, width=2, font=("Arial", 30), textvariable=age)
age_input.pack()


def calc():

    the_age_value = age.get()

    months = int(the_age_value) * 12
    week = months * 4
    days = int(the_age_value) * 365

    line_one = f"your age in months is: {months}"
    line_two = f"your age in week is: {week}"
    line_three = f"your age in days is: {days}"

    print(line_one)
    print(line_two)
    print(line_three)

    all_lines = [line_one, line_two, line_three]

    messagebox.showinfo("your age in all time units", "\n".join(all_lines))


btn = Button(
    age_app,
    text="calculate age",
    width=20,
    height=2,
    bg="#e91e63",
    fg="white",
    borderwidth=0,
    command=calc,
)
btn.pack()


age_app.mainloop()
