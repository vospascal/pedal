import serial, serial.tools.list_ports, threading, glob, sys, time
from tkinter import Frame, Tk, Button, Label
from tkinter.ttk import Notebook

from python.SerialConnect import SerialConnect
from python.Clutch import Clutch
from python.Brake import Brake
from python.Throttle import Throttle
from python.ThrottleCluster import ThrottleCluster
from python.ClutchCluster import ClutchCluster
from python.BrakeCluster import BrakeCluster


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
                    brake_map = self.filter_data[0].strip("BMAP:").split('-')
                    print("Brake map:", brake_map)
                    self.throttle.getMap(brake_map)

                if self.filter_data[0].find("TMAP:") >= 0:
                    throttle_map = self.filter_data[0].strip("TMAP:").split('-')
                    print("Throttle map:", throttle_map)
                    self.brake.getMap(throttle_map)

                if self.filter_data[0].find("B:") >= 0:
                    value = self.filter_data[0].strip("B:").split(';')
                    after = int(float(value[0]))
                    before = int(float(value[1]))
                    self.brake.change_chart_plot_value(before, after)
                    self.brakeCluster.update(after)
                    # print("Brake: before:", before)
                    # print("Brake: after:", after)

                if self.filter_data[0].find("T:") >= 0:
                    value = self.filter_data[0].strip("T:").split(';')
                    after = int(float(value[0]))
                    before = int(float(value[1]))
                    self.throttle.change_chart_plot_value(before, after)
                    self.throttleCluster.update(after)
                    # print("Throttle: before:", before)
                    # print("Throttle: after:", after)

                if self.filter_data[0].find("C:") >= 0:
                    value = self.filter_data[0].strip("C:").split(';')
                    after = int(float(value[0]))
                    before = int(float(value[1]))
                    self.clutch.change_chart_plot_value(before, after)
                    self.clutchCluster.update(after)
                    # print("Throttle: before:", before)
                    # print("Throttle: after:", after)

                if self.filter_data[0].find("setMap") >= 0:
                    print(self.filter_data[0])

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

        self.serial_object.write(b'd')
        time.sleep(.50)
        self.serial_object.write(b'e')

    def serial_send_data(self, send_data):
        if not send_data:
            print("Sent Nothing")
        self.serial_object.write(send_data)

    def init_window(self):
        # Main Container
        container = Frame(self, bg='white')
        container.pack(fill="both")

        tablayout = Notebook(container)

        # tab1
        tab1 = Frame(tablayout, bg='white')
        tab1.pack(fill="both")
        self.clutchCluster = ClutchCluster(tab1, self)
        self.clutchCluster.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tab1.grid_columnconfigure(0, weight=1)

        self.brakeCluster = BrakeCluster(tab1, self)
        self.brakeCluster.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tab1.grid_columnconfigure(1, weight=1)

        self.throttleCluster = ThrottleCluster(tab1, self)
        self.throttleCluster.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        tab1.grid_columnconfigure(2, weight=1)
        tablayout.add(tab1, text="Clusters")

        # tab2
        tab2 = Frame(tablayout, bg='white')
        tab2.pack(fill="both", expand=1)

        self.clutch = Clutch(tab2, self)
        self.clutch.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tab2.grid_columnconfigure(0, weight=1)

        self.brake = Brake(tab2, self)
        self.brake.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tab2.grid_columnconfigure(1, weight=1)

        self.throttle = Throttle(tab2, self)
        self.throttle.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        tab2.grid_columnconfigure(2, weight=1)

        tablayout.add(tab2, text="Settings")
        tablayout.pack(fill="both", expand=1)

        serialConnect = SerialConnect(container, self, self.get_serial_ports)
        serialConnect.pack()

        # self.connectButton = Button(self, text="run something", command=lambda: self.serial_connect("com24", 9600))
        connectButton = Button(self, text="connect to serial port", command=self.serial_connect)
        connectButton.pack()


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop()
