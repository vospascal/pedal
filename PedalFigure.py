import tkinter as tk
from tkinter import Frame, Label, Entry, Button, OptionMenu, StringVar, DoubleVar, Scale, HORIZONTAL
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import multiMap as mm
import numpy as np
from ProcentageInput import ProcentageInput


class PedalFigure(tk.Frame):
    def __init__(self, root, title, xscale, yscale):
        super().__init__(root)

        self.procent_0 = 0
        self.procent_20 = 15
        self.procent_40 = 43
        self.procent_60 = 53
        self.procent_80 = 75
        self.procent_100 = 100

        self.procent = [
            self.procent_0,
            self.procent_20,
            self.procent_40,
            self.procent_60,
            self.procent_80,
            self.procent_100,
        ]

        # todo add + and - button
        # todo validate value not bigger then next and smaller then last
        self.input_0 = ProcentageInput(root, "0%", 0, self.procent_0, self.set_chart_point, 0)
        self.input_0.pack()

        self.input_20 = ProcentageInput(root, "20%", 1, self.procent_20, self.set_chart_point, 1)
        self.input_20.pack()

        self.input_40 = ProcentageInput(root, "40%", 2, self.procent_40, self.set_chart_point, 2)
        self.input_40.pack()

        self.input_60 = ProcentageInput(root, "60%", 3, self.procent_60, self.set_chart_point, 3)
        self.input_60.pack()

        self.input_80 = ProcentageInput(root, "80%", 4, self.procent_80, self.set_chart_point, 4)
        self.input_80.pack()

        self.input_100 = ProcentageInput(root, "100%", 5, self.procent_100, self.set_chart_point, 5)
        self.input_100.pack()

        self.scatter_x = [0]
        self.scatter_y = [0]
        self.fig = plt.Figure(figsize=(3, 3), dpi=80, facecolor='w', edgecolor='k')
        self.fig.text(0.5, 0.95, title, ha='center')
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.sc = self.ax.scatter(self.scatter_x, self.scatter_y)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)

        self.line, = self.ax.plot(xscale, yscale)
        self.lines, = self.ax.plot(xscale, self.procent, markersize=5, marker='o')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(column=0, row=7, columnspan=10)

        self.ani_brake = animation.FuncAnimation(self.fig, self.update_chart, interval=100, blit=False)

    def update_chart(self, _):
        test = mm.multiMap(self.scatter_x[0], [0, 20, 40, 60, 80, 100], self.procent, 100);
        self.sc.set_offsets(np.column_stack((self.scatter_x, test)))
        return self.sc,

    def set_chart_point(self, point, position):
        self.procent[position] = int(point.get())
        self.lines.set_ydata(self.procent)

    def change_chart_plot_Value(self, x):
        self.scatter_x = [int(x)]
        self.scatter_y = [int(x)]

