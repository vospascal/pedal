# ---------Imports
import threading

import sys, serial, serial.tools.list_ports, warnings
import glob
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import multiMap as mm
# ---------End of imports


from PedalFigure import PedalFigure

from tkinter import Frame, Label, Entry, Button, OptionMenu, StringVar, DoubleVar, Scale, HORIZONTAL


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.serial_object = None
        self.serial_data = ''
        self.filter_data = ''

    def get_serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def serial_get_data(self):
        while True:
            try:
                self.serial_data = self.serial_object.readline().decode('utf-8').strip('\n').strip('\r')
                self.filter_data = self.serial_data.split(',')
                print('\n')

                if self.filter_data[0].find("B:") >= 0:
                    value = self.filter_data[0].strip("B:")
                    convertToInt = int(float(value))
                    self.brake.change_chart_plot_Value(convertToInt)
                    # print("Brake: " + str(convertToInt))

                if self.filter_data[0].find("T:") >= 0:
                    value = self.filter_data[0].strip("T:")
                    convertToInt = int(float(value))
                    self.throttle.change_chart_plot_Value(convertToInt)
                    # print("Throttle: " + str(convertToInt))

            except TypeError:
                pass

    def serial_connect(self, port="COM24", baud=9600):
        try:
            if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
                try:
                    self.serial_object = serial.Serial('/dev/tty' + str(port), baud)
                except:
                    print
                    "Cant Open Specified Port"
            elif sys.platform.startswith('win'):
                self.serial_object = serial.Serial(port, baud)

        except ValueError:
            print
            "Enter Baud and Port"
            return

        t1 = threading.Thread(target=self.serial_get_data)
        t1.daemon = True
        t1.start()

    # def update_chart(self, _):
    #     test = mm.multiMap(self.scatter_x[0], [0, 20, 40, 60, 80, 100], self.procent, 100);
    #     self.sc.set_offsets(np.column_stack((self.scatter_x, test)))
    #     return self.sc,

    # def set_chart_point(self, point, position):
    #     self.procent[position] = int(point.get())
    #     self.lines.set_ydata(self.procent)



    def init_window(self):
        # self.master.title("Use Of FuncAnimation in tkinter based GUI")
        self.pack(fill='both', expand=1)

        self.throttle = PedalFigure(root, "throttle", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.throttle.pack()

        self.brake = PedalFigure(root, "brake", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100],)
        self.brake.pack()

        # start temp solution
        # var = DoubleVar()
        # var.set(50)
        # horizontal = Scale(self, from_=0, to=100, orient=HORIZONTAL, variable=var, command=self.change_chart_plot_Value)
        # horizontal.grid(row=8, column=0)
        # start temp solution

        self.Label_comPortList = Label(self, text="com port selection")
        self.Label_comPortList.grid(row=9, column=0)
        self.status = StringVar()
        self.comPortList = OptionMenu(self, self.status, self.get_serial_ports())
        self.comPortList.grid(row=9, column=1)

        self.Label_baudSpeedList = Label(self, text="baud speed selection")
        self.Label_baudSpeedList.grid(row=9, column=4)
        self.status = StringVar()
        self.baudSpeedList = OptionMenu(self, self.status, *[1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200])
        self.baudSpeedList.grid(row=9, column=5)

        self.Label_bitSizeList = Label(self, text="bit size selection")
        self.Label_bitSizeList.grid(row=10, column=0)
        self.status = StringVar()
        self.bitSizeList = OptionMenu(self, self.status, *[2, 4, 8, 16, 32, 64])
        self.bitSizeList.grid(row=10, column=1)

        self.Label_timeOutList = Label(self, text="time out selection")
        self.Label_timeOutList.grid(row=10, column=4)
        self.status = StringVar()
        self.timeOutList = OptionMenu(self, self.status, *[0, 2, 4, 6, 8, 10, 15, 20])
        self.timeOutList.grid(row=10, column=5)

        # self.connectButton = Button(self, text="run something", command=lambda: self.serial_connect("com24", 9600))
        self.connectButton = Button(self, text="run something", command=self.serial_connect)
        self.connectButton.grid(row=11, column=0)

        ########################################
        # self.ani_throttle = animation.FuncAnimation(self.throttle, PedalFigure.update_chart, interval=100, blit=False)
        # self.ani_brake = animation.FuncAnimation(self.brake, PedalFigure.update_chart, interval=100, blit=False)
        # self.ani_b = animation.FuncAnimation(self.fig, self.update_chart, interval=100, blit=False)


root = tk.Tk()
root.geometry("650x750")
root.title("Pedalbox")
root.iconbitmap("./pedal.ico")
app = Window(root)
tk.mainloop()
