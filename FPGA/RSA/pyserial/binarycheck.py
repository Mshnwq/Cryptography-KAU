# import serial.tools.list_ports
import struct
# import time

# # Find the CP210x device
# ports = list(serial.tools.list_ports.grep('CP210x'))
# if len(ports) == 0:
#     print('No CP210x device found')
#     exit()

# # Connect to the first CP210x device found
# port = ports[0].device
# print(f'Connecting to {port}')

# # Open the serial connection
# ser = serial.Serial(port, baudrate=9600, bytesize=serial.EIGHTBITS,
#                     parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
#                     timeout=1)

# # Wait for the connection to be established
# time.sleep(0.2)

# # Pack the three integers into a byte array
# # Convert the integer to a 32-bit binary integer with leading zeros
# # data1 = [b'ff', b'ff', b'fe']
# # data1 = [b'2']
# data1 = 65537
# data1 = int('217124009')
data1 = 217124009
data2 = 1628560649
# data3 = 6084794
data3 = int('0x1fd525b0',16)
# data3 = 0x1fd525b0
packed_data = struct.pack('3I', data1, data2, data3)
# packed_data = struct.pack('3c', data1[2], data1[1], data1[0])
# packed_data = struct.pack('I', data1)
print(packed_data)
# print(packed_data.decode())
# print(int.from_bytes(packed_data, 'big'))
# print(type(packed_data))


# # Write the packed binary representation to the UART
# ser.write(packed_data)
# print('done sending')

# # Wait for 5 seconds
# time.sleep(0.2)

# hex_string = ""
# for i in range(4):
#     data_byte = ser.read(1)
#     print(data_byte)
#     hex_string = format(data_byte[0], "02X") + "" + hex_string

# print(hex_string)

# # Close the serial connection
# ser.close()
# print('Connection closed')