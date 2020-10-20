from tkinter import Frame, Label, OptionMenu, StringVar

class SerialOptionMenu(Frame):
    def __init__(self, root, text, list, row, column):
        super().__init__(root)

        label = Label(self, text=text)
        label.grid(row=row, column=column)
        self.status = StringVar()
        optionList = OptionMenu(self, self.status, *list)
        optionList.grid(row=row, column=column+1)

    def get(self):
        return self.status