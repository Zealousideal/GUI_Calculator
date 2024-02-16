from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)


def button_click(number):
    # e.delete(0, END)
    Button(bg="red", fg="red")
    font=('Helvetica', 20, 'bold')
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_clear():
    e.delete(0, END)


def button_equals():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))

    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))

    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))

    elif math == "division":
        e.insert(0, f_num / int(second_number))


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def onclick():
    Button(bg="white")


# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="black", fg="grey", font=('Helvetica', 20, 'bold'))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="black", fg="white", font=('Helvetica', 20, 'bold'))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="black", fg="white", font=('Helvetica', 20, 'bold'))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="black", fg="white", font=('Helvetica', 20, 'bold'))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="black", fg="white", font=('Helvetica', 20, 'bold'))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="black", fg="white", font=('Helvetica', 20, 'bold'))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="black", fg="white", font=('Helvetica', 20, 'bold'))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="black", fg="white", font=('Helvetica', 20, 'bold'))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="black", fg="white", font=('Helvetica', 20, 'bold'))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="black", fg="white", font=('Helvetica', 20, 'bold'))

button_addition = Button(root, text="+", padx=40, pady=20, command=button_add,bg="cyan", fg="white", font=('Helvetica', 20, 'bold'))
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equals,bg="cyan", fg="white", font=('Helvetica', 20, 'bold'))
button_clear_ = Button(root, text="Clear", padx=12, pady=20, command=button_clear,bg="cyan", fg="white", font=('Helvetica', 20, 'bold'))
button_multiply_ = Button(root, text="x", padx=39, pady=20, command=button_multiply,bg="cyan", fg="white", font=('Helvetica', 20, 'bold'))
button_subtract_ = Button(root, text="-", padx=44, pady=20, command=button_subtract,bg="cyan", fg="white", font=('Helvetica', 20, 'bold'))
button_divide_ = Button(root, text="/", padx=44, pady=20, command=button_divide,bg="cyan", fg="white", font=('Helvetica', 20, 'bold'))

# Put buttons on the screen
button_0.grid(row=4, column=1)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_addition.grid(row=1, column=3)
button_equal.grid(row=4, column=0)
button_clear_.grid(row=4, column=2)
button_subtract_.grid(row=2, column=3)
button_multiply_.grid(row=3, column=3)
button_divide_.grid(row=4, column=3)

root.mainloop()