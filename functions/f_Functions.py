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

		y += (height/2) - (win_height/2)    # Positioning the top level window in the center of the 'root' window
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

def createFrame(container, width, height, **kwargs) :
	fr = tk.Frame(container, width = width, height = height)

	x  = kwargs.get('x')
	y  = kwargs.get('y')
	bg = kwargs.get('bg')
	pk = kwargs.get('pk')
	pp = kwargs.get('pp')

	if pk :
		fr.pack()
	if pp :
		fr.pack_propagate(0)
	if x and y :
		fr.place(x = int(x), y = int(y))
	if bg :
		fr.config(bg = bg)

	return(fr)

def createLabel(container, **kwargs) :

	w      = kwargs.get('w')
	h      = kwargs.get('h')
	bg     = kwargs.get('bg')
	fg     = kwargs.get('fg')
	x      = kwargs.get('x')
	y	   = kwargs.get('y')
	cur    = kwargs.get('cur')
	pp     = kwargs.get('pp')
	txt	   = kwargs.get('txt')
	btn	   = kwargs.get('btn')
	anc    = kwargs.get('anc')


	lb = tk.Label(container)
	lb.pack()
	if pp :
		lb.pack_propagate(0)
	if w :
		lb.config(width = w)
	if h :
		lb.config(height = h)
	if bg :
		lb.config(bg = bg)
	if fg :
		lb.config(fg = fg)
	if x and y :
		lb.place(x = int(x), y = int(y))
	if cur :
		lb.config(cursor = cur)
	if txt :
		lb.config(text = txt)
	if anc :
		lb.config(anchor = anc)
	if btn == 1 and bg and fg :
		lb.bind('<Enter>', lambda event : event.widget.config(bg = '#A6ABAA', fg = 'white'))
		lb.bind('<Leave>', lambda event : event.widget.config(bg = bg, fg = fg))
	elif btn == 2 :
		lb.bind('<Enter>', lambda event : event.widget.config(relief = 'sunken'))
		lb.bind('<Leave>', lambda event : event.widget.config(relief = 'flat'))
	elif btn == 3 :
		lb.bind('<Enter>', lambda event : event.widget.config(bg = '#252A29'))
		lb.bind('<Leave>', lambda event : event.widget.config(bg = bg))
	return(lb)
