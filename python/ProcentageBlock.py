from tkinter import Frame
from python.ProcentageInput import ProcentageInput


class ProcentageBlock(Frame):
    def __init__(self, parent, set_chart_point, procent):
        Frame.__init__(self, parent, bg='white')

        # todo add + and - button
        # todo validate value not bigger then next and smaller then last

        input_0 = ProcentageInput(self, "0%", 0, procent[0], set_chart_point, 0, 0)
        input_0.grid(row=2, column=0)

        input_20 = ProcentageInput(self, "20%", 1, procent[1], set_chart_point, 1, 0)
        input_20.grid(row=3, column=0)

        input_40 = ProcentageInput(self, "40%", 2, procent[2], set_chart_point, 2, 0)
        input_40.grid(row=4, column=0)

        input_60 = ProcentageInput(self, "60%", 3, procent[3], set_chart_point, 3, 0)
        input_60.grid(row=5, column=0)

        input_80 = ProcentageInput(self, "80%", 4, procent[4], set_chart_point, 4, 0)
        input_80.grid(row=6, column=0)

        input_100 = ProcentageInput(self, "100%", 5, procent[5], set_chart_point, 5, 0)
        input_100.grid(row=7, column=0)