# ---------Imports

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import multiMap as mm
# ---------End of imports


from tkinter import Frame, Label, Entry, Button


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def update(self, _):
        test = mm.multiMap(self.scatter_x[0], [0, 20, 40, 60, 80, 100], [0, 15, 43, 53, 75, 100], 100);
        print(test)

        self.sc.set_offsets(np.column_stack((self.scatter_x, test)))
        return self.sc,

    def add(self, x):
        self.scatter_x = [int(x)]
        self.scatter_y = [int(x)]

    def init_window(self):
        # self.master.title("Use Of FuncAnimation in tkinter based GUI")
        self.pack(fill='both', expand=1)

        self.scatter_x = [0]
        self.scatter_y = [0]
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.sc = self.ax.scatter(self.scatter_x, self.scatter_y)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)

        self.line, = self.ax.plot([0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.line, = self.ax.plot([0, 20, 40, 60, 80, 100], [0, 15, 43, 53, 75, 100])

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(column=0, row=1)

        # start temp solution
        var = tk.DoubleVar()
        var.set(50)
        horizontal = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, variable=var, command=self.add)
        # start temp solution

        horizontal.pack()

        self.ani = animation.FuncAnimation(self.fig, self.update, interval=25, blit=False)


root = tk.Tk()
root.geometry("650x550")
root.title("Pedalbox")
root.iconbitmap("./pedal.ico")
app = Window(root)
tk.mainloop()
