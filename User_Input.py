from dearpygui.dearpygui import *
from Generating_Seal_Data import *

show_documentation()
add_plot("Seal Comparison", "X Axis", "Y Axis")
add_line_series("Seal Comparison", "Nominal Seal", cleandata, color=[255, 0, 0], weight=2)



start_dearpygui()