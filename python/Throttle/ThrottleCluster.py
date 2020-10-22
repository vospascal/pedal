from tkinter import Frame, Canvas
from python.Cluster import Cluster
from pubsub import pub


class ThrottleCluster(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')
        canvas = Canvas(self, width=200, height=200, bg='white')
        canvas.grid(row=0, column=0, columnspan=2)
        # Throttle
        self.cluster = Cluster(canvas)
        self.cluster.grid(row=1, column=0, columnspan=2)

        pub.subscribe(self.update, 'throttle_cluster')

    def update(self, after):
        self.cluster.update(after)
