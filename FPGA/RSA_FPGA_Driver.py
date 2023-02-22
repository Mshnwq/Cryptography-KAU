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
        try:
            self.read = None
            self.key = None
            self.mod = None
            self.text = None
            # self.__setupPort()# use when needed
            # self.openPort()   # use when needed
            # self.closePort()  # use when needed
            print("constructed FPGA")
        except Exception as e:
            print(f"failed FPGA {e}")

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
            print(f"failed setup {e}")

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
        return self.port.is_open()

    def encrypt(self): # TODO
        # send data to FPGA
        if self.writeToFPGA():
            print("Written to FPGA")
        else:
            print("Failed to write to FPGA")
            return
        self.clearKey()
        self.clearMod()
        self.clearText()
        
        time.sleep(0.2) # TODO
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
            for i in range(4): # TODO
                data_byte = self.port.read(1)
                print(data_byte)
                hex_string = format(data_byte[0], "02X") + "" + hex_string
            self.read = hex_string
            return True
        except Exception as e:
            print(f"error {e}")
            return False
        ...

    def writeToFPGA(self) -> bool:
        try:
            if self.key == None:
                raise Exception("Invalid key")
            if self.mod == None:
                raise Exception("Invalid mod")
            if self.text == None:
                raise Exception("Invalid text")
            # pack the the 96 bit data to be sent
            packed_data = struct.pack('3I', self.key, self.mod, self.text)
            self.port.write(packed_data)

        except Exception as e:
            print(f"error {e}")
            return False
        ...

    def clearKey(self):
        self.key = None

    def setKey(self, val: hex):
        self.key = int(val, 16)

    def getKey(self) -> str:
        return str(self.key)
    
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
    # E = 13
    # D = 133
    # mod = 169
