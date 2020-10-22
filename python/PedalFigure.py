from tkinter import Frame
from python.ProcentageBlock import ProcentageBlock
from python.FigureBlock import FigureBlock


class PedalFigure(Frame):
    def __init__(self, parent, title, xscale, yscale):
        # super().__init__(root)
        Frame.__init__(self, parent, bg='white')
        self.Inputs = ProcentageBlock(self, self.set_chart_point, [0, 20, 40, 60, 80, 100])
        self.Inputs.grid(row=0, column=0)
        self.figure = FigureBlock(self, title, xscale, yscale, [0, 20, 40, 60, 80, 100])
        self.figure.grid(row=8, column=0)

    def set_chart_point(self, point, position):
        self.figure.set_chart_point(point, position)

    def change_chart_plot_value(self, before, after):
        self.figure.change_chart_plot_value(before, after)

    def getMap(self, pedel_map):
        print(pedel_map, "pedel_map")
        self.Inputs = ProcentageBlock(self, self.set_chart_point, pedel_map)
        self.figure.set_y_data(list(map(int, pedel_map)))
