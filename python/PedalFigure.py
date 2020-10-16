from tkinter import Frame
from python.ProcentageBlock import ProcentageBlock
from python.FigureBlock import FigureBlock


class PedalFigure(Frame):
    def __init__(self, root, title, xscale, yscale):
        super().__init__(root)
        Frame.__init__(self, root, bg='white')
        self.root = root
        self.title = title
        self.xscale = xscale
        self.yscale = yscale
        self.main()

    def main(self):
        self.procent = [0, 20, 40, 60, 80, 100]
        self.Inputs = ProcentageBlock(self.root, self.set_chart_point, self.procent)
        self.Inputs.grid(row=0, column=0)
        self.figure = FigureBlock(self.root, self.title, self.xscale, self.yscale, self.procent)
        self.figure.grid(row=8, column=0)

    def set_chart_point(self, point, position):
        self.figure.set_chart_point(point, position)

    def change_chart_plot_value(self, before, after):
        self.figure.change_chart_plot_value(before, after)

    def getMap(self, pedel_map):
        self.procent = list(map(int, pedel_map))
        print(self.procent, "pedel_map")
        self.Inputs = ProcentageBlock(self.root, self.set_chart_point, self.procent)
        self.figure.abc(self.procent)
