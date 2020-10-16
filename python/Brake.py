from tkinter import Frame, Label
from python.PedalFigure import PedalFigure


class Brake(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')
        # self.pack(fill=BOTH, side=TOP)
        label = Label(self, text="input", bg='white')
        label.grid(row=1, column=0)
        label = Label(self, text="output", bg='white')
        label.grid(row=1, column=2)

        self.brake = PedalFigure(self, "brake", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.brake.grid(row=1, column=0)

    def change_chart_plot_value(self, before, after):
        self.brake.change_chart_plot_value(before, after)

    def getMap(self, brake_map):
        self.brake.getMap(brake_map)
