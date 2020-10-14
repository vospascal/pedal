# ---------Imports
import threading
import sys, serial, serial.tools.list_ports, warnings
import glob
import tkinter as tk
# ---------End of imports

from PedalFigure import PedalFigure
from SerialOptionMenu import SerialOptionMenu

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
                    # self.brake.change_chart_plot_value(convertToInt)
                    # print("Brake: " + str(convertToInt))

                if self.filter_data[0].find("T:") >= 0:
                    value = self.filter_data[0].strip("T:")
                    convertToInt = int(float(value))
                    self.throttle.change_chart_plot_value(convertToInt)
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


    def init_window(self):
        # self.master.title("Use Of FuncAnimation in tkinter based GUI")
        self.pack(fill='both', expand=1)

        self.throttle = PedalFigure(root, "throttle", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        self.throttle.pack()

        # self.brake = PedalFigure(root, "brake", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100],)
        # self.brake.pack()

        self.com_port = SerialOptionMenu(root, "com port selection", self.get_serial_ports(), 0, 1)
        self.com_port.pack()

        self.bout_speed = SerialOptionMenu(root, "baud speed selection",
                                           [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200], 0, 1)
        self.bout_speed.pack()

        self.bit_size = SerialOptionMenu(root, "bit size selection", [2, 4, 8, 16, 32, 64], 0, 1)
        self.bit_size.pack()

        self.time_out = SerialOptionMenu(root, "time out selection", [0, 2, 4, 6, 8, 10, 15, 20], 0, 1)
        self.time_out.pack()

        # self.connectButton = Button(self, text="run something", command=lambda: self.serial_connect("com24", 9600))
        self.connectButton = Button(self, text="run something", command=self.serial_connect)
        self.connectButton.pack()


root = tk.Tk()
root.geometry("650x750")
root.title("Pedalbox")
root.iconbitmap("./pedal.ico")
app = Window(root)
tk.mainloop()
