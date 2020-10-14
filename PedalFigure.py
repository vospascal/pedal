import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import multiMap as mm
import numpy as np

from tkinter import LEFT, RIGHT

from ProcentageBlock import ProcentageBlock
from FigureBlock import FigureBlock


class PedalFigure(tk.Frame):
    def __init__(self, root, title, xscale, yscale):
        super().__init__(root)

        self.procent = [0, 15, 43, 53, 75, 100]
        self.scatter_x = [0]
        self.scatter_y = [0]

        self.Inputs = ProcentageBlock(root, self.set_chart_point, self.procent)
        self.Inputs.pack()

        self.figure = FigureBlock(root, title, xscale, yscale, self.procent)
        self.figure.pack()

    def set_chart_point(self, point, position):
        self.figure.set_chart_point(point, position)

    def change_chart_plot_value(self, x):
        self.figure.change_chart_plot_value(x)
