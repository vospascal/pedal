from tkinter import Frame, Label, CENTER
from PedalFigure import PedalFigure
from pubsub import pub


class Throttle(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')

        name_label = Label(self, text="Throttle", bg='white', justify=CENTER, font='Helvetica 18 bold')
        name_label.grid(row=1, column=0)

        self.throttle = PedalFigure(self, "throttle", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.throttle.grid(row=2, column=0)

        pub.subscribe(self.get_map, 'throttle_map')
        pub.subscribe(self.change_chart_plot_value, 'throttle_value')

    def change_chart_plot_value(self, before, after):
        self.throttle.change_chart_plot_value(before, after)

    def get_map(self, pedel_map):
        self.throttle.get_map(pedel_map)

