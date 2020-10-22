from tkinter import Frame, Label
from python.PedalFigure import PedalFigure
from pubsub import pub


class Brake(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')

        self.brake = PedalFigure(self, "brake", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.brake.grid(row=1, column=0)

        pub.subscribe(self.getMap, 'brake_map')
        pub.subscribe(self.change_chart_plot_value, 'brake_value')

    def change_chart_plot_value(self, before, after):
        self.brake.change_chart_plot_value(before, after)

    def getMap(self, pedel_map):
        self.brake.getMap(pedel_map)

