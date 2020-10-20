from tkinter import Frame, Label
from python.PedalFigure import PedalFigure


class Throttle(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')

        self.throttle = PedalFigure(self, "throttle", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.throttle.grid(row=1, column=0)

    def change_chart_plot_value(self, after, before):
        self.throttle.change_chart_plot_value(after, before)

    def getMap(self, throttle_map):
        self.throttle.getMap(throttle_map)