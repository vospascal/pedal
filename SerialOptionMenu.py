import tkinter as tk
from tkinter import Frame, Label, Entry, Button, OptionMenu, StringVar, DoubleVar, Scale, HORIZONTAL, LEFT

class SerialOptionMenu(tk.Frame):
    def __init__(self, root, text, list, row, column):
        super().__init__(root)

        self.label = Label(self, text=text)
        self.label.grid(row=row, column=column)
        self.status = StringVar()
        self.optionList = OptionMenu(self, self.status, *list)
        self.optionList.grid(row=row, column=column+1)

    def get(self):
        return self.status