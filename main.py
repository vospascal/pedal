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
        test = mm.multiMap(self.scatter_x[0], [0, 20, 40, 60, 80, 100], self.procent, 100);
        self.sc.set_offsets(np.column_stack((self.scatter_x, test)))
        return self.sc,

    def setpoint(self, point, position):
        self.procent[position] = int(point.get())
        self.lines.set_ydata(self.procent)

    def add(self, x):
        self.scatter_x = [int(x)]
        self.scatter_y = [int(x)]

    def init_window(self):
        # self.master.title("Use Of FuncAnimation in tkinter based GUI")
        self.pack(fill='both', expand=1)

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
        self.Label_0 = Label(self, text="0%", width=12)
        self.Label_0.grid(row=0, column=0)
        self.text_0 = Entry(self, width=12)
        self.text_0.insert(0, self.procent_0)
        # self.text_0.configure(state='readonly')
        self.text_0.bind('<FocusOut>', (lambda _: self.setpoint(self.text_0, 0)))
        self.text_0.grid(row=0, column=1)

        self.Label_20 = Label(self, text="20%", width=12)
        self.Label_20.grid(row=1, column=0)
        self.text_20 = Entry(self, width=12)
        self.text_20.insert(0, self.procent_20)
        self.text_20.bind('<FocusOut>', (lambda _: self.setpoint(self.text_20, 1)))
        self.text_20.grid(row=1, column=1)

        self.Label_40 = Label(self, text="40%", width=12)
        self.Label_40.grid(row=2, column=0)
        self.text_40 = Entry(self, width=12)
        self.text_40.insert(0, self.procent_40)
        self.text_40.bind('<FocusOut>', (lambda _: self.setpoint(self.text_40, 2)))
        self.text_40.grid(row=2, column=1)

        self.Label_60 = Label(self, text="60%", width=12)
        self.Label_60.grid(row=3, column=0)
        self.text_60 = Entry(self, width=12)
        self.text_60.insert(0, self.procent_60)
        self.text_60.bind('<FocusOut>', (lambda _: self.setpoint(self.text_60, 3)))
        self.text_60.grid(row=3, column=1)

        self.Label_80 = Label(self, text="80%", width=12)
        self.Label_80.grid(row=4, column=0)
        self.text_80 = Entry(self, width=12)
        self.text_80.insert(0, self.procent_80)
        self.text_80.bind('<FocusOut>', (lambda _: self.setpoint(self.text_80, 4)))
        self.text_80.grid(row=4, column=1)

        self.Label_100 = Label(self, text="100%", width=12)
        self.Label_100.grid(row=5, column=0)
        self.text_100 = Entry(self, width=12)
        self.text_100.insert(0, self.procent_100)
        self.text_100.bind('<FocusOut>', (lambda _: self.setpoint(self.text_100, 5)))
        self.text_100.grid(row=5, column=1)

        self.scatter_x = [0]
        self.scatter_y = [0]
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.sc = self.ax.scatter(self.scatter_x, self.scatter_y)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)

        self.line, = self.ax.plot([0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.lines, = self.ax.plot([0, 20, 40, 60, 80, 100], self.procent, markersize=5, marker='o')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(column=0, row=7, columnspan=10)

        # start temp solution
        var = tk.DoubleVar()
        var.set(50)
        horizontal = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, variable=var, command=self.add)
        horizontal.pack()
        # start temp solution

        self.ani = animation.FuncAnimation(self.fig, self.update, interval=100, blit=False)


root = tk.Tk()
root.geometry("650x650")
root.title("Pedalbox")
root.iconbitmap("./pedal.ico")
app = Window(root)
tk.mainloop()
