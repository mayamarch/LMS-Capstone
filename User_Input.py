from dearpygui.core import *
from dearpygui.simple import *
from LMS_Seal import laser_algorithm
from Generating_Seal_Data import generate_seal_data

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

# Second Directory Picker
def file_picker2(sender, data):
    open_file_dialog(callback=apply_selected_file2, extensions=".*,.py")


def apply_selected_file2(sender, data):
    log_debug(data)  # so we can see what is inside of data
    directory2 = data[0]
    file2 = data[1]
    set_value("directory2", directory2)
    set_value("file2", file2)
    set_value("file_path2", f"{directory2}\\{file2}")
    lines = get_data("lines")
    laserdatax, laserdatay, laserdata = laser_algorithm(file2, lines)
    add_scatter_series("Seal Comparison", "Measured Data", laserdatax, laserdatay, marker=2, size=1, weight=2)


with window("Select Laser Data", width=280, height=200, x_pos=300, y_pos=10):
    add_button("Laser Data Selector", callback=file_picker2)
    add_text("Directory Path: ")
    add_same_line()
    add_label_text("##filedir2", source="directory2", color=[255, 0, 0])
    add_text("File: ")
    add_same_line()
    add_label_text("##file2", source="file2", color=[255, 0, 0])
    add_text("File Path: ")
    add_same_line()
    add_label_text("##filepath2", source="file_path2", color=[255, 0, 0])


with window('Plot', width=800, height=200, x_pos=300, y_pos=10):
    add_plot("Seal Comparison", x_axis_name="X Axis", y_axis_name="Y Axis")

start_dearpygui()