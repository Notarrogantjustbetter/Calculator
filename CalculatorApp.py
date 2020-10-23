# Simple calculator with Python and tkinter.

from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master

        master.title("Calculator")
        self.entry = Entry(master, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.button1 = Button(master, text='1', padx=40, pady=20, command=lambda: self.press(1))  # <- From line 14 to
        self.button2 = Button(master, text='2', padx=40, pady=20, command=lambda: self.press(2))  # 31 we define our
        self.button3 = Button(master, text='3', padx=40, pady=20, command=lambda: self.press(3))  # buttons.
        self.button4 = Button(master, text='4', padx=40, pady=20, command=lambda: self.press(4))
        self.button5 = Button(master, text='5', padx=40, pady=20, command=lambda: self.press(5))
        self.button6 = Button(master, text='6', padx=40, pady=20, command=lambda: self.press(6))
        self.button7 = Button(master, text='7', padx=40, pady=20, command=lambda: self.press(7))
        self.button8 = Button(master, text='8', padx=40, pady=20, command=lambda: self.press(8))
        self.button9 = Button(master, text='9', padx=40, pady=20, command=lambda: self.press(9))
        self.button0 = Button(master, text='0', padx=40, pady=20, command=lambda: self.press(0))

        self.button_add = Button(master, text="+", padx=39, pady=20, command=self.button_add)
        self.button_equal = Button(master, text="=", padx=93, pady=20, command=self.button_equal)
        self.button_clear = Button(master, text="Clear", padx=80, pady=20, command=self.button_clear)

        self.button_subtract = Button(master, text="-", padx=41, pady=20, command=self.button_subtract)
        self.button_multiply = Button(master, text="*", padx=41, pady=20, command=self.button_multiply)
        self.button_divide = Button(master, text="/", padx=41, pady=20, command=self.button_divide)

        self.button1.grid(row=3, column=0)      # <- From line 33 to 53 we define the position of the buttons.
        self.button2.grid(row=3, column=1)
        self.button3.grid(row=3, column=2)

        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)

        self.button7.grid(row=1, column=0)
        self.button8.grid(row=1, column=1)
        self.button9.grid(row=1, column=2)

        self.button0.grid(row=4, column=0)
        self.button_clear.grid(row=4, column=1, columnspan=2)

        self.button_add.grid(row=5, column=0)
        self.button_equal.grid(row=5, column=1, columnspan=2)

        self.button_subtract.grid(row=6, column=0)
        self.button_multiply.grid(row=6, column=1)
        self.button_divide.grid(row=6, column=2)

    def press(self, number):            # <- from line 55 to 106 are the functions we use.
        current = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, str(current) + str(number))

    def button_clear(self):
        self.entry.delete(0, END)

    def button_add(self):
        first_number = self.entry.get()
        global num
        global operation
        operation = "add"
        num = int(first_number)
        self.entry.delete(0, END)

    def button_equal(self):
        second_number = self.entry.get()
        self.entry.delete(0, END)

        if operation == 'add':
            self.entry.insert(0, num + int(second_number))
        if operation == 'subtract':
            self.entry.insert(0, num - int(second_number))
        if operation == 'multiply':
            self.entry.insert(0, num * int(second_number))
        if operation == 'division':
            self.entry.insert(0, num / int(second_number))

    def button_subtract(self):
        first_number = self.entry.get()
        global num
        global operation
        operation = "subtract"
        num = int(first_number)
        self.entry.delete(0, END)

    def button_multiply(self):
        first_number = self.entry.get()
        global num
        global operation
        operation= "multiply"
        num = int(first_number)
        self.entry.delete(0, END)

    def button_divide(self):
        first_number = self.entry.get()
        global num
        global operation
        operation = "division"
        num = int(first_number)
        self.entry.delete(0, END)


root = Tk()
myapp = Calculator(root)
root.mainloop()
