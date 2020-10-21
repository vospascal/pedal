from tkinter import Frame, Tk, Button, DISABLED, NORMAL, READABLE
from tkinter.ttk import Notebook

from python.Clutch.Clutch import Clutch
from python.Brake.Brake import Brake
from python.Throttle.Throttle import Throttle
from python.Throttle.ThrottleCluster import ThrottleCluster
from python.Clutch.ClutchCluster import ClutchCluster
from python.Brake.BrakeCluster import BrakeCluster

from python.SerialConnect import serial_connect
from python.SerialPort import SerialPort
import python.Config as config

class MainWindow(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.geometry("775x475")
        self.title("Pedalbox")
        self.iconbitmap("./Assets/pedal.ico")
        self.master = master
        self.serial_object = None  # main serial ref
        self.serial_data = ''
        self.filter_data = ''

        # Main Container
        container = Frame(self, bg='white')
        container.pack(fill="both")

        self.tablayout = Notebook(container)

        # # tab1
        # self.tab1 = Frame(self.tablayout, bg='white')
        # self.tab1.pack(fill="both")
        # self.clutchCluster = ClutchCluster(self.tab1, self)
        # self.brakeCluster = BrakeCluster(self.tab1, self)
        # self.throttleCluster = ThrottleCluster(self.tab1, self)

        # tab2
        self.tab2 = Frame(self.tablayout, bg='white')
        self.tab2.pack(fill="both", expand=1)

        self.clutch = Clutch(self.tab2, self)
        self.brake = Brake(self.tab2, self)
        self.throttle = Throttle(self.tab2, self)

        # tab3
        self.tab3 = Frame(self.tablayout, bg='white')
        self.tab3.pack(fill="both", expand=1)
        self.serialPortSettings = SerialPort(self.tab3, self)

        self.init_window()

    def get_connection_info(self):
        connectioninfo = config.connection_info()
        return [connectioninfo['baudrate'], connectioninfo['comport']]

    def init_window(self):
        # tab1
        # self.clutchCluster.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        # self.tab1.grid_columnconfigure(0, weight=1)
        # self.brakeCluster.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        # self.tab1.grid_columnconfigure(1, weight=1)
        # self.throttleCluster.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        # self.tab1.grid_columnconfigure(2, weight=1)
        # self.tablayout.add(self.tab1, text="Clusters")

        # tab2
        self.clutch.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.tab2.grid_columnconfigure(0, weight=1)
        self.brake.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.tab2.grid_columnconfigure(1, weight=1)
        self.throttle.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.tab2.grid_columnconfigure(2, weight=1)
        self.tablayout.add(self.tab2, text="Settings")
        self.tablayout.pack(fill="both", expand=1)

        # tab3
        self.serialPortSettings.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.tablayout.add(self.tab3, text="config")
        self.tablayout.pack(fill="both", expand=1)

        connectButton = Button(self, text="connect to serial port", command=lambda: serial_connect(self, self.get_connection_info()[1], self.get_connection_info()[0]))
        connectButton.pack()

        # connectButton.configure(state=DISABLED)

        # serialConnect = SerialConnect.py(container, self.get_serial_ports)
        # serialConnect.pack()
        # self.tablayout.tab(0, state=DISABLED)
        # self.tablayout.tab(1, state=DISABLED)
        # tablayout.tab(2, state=DISABLED)


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop()
