from tkinter import Frame, Label
from python.PedalFigure import PedalFigure
from pubsub import pub


class Clutch(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')

        self.clutch = PedalFigure(self, "clutch", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.clutch.grid(row=1, column=0)

        pub.subscribe(self.getMap, 'clutch_map')
        pub.subscribe(self.change_chart_plot_value, 'clutch_value')

    def change_chart_plot_value(self, before, after):
        self.clutch.change_chart_plot_value(before, after)

    def getMap(self, message):
        self.clutch.getMap(message)

