"""
win -> window
fr  -> frame
lb  -> label
en  -> entry
"""


import sys
sys.path.insert(0, 'classes')
sys.path.insert(0, 'functions')
import tkinter as tk
import f_Functions as funcs
import os

dir = os.path.dirname(os.path.realpath(__file__))

with open('CM.conf', 'r', newline = '') as conf_file :
	for row in conf_file :
		if 'bgColor' in row :
			bg_color_row = row
conf_file.close()

bg_color = bg_color_row.split("=")[1]

win_master = funcs.defineWindow(1280, 720, title = "D&D Manager")
fr_base_top = funcs.createFrame(win_master, 1280, 100, x = '0', y = '0', bg = bg_color, pk = 1, pp = 1)
fr_base_left = funcs.createFrame(win_master, 150, 416, x = '0', y = '102', bg = bg_color, pk = 1, pp = 1)
fr_base_right = funcs.createFrame(win_master, 200, 618, x = '1080', y = '102', bg = bg_color, pk = 1, pp = 1)
fr_base_bottom = funcs.createFrame(win_master, 1078, 200, x = '0', y = '520', bg = bg_color, pk = 1, pp = 1)
fr_base_center = funcs.createFrame(win_master, 926, 416, x = '152', y = '102', bg = bg_color, pk = 1, pp = 1)
win_master.mainloop()