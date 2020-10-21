from tkinter import Frame, Tk, Button, DISABLED, NORMAL, READABLE
from tkinter.ttk import Notebook
import threading

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
        self.activeTab = 0
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
        tablayout = Notebook(container)

        # # tab1
        tab1 = Frame(tablayout, bg='white')
        tab1.pack(fill="both")
        self.clutchCluster = ClutchCluster(tab1, self)
        self.brakeCluster = BrakeCluster(tab1, self)
        self.throttleCluster = ThrottleCluster(tab1, self)

        # tab2
        tab2 = Frame(tablayout, bg='white')
        tab2.pack(fill="both", expand=1)

        self.clutch = Clutch(tab2, self)
        self.brake = Brake(tab2, self)
        self.throttle = Throttle(tab2, self)

        # tab3
        tab3 = Frame(tablayout, bg='white')
        tab3.pack(fill="both", expand=1)
        self.serialPortSettings = SerialPort(tab3, self)

        threading.Thread(target=self.init_window(container, tablayout, tab1, tab2, tab3 )).start()
        # self.init_window(container, tablayout, tab1, tab2, tab3 )

    def get_connection_info(self):
        connectioninfo = config.connection_info()
        return [connectioninfo['baudrate'], connectioninfo['comport']]

    def init_window(self, container, tablayout, tab1, tab2, tab3):
        # tab1
        self.clutchCluster.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tab1.grid_columnconfigure(0, weight=1)
        self.brakeCluster.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tab1.grid_columnconfigure(1, weight=1)
        self.throttleCluster.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        tab1.grid_columnconfigure(2, weight=1)
        tablayout.add(tab1, text="Clusters")

        # tab2
        self.clutch.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tab2.grid_columnconfigure(0, weight=1)
        self.brake.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tab2.grid_columnconfigure(1, weight=1)
        self.throttle.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        tab2.grid_columnconfigure(2, weight=1)
        tablayout.add(tab2, text="Settings")
        tablayout.pack(fill="both", expand=1)

        # tab3
        self.serialPortSettings.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tablayout.add(tab3, text="config")
        tablayout.pack(fill="both", expand=1)

        connectButton = Button(self, text="connect to serial port", command=lambda: serial_connect(self, self.get_connection_info()[1], self.get_connection_info()[0]))
        connectButton.pack()

        # connectButton.configure(state=DISABLED)

        # serialConnect = SerialConnect.py(container, self.get_serial_ports)
        # serialConnect.pack()
        # tablayout.tab(0, state=DISABLED)
        # tablayout.tab(1, state=DISABLED)
        # tablayout.tab(2, state=DISABLED)

        tablayout.bind("<<NotebookTabChanged>>", lambda event: self.tab_changed(tablayout))

    def tab_changed(self, tablayout):
        self.activeTab = tablayout.index(tablayout.select())  # get the active instance of tab

if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop()


# threading.Thread(target=funcname).start()