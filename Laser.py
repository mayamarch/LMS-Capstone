import serial
from time import time, sleep


# configure the serial port
serial_port = serial.Serial("COM3", 9600, parity=serial.PARITY_NONE, stopbits=1, timeout=3)

serial_port.write("D".encode())     # set output format to ascii
serial_port.write("A1".encode())    # set output to English Units

num_measurements = 5
time_delay = 1

serial_port.write("H1".encode())    # start sampling

distance = []

for i in range(0, num_measurements):
    serial_port.write("H2".encode())
    sleep(time_delay - time() % 1)  # runs every 1 sec
    serial_port.write("H1".encode())    # start sampling
    distance.append(float(serial_port.readline().decode('ascii').strip()))  # read distance

print(distance)
