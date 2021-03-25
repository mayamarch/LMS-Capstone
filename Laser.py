import serial
from time import time, sleep


# configure the serial port

serial_port = serial.Serial(

    "COM3",

    9600,

    parity=serial.PARITY_NONE,

    stopbits=1,

    timeout=3

)

serial_port.write("D".encode())     # set output format to ascii
serial_port.write("A1".encode())    # set output to English Units
serial_port.write("H2".encode())

interval = 10

start = input("Are you ready to start? Y/N")

serial_port.write("H1".encode())

distance = []

if start == 'Y' or 'y':
    for i in range(0, interval):
        serial_port.write("H2".encode())
        sleep(1 - time() % 1)  # runs every 1 sec
        serial_port.write("H1".encode())    # start sampling
        distance.append(float(serial_port.readline().decode('ascii').strip()))  # read distance
else:
    print('error')

serial_port.write("H2".encode())    # stop streaming

print(distance)
