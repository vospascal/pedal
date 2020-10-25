from tkinter import Frame, Canvas, Label, CENTER
from Cluster import Cluster
from pubsub import pub


class BrakeCluster(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')

        name_label = Label(self, text="Brake", bg='white', justify=CENTER, font='Helvetica 18 bold')
        name_label.grid(row=1, column=0)

        canvas = Canvas(self, width=200, height=200, bg='white')
        canvas.grid(row=2, column=0)
        # brake
        self.cluster = Cluster(canvas)
        self.cluster.grid(row=3, column=0)

        pub.subscribe(self.update, 'brake_cluster')

    def update(self, after):
        self.cluster.update(after)
