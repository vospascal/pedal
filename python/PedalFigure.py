from tkinter import Frame
from python.ProcentageBlock import ProcentageBlock
from python.FigureBlock import FigureBlock


class PedalFigure(Frame):
    def __init__(self, root, title, xscale, yscale):
        super().__init__(root)
        Frame.__init__(self, root, bg='white')

        procent = [0, 15, 43, 53, 75, 100]
        Inputs = ProcentageBlock(root, self.set_chart_point, procent)
        Inputs.grid(row=0, column=0)

        self.figure = FigureBlock(root, title, xscale, yscale, procent)
        self.figure.grid(row=8, column=0)

    def set_chart_point(self, point, position):
        self.figure.set_chart_point(point, position)

    def change_chart_plot_value(self, before, after):
        self.figure.change_chart_plot_value(before, after)
