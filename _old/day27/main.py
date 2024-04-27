import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=900, height=600)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


def button_clicked():
    print("I got clicked.")
    my_label.config(text="Button got clicked")


# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button1 = tkinter.Button(text="Click Me", command=button_clicked)
button1.grid(column=2, row=0)
# Entry

my_input = tkinter.Entry(width=10)
print(my_input.get())
my_input.grid(column=3, row=2)

window.mainloop()