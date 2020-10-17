from tkinter import Frame
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from python import multiMap as mm
import numpy as np

class Cluster(Frame):
    def __init__(self, root):
        super().__init__(root)

        fig = plt.Figure(figsize=(3, 3), dpi=80, facecolor='w', edgecolor='k')
        # fig.text(0.5, 0.95, title, ha='center')
        self.ax = fig.add_subplot(1, 1, 1)
        self.procent = [0, 100]

        self.pie = self.ax.pie(self.procent, radius=1.4, startangle=270, counterclock=False,
                               colors=['blue', 'white'],
                               wedgeprops={'width': 0.2, 'edgecolor': 'gray'})
        self.text = self.ax.text(0, 0, f'{self.procent[0]}%', ha='center', va='center', size=20)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack()

        self.ani_brake = animation.FuncAnimation(fig, self.update_chart, interval=100, blit=False)

    def update(self, delta):
        self.procent = [int(delta), 100 - int(delta)]

    def update_chart(self, abc):
        self.pie = self.ax.pie(self.procent, radius=1.4, startangle=270, counterclock=False,
                               colors=['blue', 'white'],
                               wedgeprops={'width': 0.2, 'edgecolor': 'black'})
        self.text.set_text(f'{self.procent[0]}%')
