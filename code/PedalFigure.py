from tkinter import Frame, Button
from ProcentageBlock import ProcentageBlock
from FigureBlock import FigureBlock
from pubsub import pub


class PedalFigure(Frame):
    def __init__(self, parent, title, xscale, yscale):
        Frame.__init__(self, parent, bg='white')
        self.procent = [0, 20, 40, 60, 80, 100]

        self.Inputs = ProcentageBlock(self, self.set_chart_point, [0, 20, 40, 60, 80, 100])
        self.Inputs.grid(row=0, column=0)

        self.save = Button(self, text="save to arduino", command=lambda: self.send(title))
        self.save.grid(row=1, column=0)

        self.figure = FigureBlock(self, title, xscale, yscale, [0, 20, 40, 60, 80, 100])
        self.figure.grid(row=2, column=0)

    def update_procent(self, point, position):
        self.procent[position] = int(point.get())

    def set_chart_point(self, point, position):
        self.update_procent(point, position)
        self.figure.set_chart_point(point, position)

    def change_chart_plot_value(self, before, after):
        self.figure.change_chart_plot_value(before, after)

    def get_map(self, pedel_map):
        self.procent = pedel_map
        self.Inputs.update(pedel_map)
        self.figure.set_y_data(list(map(int, pedel_map)))

    def send(self, title, **kwargs):
        pub.sendMessage(f"{title}_map_update", pedel_map_update=self.procent)

