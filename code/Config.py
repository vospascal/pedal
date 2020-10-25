#! /usr/bin/env python

import sys
import glob
from SerialPortList import get_serial_ports
import json
import os.path

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = 0
except ImportError:
    import tkinter.ttk as ttk

    py3 = 1

filename = 'serialconfig.txt'
localserialconfig = {"baudrate": "9600", "comport": "COM24"}
cbaudrates = ('9600', '19200', '38400', '57600', '115200', '230400', '250000')  # possible baudrates


# get filename of serial port configuration
def GetFileName():
    return filename


# save serial config
def Saveconfig():
    global localserialconfig
    f = open(filename, 'w')
    json.dump(localserialconfig, f, indent=2)
    f.close()
    # print('Stored : ', localserialconfig)


# read serial config
def Readconfig():
    global localserialconfig
    print(' Open config: ', filename, ' ', localserialconfig)
    if os.path.isfile(filename):  # check if config file exists and load config
        print('File found')
        f = open(filename, 'r')
        llconfig = json.load(f)
        localserialconfig = llconfig
        f.close()
        print('Loaded : ', localserialconfig)
    else:
        localserialconfig = {"baudrate": cbaudrates[0], "comport": get_serial_ports()[0]}
        print('Not found, defaults set ', localserialconfig)
    return localserialconfig


def connection_info():
    global localserialconfig
    return localserialconfig


def Close():
    Saveconfig()
    sys.stdout.flush()
