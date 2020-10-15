from tkinter import *

from tkinter import Frame, Label, LEFT
from tkinter.ttk import Notebook

from PedalFigure import PedalFigure


class Clutch(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')
        # self.pack(fill=BOTH, side=TOP)
        lblTitle = Label(self, text='Welcome to the Program!')
        lblTitle.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.clutch = PedalFigure(self, "clutch", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.clutch.grid(row=1, column=0)


class Brake(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')
        # self.pack(fill=BOTH, side=TOP)
        lblTitle = Label(self, text='Welcome to the Program!')
        lblTitle.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.brake = PedalFigure(self, "brake", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.brake.grid(row=1, column=0)


class Trottle(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')
        # self.pack(fill=BOTH, side=TOP)
        lblTitle = Label(self, text='Welcome to the Program!')
        lblTitle.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.brake = PedalFigure(self, "brake", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.brake.grid(row=1, column=0)


class MainWindow(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.geometry("750x600")
        self.title("Pedalbox")
        self.iconbitmap("./pedal.ico")
        self.master = master
        self.init_window()
        self.serial_object = None
        self.serial_data = ''
        self.filter_data = ''

    def init_window(self):
        # Main Container
        container = Frame(self, bg='white')
        container.pack(fill="both")

        tablayout = Notebook(container)

        # tab1
        tab1 = Frame(tablayout, bg='white')
        tab1.pack(fill="both", expand=1)

        self.clutch = Clutch(tab1, self)
        self.clutch.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tab1.grid_columnconfigure(0, weight=1)

        self.brake = Brake(tab1, self)
        self.brake.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tab1.grid_columnconfigure(1, weight=1)
        tablayout.add(tab1, text="TAB 1")

        self.trottle = Trottle(tab1, self)
        self.trottle.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        tab1.grid_columnconfigure(2, weight=1)

        # # tab2
        # tab2 = Frame(tablayout)
        # tab2.pack(fill="both")
        # tab2labela = Label(tab2, text="tab2a")
        # tab2labela.grid(row=0, column=0)
        # tablayout.add(tab2, text="TAB 2")

        tablayout.pack(fill="both", expand=1)


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop()
