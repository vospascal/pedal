from tkinter import Frame, Canvas
from python.Cluster import Cluster


class ThrottleCluster(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')
        canvas = Canvas(self, width=200, height=200, bg='white')
        canvas.grid(row=0, column=0, columnspan=2)
        # Throttle
        self.cluster = Cluster(canvas)
        self.cluster.grid(row=1, column=0, columnspan=2)

    def update(self, delta):
        self.cluster.update(delta)
