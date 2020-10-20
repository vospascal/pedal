def serial_send_data(self, send_data):
    if not send_data:
        print("Sent Nothing")

    self.serial_object.write(send_data)
    # self.serial_object.flush()