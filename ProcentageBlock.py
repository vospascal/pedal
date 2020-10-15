import tkinter as tk
from tkinter import Frame, Label, Entry, Button, OptionMenu, StringVar, DoubleVar, Scale, HORIZONTAL
from ProcentageInput import ProcentageInput


class ProcentageBlock(tk.Frame):
    def __init__(self, root, set_chart_point, procent):
        super().__init__(root)
        Frame.__init__(self, root, bg='white')
        # todo add + and - button
        # todo validate value not bigger then next and smaller then last
        self.input_0 = ProcentageInput(root, "0%", 0, procent[0], set_chart_point, 0, 0)
        self.input_0.grid(row=1, column=0)

        self.input_20 = ProcentageInput(root, "20%", 1, procent[1], set_chart_point, 1, 0)
        self.input_20.grid(row=2, column=0)

        self.input_40 = ProcentageInput(root, "40%", 2, procent[2], set_chart_point, 2, 0)
        self.input_40.grid(row=3, column=0)

        self.input_60 = ProcentageInput(root, "60%", 3, procent[3], set_chart_point, 3, 0)
        self.input_60.grid(row=4, column=0)

        self.input_80 = ProcentageInput(root, "80%", 4, procent[4], set_chart_point, 4, 0)
        self.input_80.grid(row=5, column=0)

        self.input_100 = ProcentageInput(root, "100%", 5, procent[5], set_chart_point, 5, 0)
        self.input_100.grid(row=6, column=0)
