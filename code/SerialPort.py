from tkinter import Frame, StringVar, Button
from tkinter.ttk import Combobox
import Config
from SerialPortList import get_serial_ports


class SerialPort(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='white')

        Config.Readconfig()

        baudrateindex = self.find_index(Config.localserialconfig['baudrate'], Config.cbaudrates)
        if baudrateindex < 0: baudrateindex = 0

        comportindex = self.find_index(Config.localserialconfig['comport'], get_serial_ports())
        if comportindex < 0: comportindex = 0

        self.tc_baudrate = StringVar()
        self.tc_baudrate = Combobox(self, textvariable=self.tc_baudrate)
        self.tc_baudrate['values'] = Config.cbaudrates
        self.tc_baudrate.current(baudrateindex)
        self.tc_baudrate.bind('<<ComboboxSelected>>', self.set_baudrate)
        self.tc_baudrate.configure(takefocus="")
        self.tc_baudrate.grid(row=1, column=0)

        self.tc_comports = StringVar()
        self.tc_comport = Combobox(self, textvariable=self.tc_comports)
        self.tc_comport['values'] = get_serial_ports()
        self.tc_comport.current(comportindex)
        self.tc_comport.bind('<<ComboboxSelected>>', self.set_comport)
        self.tc_comport.configure(takefocus="")
        self.tc_comport.grid(row=2, column=0)

        self.save = Button(self, text="save", command=Config.Close)
        self.save.grid(row=3, column=0)

        # print('baudrate: ', self.tc_baudrate['values'])
        # print('ports: ', get_serial_ports())

    def set_baudrate(self, event):
        Config.localserialconfig["baudrate"] = self.tc_baudrate.get()
        # print('Set baudrate ', config.localserialconfig["baudrate"])
        # print(config.localserialconfig)

    def set_comport(self, event):
        Config.localserialconfig["comport"] = self.tc_comports.get()
        # print('Set comport', config.localserialconfig["comport"])
        # print(config.localserialconfig)

    def find_index(self, value, qlist):
        try:
            idx = qlist.index(value)
        except ValueError:
            idx = -1
        # print('find_index: ', idx, ' Value: ', value, ' list: ', qlist)
        return idx
