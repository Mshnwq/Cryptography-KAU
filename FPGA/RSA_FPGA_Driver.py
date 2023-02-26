import serial.tools.list_ports
from serial import Serial
import struct
import time

class RSA_FPGA:
    """
    RSA FPGA Class
    
    responsible for driving RSA of FPGA
    """
    # fpga constructor
    def __init__(self):
        # try:  
            self.read = None
            self.exp = None
            self.mod = None
            self.text = None 
            # print(self.find_all())
            self.__setupPort()
            # self.openPort()   # use when needed
            # self.closePort()  # use when needed
            print("constructed FPGA")
        # except Exception as e:
            # print(f"failed FPGA {e}")

    def __setupPort(self):
        try:
            # Find the CP210x device
            ports = list(serial.tools.list_ports.grep('CP210x'))
            if len(ports) == 0:
                raise Exception('No CP210x device found')

            # Connect to the first CP210x device found
            self.portID = ports[0].device
            print(f'Connecting to {self.portID}')
            
            # create the port
            self.port = Serial(self.portID, baudrate=9600, bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                        timeout=1)
            
        except Exception as e:
            raise Exception(f"failed setup {e}")

    def find_all(pattern=None):
        """
        Returns all serial ports present.

        params:
            pattern (str): pattern to search for when retrieving serial ports
        returns: list of devices
        raises: :py:class:`~alarmdecoder.util.CommError`
        """
        devices = []

        # try:
        #     if pattern:
        #         devices = serial.tools.list_ports.grep(pattern)
        #     else:
        devices = serial.tools.list_ports.comports(include_links=True)

        # except serial.SerialException as err:
        #     raise CommError('Error enumerating serial devices: {0}'.format(str(err)), err)

        for i, device in enumerate(devices):
            print(f"#{i} description {device.description}")
            print(f"#{i} device {device.device}")
            print(f"#{i} name {device.name}")
            print(f"#{i} hwid {device.hwid}")
            print(f"#{i} pid {device.pid}")
            print(f"#{i} vid {device.vid}")
            print(f"#{i} interface {device.interface}")
            print(f"#{i} product {device.product}")
            print(f"#{i} location {device.location}")
            print(f"#{i} serial_number {device.serial_number}")
            print(f"#{i} manufacturer {device.manufacturer}\n")

        # return devices

    def openPort(self) -> bool:
        try:
            self.port.open()
            print(f"success open {self.portID}")
            return True
        except Exception as e:
            print(f"failed open {self.portID} error {e}")
            return False
        ...

    def closePort(self) -> bool:
        try:
            self.port.close()
            print(f"success close {self.portID}")
            return True
        except Exception as e:
            print(f"failed close {self.portID} error {e}")
            return False
        ...    

    def isPortOpen(self) -> bool:
        return self.port.isOpen()

    def decrypt(self):
        return self.encrypt()

    def encrypt(self):
        # send data to FPGA
        if self.writeToFPGA():
            print("Written to FPGA")
        else:
            # print("Failed to write to FPGA")
            raise Exception("Failed to write to FPGA")
        self.clearExp()
        self.clearMod()
        self.clearText()
        
        time.sleep(0.3)
        # read data from FPGA
        if self.readFromFPGA():
            print("Read from FPGA")
        else:
            print("Failed to read from FPGA")
            return
        __readTemp = self.getRead()
        self.clearRead()
        return __readTemp
    ...
    
    def readFromFPGA(self) -> bool:
        try:
            hex_string = ""
            for i in range(4):
                data_byte = self.port.read(1)
                print(data_byte)
                hex_string = format(data_byte[0], "02x") + "" + hex_string
            self.read = hex_string
            return True
        
        except Exception as e:
            print(f"read error {e}")
            return False
        ...

    def writeToFPGA(self) -> bool:
        try:
            if self.exp == None:
                raise Exception("Invalid Exp")
            if self.mod == None:
                raise Exception("Invalid mod")
            if self.text == None:
                raise Exception("Invalid text")
            # pack the the 96 bit data to be sent
            print(self.exp)
            print(self.mod)
            print(self.text)
            packed_data = struct.pack('3I', self.exp, self.mod, self.text)
            self.port.write(packed_data)
            print(f"packed data {packed_data}")
            return True

        except Exception as e:
            print(f"write error {e}")
            return False
        ...

    def clearExp(self):
        self.exp = None

    def setExp(self, val: hex):
        self.exp = int(val, 16)

    def getExp(self) -> str:
        return str(self.exp)
    
    def clearMod(self):
        self.mod = None

    def setMod(self, val: hex):
        self.mod = int(val, 16)

    def getMod(self) -> str:
        return str(self.mod)
    
    def clearText(self):
        self.text = None

    def setText(self, val: hex):
        self.text = int(val, 16)

    def getText(self) -> str:
        return str(self.text)

    def clearRead(self):
        self.read = None

    def getRead(self) -> str:
        return str(self.read)

if __name__ == "__main__":
    
    fpga = RSA_FPGA()
    # fpga.isPortOpen()
    
    fpga.setExp("0x10001")
    fpga.setMod("0xf0c792cb")
    message = 'E460'.encode().hex()
    # print(message)
    fpga.setText(message)
    cipher = fpga.encrypt()
    print(f" the cipher is {cipher}")
    print(f" the cipher is type {type(cipher)}")

    fpga.setExp("0xe4f319c1")
    fpga.setMod("0xf0c792cb")
    fpga.setText("0x"+cipher)
    plain = fpga.decrypt()
    print(f" the plain is {plain}")
    # print(f" the plain is {plain.decode()}")

    b = bytes.fromhex(plain)
    s = b.decode("utf-8")
    print(b)
    
    # fpga.closePort()