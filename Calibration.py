from dearpygui.core import *
from dearpygui.simple import *
import serial
from time import time, sleep

def RunLaser(sender, data):
    # configure the serial port
    serial_port = serial.Serial("COM3", 9600, parity=serial.PARITY_NONE, stopbits=1, timeout=3)

    serial_port.write("D".encode())     # set output format to ascii
    serial_port.write("A1".encode())    # set output to English Units
    serial_port.write("H1".encode())    # start sampling

    num_measurements = get_value("Number of Measurements")
    time_delay = get_value("Time Delay")
    D = get_value("Interval Distance")

    distance = []
    for i in range(0, num_measurements):
        serial_port.write("H2".encode())
        sleep(time_delay - time() % 1)  # runs every 1 sec
        serial_port.write("H1".encode())    # start sampling
        distance.append(float(serial_port.readline().decode('ascii').strip()))  # read distance

    Interval_Dist = 0
    Intervals = []
    for i in range(0, num_measurements):
        Interval_Dist = Interval_Dist + D
        Intervals.append(Interval_Dist)

    add_scatter_series("Calibration Data", "Measurement", distance, Intervals, marker=2, size=1, weight=2)

    minvalue = distance[0]
    for i in range(0, len(distance)):
        if distance[i] < minvalue:
            minvalue = distance[i]

    set_value("Minimum Distance", minvalue)

    min_interval = 0
    for i in range(0, len(distance)):
        if distance[i] == minvalue:
            min_interval = i

    set_value("Minimum Distance Interval", min_interval)


set_main_window_size(900, 700)
with window("Calibration", width=500, height=200, x_pos=10, y_pos=10):
    add_button("Start", callback=RunLaser)
    add_input_int("Number of Measurements", default_value=15)
    add_input_float("Time Delay", default_value=1)
    add_input_float("Interval Distance", default_value=0.05)
    add_label_text("Minimum Distance", default_value='0', color=[210, 0, 0])
    add_label_text("Minimum Distance Interval", default_value='0',  color=[210, 0, 0])

with window('Plot', width=840, height=420, x_pos=10, y_pos=220):
    add_plot("Calibration Data", x_axis_name="X Axis", y_axis_name="Y Axis")


start_dearpygui()

