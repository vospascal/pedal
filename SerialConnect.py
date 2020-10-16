from tkinter import Frame
from SerialOptionMenu import SerialOptionMenu

class SerialConnect(Frame):
    def __init__(self, parent, controller, get_serial_ports):
        Frame.__init__(self, parent, bg='white')
        com_port = SerialOptionMenu(self, "com port selection", get_serial_ports(), 0, 1)
        com_port.grid(row=1, column=0)

        bout_speed = SerialOptionMenu(self, "baud speed selection",
                                           [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200], 0, 1)
        bout_speed.grid(row=1, column=1)

        bit_size = SerialOptionMenu(self, "bit size selection", [2, 4, 8, 16, 32, 64], 0, 1)
        bit_size.grid(row=1, column=2)

        time_out = SerialOptionMenu(self, "time out selection", [0, 2, 4, 6, 8, 10, 15, 20], 0, 1)
        time_out.grid(row=1, column=3)
