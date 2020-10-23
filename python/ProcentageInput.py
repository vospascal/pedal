from tkinter import Frame, Label, Entry


class ProcentageInput(Frame):
    def __init__(self, parent, text, index, varValue, set_chart_point, row=0, column=0):
        Frame.__init__(self, parent, bg='white')
        self.label = Label(self, text=text, width=12, bg='white')
        self.label.grid(row=row, column=column)
        self.input = Entry(self, width=12)
        self.input.insert(0, varValue)
        # self.text_0.configure(state='readonly')
        self.input.bind('<FocusOut>', (lambda _: set_chart_point(self.input, index)))
        self.input.grid(row=row, column=column+1)
