import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import multiMap as mm
import numpy as np

from tkinter import LEFT, RIGHT

class FigureBlock(tk.Frame):
    def __init__(self, root, title, xscale, yscale, procent):
        super().__init__(root)

        self.scatter_x = [0]
        self.scatter_y = [0]
        self.procent = procent

        self.fig = plt.Figure(figsize=(3, 3), dpi=80, facecolor='w', edgecolor='k')
        self.fig.text(0.5, 0.95, title, ha='center')
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.sc = self.ax.scatter(self.scatter_x, self.scatter_y)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)

        self.line, = self.ax.plot(xscale, yscale)
        self.lines, = self.ax.plot(xscale, self.procent, markersize=5, marker='o')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=RIGHT)

        self.ani_brake = animation.FuncAnimation(self.fig, self.update_chart, interval=100, blit=False)

    def update_chart(self, _):
        test = mm.multiMap(self.scatter_x[0], [0, 20, 40, 60, 80, 100], self.procent, 100);
        self.sc.set_offsets(np.column_stack((self.scatter_x, test)))
        return self.sc

    def set_chart_point(self, point, position):
        self.procent[position] = int(point.get())
        self.lines.set_ydata(self.procent)

    def change_chart_plot_value(self, x):
        self.scatter_x = [int(x)]
        self.scatter_y = [int(x)]