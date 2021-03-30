from dearpygui.core import *
from dearpygui.simple import *
from LMS_Seal import laser_algorithm
from Generating_Seal_Data import generate_seal_data
import serial
from time import time, sleep

# First Directory Picker
def file_picker(sender, data):
    open_file_dialog(callback=apply_selected_file, extensions=".*,.py")


def apply_selected_file(sender, data):
    log_debug(data)  # so we can see what is inside of data
    directory = data[0]
    file = data[1]
    set_value("directory", directory)
    set_value("file", file)
    set_value("file_path", f"{directory}\\{file}")
    sealnomx, sealnomy, lines = generate_seal_data(file)
    add_data("lines", lines)
    add_line_series("Seal Comparison", "Nominal Seal", sealnomx, sealnomy, color=[255, 255, 0], weight=2)


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

    laserdatax, laserdatay, laserdata = laser_algorithm(distance, get_data("lines"))
    add_scatter_series("Seal Comparison", "Measured Data", laserdatax, laserdatay, marker=2, size=1, weight=2)


set_main_window_size(900, 700)
with window("Select Nominal Seal Profile Data", width=280, height=200, x_pos=10, y_pos=10):
    add_button("Nominal Profile Data Selector", callback=file_picker)
    add_text("Directory Path: ")
    add_same_line()
    add_label_text("##filedir", source="directory", color=[255, 0, 0])
    add_text("File: ")
    add_same_line()
    add_label_text("##file", source="file", color=[255, 0, 0])
    add_text("File Path: ")
    add_same_line()
    add_label_text("##filepath", source="file_path", color=[255, 0, 0])

with window("Calibration", width=500, height=200, x_pos=10, y_pos=10):
    add_button("Start", callback=RunLaser)
    add_input_int("Number of Measurements", default_value=15)
    add_input_float("Time Delay", default_value=1)
    add_input_float("Interval Distance", default_value=0.05)

with window('Plot', width=840, height=420, x_pos=10, y_pos=220):
    add_plot("Seal Comparison", x_axis_name="X Axis", y_axis_name="Y Axis")

start_dearpygui()