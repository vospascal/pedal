from tkinter import Frame, Label
from python.PedalFigure import PedalFigure
from pubsub import pub


class Throttle(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')

        self.throttle = PedalFigure(self, "throttle", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.throttle.grid(row=1, column=0)

        pub.subscribe(self.getMap, 'throttle_map')
        pub.subscribe(self.change_chart_plot_value, 'throttle_value')

    def change_chart_plot_value(self, before, after):
        self.throttle.change_chart_plot_value(before, after)

    def getMap(self, message):
        self.throttle.getMap(message)

