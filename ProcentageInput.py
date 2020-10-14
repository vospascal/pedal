import tkinter as tk
from tkinter import Frame, Label, Entry, Button, OptionMenu, StringVar, DoubleVar, Scale, HORIZONTAL


class ProcentageInput(tk.Frame):
    def __init__(self, master, text, index, varValue, set_chart_point, row):
        super().__init__(master)
        self.label = Label(self, text=text, width=12)
        self.label.grid(row=row, column=0)
        self.input = Entry(self, width=12)
        self.input.insert(0, varValue)
        # self.text_0.configure(state='readonly')
        self.input.bind('<FocusOut>', (lambda _: set_chart_point(self.input, index)))
        self.input.grid(row=row, column=1)
