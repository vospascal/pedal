import threading


def serial_get_data(self):
    while True:
        try:
            self.serial_data = self.serial_object.readline().decode('utf-8').strip('\n').strip('\r')
            self.filter_data = self.serial_data.split(',')

            print(self.activeTab)
            if self.filter_data[0].find("BMAP:") >= 0:
                brake_map = self.filter_data[0].strip("BMAP:").split('-')
                print("Brake map:", brake_map)
                self.brake.getMap(brake_map)

            if self.filter_data[0].find("TMAP:") >= 0:
                throttle_map = self.filter_data[0].strip("TMAP:").split('-')
                print("Throttle map:", throttle_map)
                self.throttle.getMap(throttle_map)

            if self.filter_data[0].find("CMAP:") >= 0:
                clutch_map = self.filter_data[0].strip("CMAP:").split('-')
                print("Clutch map:", clutch_map)
                self.clutch.getMap(clutch_map)

            if self.filter_data[0].find("B:") >= 0:
                value = self.filter_data[0].strip("B:").split(';')
                after = int(float(value[0]))
                before = int(float(value[1]))

                if self.activeTab == 1:
                    threading.Thread(target=self.brake.change_chart_plot_value(before, after)).start()

                if self.activeTab == 0:
                    threading.Thread(target=self.brakeCluster.update(after)).start()
                # self.brake.change_chart_plot_value(before, after)
                # self.brakeCluster.update(after)
                # print("Brake: before:", before)
                # print("Brake: after:", after)

            if self.filter_data[0].find("T:") >= 0:
                value = self.filter_data[0].strip("T:").split(';')
                after = int(float(value[0]))
                before = int(float(value[1]))

                if self.activeTab == 1:
                    self.throttle.change_chart_plot_value(before, after)

                if self.activeTab == 0:
                    self.throttleCluster.update(after)
                # print("Throttle: before:", before)
                # print("Throttle: after:", after)

            if self.filter_data[0].find("C:") >= 0:
                value = self.filter_data[0].strip("C:").split(';')
                after = int(float(value[0]))
                before = int(float(value[1]))

                if self.activeTab == 1:
                    self.clutch.change_chart_plot_value(before, after)

                if self.activeTab == 0:
                    self.clutchCluster.update(after)
                # print("Clutch: before:", before)
                # print("Clutch: after:", after)

            if self.filter_data[0].find("setMap") >= 0:
                print(self.filter_data[0])

        except TypeError:
            pass
