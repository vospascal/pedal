import serial
import serial.tools.list_ports
import sys
import threading
from pubsub import pub
from tkinter import Frame, Tk, Button
from tkinter.ttk import Notebook

import Config

from clutch.Clutch import Clutch
from brake.Brake import Brake
from throttle.Throttle import Throttle
from throttle.ThrottleCluster import ThrottleCluster
from clutch.ClutchCluster import ClutchCluster
from brake.BrakeCluster import BrakeCluster

from SerialPort import SerialPort

###############################################################
# only global...
serial_object = None  # main serial ref


###############################################################

def serial_connect(self, port="COM3", baud=9600):
    global serial_object
    try:
        if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):

            try:
                serial_object = serial.Serial('/dev/tty' + str(port), baud)

            except:
                print("Cant Open Specified Port")

        elif sys.platform.startswith('win'):
            serial_object = serial.Serial(port, baud)

    except ValueError:
        print("Enter Baud and Port")
        return

    t1 = threading.Thread(target=lambda: serial_get_data(self))
    t1.daemon = True
    t1.start()

    serial_object.write(("Getmap:\n".encode()))

def serial_disconect():
    try:
        serial_object.close()
    except AttributeError:
        print("Closed serial conection")


def serial_get_data(self):
    global serial_object
    while True:
        try:
            serial_data = serial_object.readline().decode('utf-8').strip('\n').strip('\r')
            filter_data = serial_data.split(',')

            if filter_data[0].find("BMAP:") >= 0:
                print(filter_data[0])
                brake_map = filter_data[0].strip("BMAP:").split('-')
                pub.sendMessage('brake_map', pedel_map=brake_map)

            if filter_data[0].find("TMAP:") >= 0:
                print(filter_data[0])
                throttle_map = filter_data[0].strip("TMAP:").split('-')
                pub.sendMessage('throttle_map', pedel_map=throttle_map)

            if filter_data[0].find("CMAP:") >= 0:
                print(filter_data[0])
                clutch_map = filter_data[0].strip("CMAP:").split('-')
                pub.sendMessage('clutch_map', pedel_map=clutch_map)

            if filter_data[0].find("B:") >= 0:
                value = filter_data[0].strip("B:").split(';')
                after = int(float(value[0]))
                before = int(float(value[1]))

                if self.activeTab == 1:
                    pub.sendMessage('brake_value', after=after, before=before)

                if self.activeTab == 0:
                    pub.sendMessage('brake_cluster', after=after)

            if filter_data[0].find("T:") >= 0:
                value = filter_data[0].strip("T:").split(';')
                after = int(float(value[0]))
                before = int(float(value[1]))

                if self.activeTab == 1:
                    pub.sendMessage('throttle_value', after=after, before=before)

                if self.activeTab == 0:
                    pub.sendMessage('throttle_cluster', after=after)

            if filter_data[0].find("C:") >= 0:
                value = filter_data[0].strip("C:").split(';')
                after = int(float(value[0]))
                before = int(float(value[1]))

                if self.activeTab == 1:
                    pub.sendMessage('clutch_value', after=after, before=before)
                    # self.clutch.change_chart_plot_value(before, after)

                if self.activeTab == 0:
                    pub.sendMessage('clutch_cluster', after=after)

            # if filter_data[0].find("setMap") >= 0:
            #     print(filter_data[0])

        except TypeError:
            pass


def get_map_update_brake(pedel_map_update):
    global serial_object
    new_string = "-".join(str(item) for item in pedel_map_update)
    serial_object.write((f"BMAP:{new_string}\n".encode()))


def get_map_update_throttle(pedel_map_update):
    global serial_object
    new_string = "-".join(str(item) for item in pedel_map_update)
    serial_object.write((f"TMAP:{new_string}\n".encode()))


def get_map_update_clutch(pedel_map_update):
    global serial_object
    new_string = "-".join(str(item) for item in pedel_map_update)
    serial_object.write((f"CMAP:{new_string}\n".encode()))


def get_connection_info():
    connectioninfo = Config.connection_info()
    return [connectioninfo['baudrate'], connectioninfo['comport']]


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.activeTab = 0
        self.geometry("775x550")
        self.title("Pedalbox")
        # self.iconbitmap("assets/pedal.ico")
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

        connect_button = Button(self, text="connect serial port",
                                command=lambda: serial_connect(self, get_connection_info()[1],
                                                               get_connection_info()[0]))
        connect_button.pack()

        disconect_button = Button(self, text="disconect serial port",
                                  command=serial_disconect)
        disconect_button.pack()

        pub.subscribe(get_map_update_clutch, 'clutch_map_update')
        pub.subscribe(get_map_update_brake, 'brake_map_update')
        pub.subscribe(get_map_update_throttle, 'throttle_map_update')

    def tab_changed(self, tablayout):
        self.activeTab = tablayout.index(tablayout.select())  # get the active instance of tab


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop()

# import struct
# print(struct.calcsize("P") * 8)
