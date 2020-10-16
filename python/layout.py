import serial, serial.tools.list_ports, threading, glob, sys
from tkinter import Frame, Tk, Button
from tkinter.ttk import Notebook

from python.SerialConnect import SerialConnect
from python.Clutch import Clutch
from python.Brake import Brake
from python.Throttle import Throttle


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

                if self.filter_data[0].find("BMAP:") >= 0:
                    value = self.filter_data[0].strip("BMAP:").split('-')
                    print("Brake map:", value)

                if self.filter_data[0].find("TMAP:") >= 0:
                    value = self.filter_data[0].strip("TMAP:").split('-')
                    print("Throttle map:", value)

                if self.filter_data[0].find("B:") >= 0:
                    value = self.filter_data[0].strip("B:").split(';')
                    after = int(float(value[0]))
                    before = int(float(value[1]))
                    self.brake.change_chart_plot_value(before, after)
                    # print("Brake: before:", before)
                    # print("Brake: after:", after)

                if self.filter_data[0].find("T:") >= 0:
                    value = self.filter_data[0].strip("T:").split(';')
                    after = int(float(value[0]))
                    before = int(float(value[1]))
                    self.throttle.change_chart_plot_value(before, after)
                    # print("Throttle: before:", before)
                    # print("Throttle: after:", after)

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

        self.serial_object.write(bytes(b'd'))

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

        self.throttle = Throttle(tab1, self)
        self.throttle.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        tab1.grid_columnconfigure(2, weight=1)

        # # tab2
        # tab2 = Frame(tablayout)
        # tab2.pack(fill="both")
        # tab2labela = Label(tab2, text="tab2a")
        # tab2labela.grid(row=0, column=0)
        # tablayout.add(tab2, text="TAB 2")

        tablayout.pack(fill="both", expand=1)

        serialConnect = SerialConnect(container, self, self.get_serial_ports)
        serialConnect.pack()

        # self.connectButton = Button(self, text="run something", command=lambda: self.serial_connect("com24", 9600))
        connectButton = Button(self, text="run something", command=self.serial_connect)
        connectButton.pack()


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop()
