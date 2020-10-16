from tkinter import Frame, Label
from python.PedalFigure import PedalFigure


class Throttle(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')
        # self.pack(fill=BOTH, side=TOP)
        label = Label(self, text="input", bg='white')
        label.grid(row=1, column=0)
        label = Label(self, text="output", bg='white')
        label.grid(row=1, column=2)

        self.throttle = PedalFigure(self, "brake", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.throttle.grid(row=1, column=0)

    def change_chart_plot_value(self, value):
        self.throttle.change_chart_plot_value(value)