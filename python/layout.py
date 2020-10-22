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

        ################################################################
        ## tab1
        tab1 = Frame(tablayout, bg='white')
        tab1.pack(fill="both")

        clutch_cluster = ClutchCluster(tab1, self)
        brake_cluster = BrakeCluster(tab1, self)
        throttle_cluster = ThrottleCluster(tab1, self)

        clutch_cluster.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        brake_cluster.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        throttle_cluster.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        tab1.grid_columnconfigure(0, weight=1)
        tab1.grid_columnconfigure(1, weight=1)
        tab1.grid_columnconfigure(2, weight=1)

        tablayout.add(tab1, text="Clusters")

        ################################################################
        # tab2
        tab2 = Frame(tablayout, bg='white')
        tab2.pack(fill="both", expand=1)

        clutch = Clutch(tab2, self)
        brake = Brake(tab2, self)
        throttle = Throttle(tab2, self)

        clutch.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        brake.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        throttle.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        tab2.grid_columnconfigure(0, weight=1)
        tab2.grid_columnconfigure(1, weight=1)
        tab2.grid_columnconfigure(2, weight=1)

        tablayout.add(tab2, text="Settings")
        tablayout.pack(fill="both", expand=1)

        ################################################################
        # tab3
        tab3 = Frame(tablayout, bg='white')
        tab3.pack(fill="both", expand=1)
        serial_port_settings = SerialPort(tab3, self)
        serial_port_settings.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tablayout.add(tab3, text="config")
        tablayout.pack(fill="both", expand=1)

        tablayout.bind("<<NotebookTabChanged>>", lambda event: self.tab_changed(tablayout))

        connect_button = Button(self, text="connect to serial port", command=lambda: serial_connect(self, self.get_connection_info()[1], self.get_connection_info()[0]))
        connect_button.pack()

    def get_connection_info(self):
        connectioninfo = config.connection_info()
        return [connectioninfo['baudrate'], connectioninfo['comport']]

    def tab_changed(self, tablayout):
        self.activeTab = tablayout.index(tablayout.select())  # get the active instance of tab


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop()

# threading.Thread(target=funcname).start()
