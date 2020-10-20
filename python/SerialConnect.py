import serial
import serial.tools.list_ports
import sys
import threading

from python.SerialGetData import serial_get_data
from python.SerialSendData import serial_send_data


def serial_connect(self, port="COM24", baud=9600):
    try:
        if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):

            try:
                self.serial_object = serial.Serial('/dev/tty' + str(port), baud)

            except:
                print("Cant Open Specified Port")

        elif sys.platform.startswith('win'):
            self.serial_object = serial.Serial(port, baud)

    except ValueError:
        print("Enter Baud and Port")
        return

    t1 = threading.Thread(target=lambda: serial_get_data(self))
    t1.daemon = True
    t1.start()

    serial_send_data(self, b'd')
    serial_send_data(self, b'e')
