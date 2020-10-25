from tkinter import Frame, Label, Entry, END


class ProcentageInput(Frame):
    def __init__(self, parent, text, index, var_value, set_chart_point, row=0, column=0):
        Frame.__init__(self, parent, bg='white')
        label = Label(self, text=text, width=12, bg='white')
        label.grid(row=row, column=column)
        self.input = Entry(self, width=12)
        self.input.insert(0, var_value)
        # self.text_0.configure(state='readonly')
        self.input.bind('<FocusOut>', (lambda _: set_chart_point(self.input, index)))
        self.input.grid(row=row, column=column + 1)

    def update(self, var_value):
        self.input.delete(0, END)
        self.input.insert(0, var_value)
