from tkinter import Frame
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from python import multiMap as mm
import numpy as np


class FigureBlock(Frame):
    def __init__(self, root, title, xscale, yscale, procent):
        super().__init__(root)

        self.scatter_x = [0]
        self.scatter_y = [0]
        self.procent = procent

        fig = plt.Figure(figsize=(3, 3), dpi=80, facecolor='w', edgecolor='k')
        fig.text(0.5, 0.95, title, ha='center')
        ax = fig.add_subplot(1, 1, 1)
        self.sc = ax.scatter(self.scatter_x, self.scatter_y)
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)

        self.line, = ax.plot(xscale, yscale)
        self.lines, = ax.plot(xscale, self.procent, markersize=5, marker='o')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack()

        self.ani_brake = animation.FuncAnimation(fig, self.update_chart, frames=30, blit=False)

    def update_chart(self, _):
        # test = mm.multiMap(self.scatter_x[0], [0, 20, 40, 60, 80, 100], self.procent, 100)
        self.sc.set_offsets(np.column_stack((self.scatter_x, self.scatter_y)))
        return self.sc

    def set_chart_point(self, point, position):
        self.procent[position] = int(point.get())
        self.lines.set_ydata(self.procent)

    def change_chart_plot_value(self, before, after):
        self.scatter_x = [int(after)]
        self.scatter_y = [int(before)]

    def set_y_data(self, xyz):
        self.lines.set_ydata(xyz)
