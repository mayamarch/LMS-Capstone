import serial
from time import time, sleep

# configure the serial port
serial_port = serial.Serial("COM3", 9600, parity=serial.PARITY_NONE, stopbits=1, timeout=3)

serial_port.write("D".encode())     # set output format to ascii
serial_port.write("A1".encode())    # set output to English Units

sleep(.5 - time() % .1)

distance = []
for i in range(0, 20):
    serial_port.write("H1".encode())    # start sampling
    distance.append(float(serial_port.readline().decode('ascii').strip()))  # read distance
    serial_port.write("H2".encode())
    sleep(1.26 - time() % .1)

intervalL = 0
laserdata = []
for i in range(0, len(distance)):
    intervalL = intervalL + 0.013
    laserdata.append((intervalL, (2.8818-distance[i])))
    print((intervalL, (2.8818-distance[i])))
