class USBCPort:
    def connect(self):
        print("using type c transfer data")


class USBBPort:
    def connect_type_b(self):
        print("using type b transfer data")


class USBBToCAdapter(USBCPort):
    def __init__(self, usb_port):
        self.usb_port = usb_port

    def connect(self):
        return self.usb_port.connect_type_b()


if __name__ == "__main__":
    usb_c = USBCPort()
    usb_c.connect()

    usb_b = USBBPort()
    adapter = USBBToCAdapter(usb_b)
    adapter.connect()
