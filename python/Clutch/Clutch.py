from tkinter import Frame, Label
from python.PedalFigure import PedalFigure


class Clutch(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')

        self.clutch = PedalFigure(self, "clutch", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.clutch.grid(row=1, column=0)

    def change_chart_plot_value(self, value):
        self.clutch.change_chart_plot_value(value)

    def getMap(self, clutch_map):
        self.clutch.getMap(clutch_map)
