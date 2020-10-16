# ---------Imports
import threading
import sys, serial, serial.tools.list_ports
import glob
import tkinter as tk
# ---------End of imports

from python.SerialOptionMenu import SerialOptionMenu

from tkinter import Frame, Label, Button
from tkinter.ttk import Notebook

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.serial_object = None
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

        frameTabs = Frame(root)
        frameTabs.pack(fill="both")

        tablayout = Notebook(frameTabs)

        # tab1
        tab1 = Frame(tablayout)
        tab1.pack(fill="both")

        # self.throttle = PedalFigure(tab1, "throttle", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        # horzontal = self.throttle.pack(fill="both")
        # horzontal.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        horzontal = Label(tab1, text="Item 2 in Horizontal")
        horzontal.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        horzontal = Label(tab1, text="Item 3 in Horizontal")
        horzontal.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        tab1.grid_columnconfigure(0, weight=1)
        tab1.grid_columnconfigure(1, weight=1)
        tab1.grid_columnconfigure(2, weight=1)
        tablayout.add(tab1, text="TAB 1")

        # tab2
        tab2 = Frame(tablayout)
        tab2.pack(fill="both")
        tab2labela = Label(tab2, text="tab2a")
        tab2labela.grid(row=0, column=0)
        tab2labelb = Label(tab2, text="tab2b")
        tab2labelb.grid(row=0, column=1)
        tablayout.add(tab2, text="TAB 2")

        tablayout.pack(fill="both")





        # self.throttle = PedalFigure(root, "throttle", [0, 20, 40, 60, 80, 100], [0, 20, 40, 60, 80, 100])
        # self.throttle.pack()

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
