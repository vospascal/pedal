import tkinter as tk
from tkinter import Frame, Label

from ProcentageBlock import ProcentageBlock
from FigureBlock import FigureBlock


class PedalFigure(Frame):
    def __init__(self, root, title, xscale, yscale):
        super().__init__(root)
        Frame.__init__(self, root, bg='white')

        self.procent = [0, 15, 43, 53, 75, 100]
        self.scatter_x = [0]
        self.scatter_y = [0]


        self.Inputs = ProcentageBlock(root, self.set_chart_point, self.procent)
        # self.Inputs.pack()
        self.Inputs.grid(row=0, column=0)
        #
        self.figure = FigureBlock(root, title, xscale, yscale, self.procent)
        # self.figure.pack()
        self.figure.grid(row=7, column=0)


    def set_chart_point(self, point, position):
        self.figure.set_chart_point(point, position)

    def change_chart_plot_value(self, x):
        self.figure.change_chart_plot_value(x)
