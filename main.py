# ---------Imports
import sys, serial, serial.tools.list_ports, warnings
import glob
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import multiMap as mm
# ---------End of imports


from tkinter import Frame, Label, Entry, Button, OptionMenu, StringVar, DoubleVar, Scale, HORIZONTAL


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

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

    # def connect(ser):  # button that starts a connection, ser
    #     try:
    #         global ser  # makes ser a global variable accessible to other functions
    #         port = D.get()  # snags the number in the dropdown
    #         print(D.get())
    #         ser = serial.Serial(
    #             port="COM" + str(port),
    #             baudrate=9600,
    #         )
    #         print(ser.port)
    #     except:
    #         ctypes.windll.user32.MessageBoxW(0, "Fail", title, 0)
    #         ser.close()
    #     return ser

    def update_chart(self, _):
        test = mm.multiMap(self.scatter_x[0], [0, 20, 40, 60, 80, 100], self.procent, 100);
        self.sc.set_offsets(np.column_stack((self.scatter_x, test)))
        return self.sc,

    def set_chart_point(self, point, position):
        self.procent[position] = int(point.get())
        self.lines.set_ydata(self.procent)

    def change_chart_plot_Value(self, x):
        self.scatter_x = [int(x)]
        self.scatter_y = [int(x)]

    def init_window(self):
        # self.master.title("Use Of FuncAnimation in tkinter based GUI")
        self.pack(fill='both', expand=1)

        self.procent_0 = 0
        self.procent_20 = 15
        self.procent_40 = 43
        self.procent_60 = 53
        self.procent_80 = 75
        self.procent_100 = 100

        self.procent = [
            self.procent_0,
            self.procent_20,
            self.procent_40,
            self.procent_60,
            self.procent_80,
            self.procent_100,
        ]

        # todo add + and - button
        # todo validate value not bigger then next and smaller then last
        self.Label_0 = Label(self, text="0%", width=12)
        self.Label_0.grid(row=0, column=0)
        self.text_0 = Entry(self, width=12)
        self.text_0.insert(0, self.procent_0)
        # self.text_0.configure(state='readonly')
        self.text_0.bind('<FocusOut>', (lambda _: self.set_chart_point(self.text_0, 0)))
        self.text_0.grid(row=0, column=1)

        self.Label_20 = Label(self, text="20%", width=12)
        self.Label_20.grid(row=1, column=0)
        self.text_20 = Entry(self, width=12)
        self.text_20.insert(0, self.procent_20)
        self.text_20.bind('<FocusOut>', (lambda _: self.set_chart_point(self.text_20, 1)))
        self.text_20.grid(row=1, column=1)

        self.Label_40 = Label(self, text="40%", width=12)
        self.Label_40.grid(row=2, column=0)
        self.text_40 = Entry(self, width=12)
        self.text_40.insert(0, self.procent_40)
        self.text_40.bind('<FocusOut>', (lambda _: self.set_chart_point(self.text_40, 2)))
        self.text_40.grid(row=2, column=1)

        self.Label_60 = Label(self, text="60%", width=12)
        self.Label_60.grid(row=3, column=0)
        self.text_60 = Entry(self, width=12)
        self.text_60.insert(0, self.procent_60)
        self.text_60.bind('<FocusOut>', (lambda _: self.set_chart_point(self.text_60, 3)))
        self.text_60.grid(row=3, column=1)

        self.Label_80 = Label(self, text="80%", width=12)
        self.Label_80.grid(row=4, column=0)
        self.text_80 = Entry(self, width=12)
        self.text_80.insert(0, self.procent_80)
        self.text_80.bind('<FocusOut>', (lambda _: self.set_chart_point(self.text_80, 4)))
        self.text_80.grid(row=4, column=1)

        self.Label_100 = Label(self, text="100%", width=12)
        self.Label_100.grid(row=5, column=0)
        self.text_100 = Entry(self, width=12)
        self.text_100.insert(0, self.procent_100)
        self.text_100.bind('<FocusOut>', (lambda _: self.set_chart_point(self.text_100, 5)))
        self.text_100.grid(row=5, column=1)

        self.scatter_x = [0]
        self.scatter_y = [0]
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.sc = self.ax.scatter(self.scatter_x, self.scatter_y)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)

        self.line, = self.ax.plot([0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.lines, = self.ax.plot([0, 20, 40, 60, 80, 100], self.procent, markersize=5, marker='o')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(column=0, row=7, columnspan=10)

        # start temp solution
        var = DoubleVar()
        var.set(50)
        horizontal = Scale(self, from_=0, to=100, orient=HORIZONTAL, variable=var, command=self.change_chart_plot_Value)
        horizontal.grid(row=8, column=0)
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

        ########################################
        self.ani = animation.FuncAnimation(self.fig, self.update_chart, interval=100, blit=False)


root = tk.Tk()
root.geometry("650x750")
root.title("Pedalbox")
root.iconbitmap("./pedal.ico")
app = Window(root)
tk.mainloop()
