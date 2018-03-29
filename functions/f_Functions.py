import tkinter as tk

def defineWindow(win_width, win_height, **kwargs) :

	title    = kwargs.get('title')
	icon     = kwargs.get('icon')
	toplevel = kwargs.get('toplevel')
	grab     = kwargs.get('grab')

	if toplevel :
		win = tk.Toplevel(toplevel)
		width = int((toplevel.geometry()).split('x')[0]) # Width of 'root' window
		height = int((toplevel.geometry()).split('x')[1].split('+')[0]) # Height of 'root' window
		x = int((toplevel.geometry()).split('x')[1].split('+')[1]) # 'x' position of 'root' window
		y = int((toplevel.geometry()).split('x')[1].split('+')[2])# 'y' position of 'root' window

		y += (height/2) - (win_height/2)    # Positionning the top level window in the center of the 'root' window
		x += (width/2) - (win_width/2)      # //

	else :
		win = tk.Tk()
		screen_width = win.winfo_screenwidth() # Screen width
		screen_height = win.winfo_screenheight() # Screen height

		x = (screen_width/2) - (win_width/2)    # Positioning the window in the center of the screen
		y = (screen_height/2) - (win_height/2)  # //

	if grab :
		win.grab_set()

	if title :
		win.title(title) # Window title

	if icon :
		win.iconbitmap(icon)


	win.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))
	win.resizable(0,0)

	return(win)