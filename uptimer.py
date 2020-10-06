# ctypes required for using GetTickCount64() 
import ctypes 
#from win10toast import ToastNotifier
import tkinter as tk
from tkinter.messagebox import *


#notifier = ToastNotifier() 

d = {}
day = hour = mins = sec = 0

def display():
	global d
	up()
	tk.Tk().withdraw()
	try:
		#							GUI POP UP
		#		SHORT FORM
		# showinfo("System Uptime For",
		# 		f"{days} {d[int(days)]}, {hour:02}:{mins:02}:{sec:02}")
	
		# 		LONG FORM
		showinfo("System Uptime For",
		f"{days} {d[int(days)]}, {hour:02} {d[int(hour)]}, {mins:02} {d[int(mins)]}, {sec:02} {d[int(sec)]}")
		
		#							NOTIFICATION
		# notifier.show_toast("System Uptime For",
		# 				f"{days} {d[int(days)]}, {hour:02}:{mins:02}:{sec:02}",
		# 	duration=10)

		# notifier.show_toast("System Uptime For",
		# 	f"{days} {d[int(days)]}, {hour:02} {d[int(hour)]}, {mins:02} {d[int(mins)]}, {sec:02} {d[int(sec)]}",
		# 	duration = 25)
	except KeyError:
		#							GUI POP UP
		#		SHORT FORM
		# showinfo("System Uptime For",
		# 		f"{hour:02}:{mins:02}:{sec:02}")

		# 		LONG FORM
		showinfo("System Uptime For",
		f"{hour:02} {d[int(hour)]}, {mins:02} {d[int(mins)]}, {sec:02} {d[int(sec)]}")
		
		#							NOTIFICATION
		#		SHORT FORM
		# notifier.show_toast("System Uptime For",
		# 				f"{hour:02}:{mins:02}:{sec:02}",
		# 	duration=10)

		# 		LONG FORM
		# notifier.show_toast("System Uptime For",
		# 	f"{hour:02} {d[int(hour)]}, {mins:02} {d[int(mins)]}, {sec:02} {d[int(sec)]}",
		# 	duration = 20)


def up():
	global days,hour,mins,sec 
	# getting the library in which GetTickCount64() resides 
	lib = ctypes.windll.kernel32 
	  
	# calling the function and storing the return value 
	t = lib.GetTickCount64() 
	  
	# since the time is in milliseconds i.e. 1000 * seconds 
	# therefore truncating the value 
	t = int(str(t)[:-3]) 
	  
	# extracting hours, minutes, seconds & days from t 
	# variable (which stores total time in seconds) 
	mins, sec = divmod(t, 60) 
	hour, mins = divmod(mins, 60) 
	days, hour = divmod(hour, 24) 
	assigner()
  
# formatting the time in readable form 
# (format = x days, HH:MM:SS) 

#print (type(days))

def assigner():
	global d,days,hour, mins, sec
	if int(days)==0:
		pass
	else:
		if int(days)==1:
			d[int(days)]="day"
		else:
			d[int(days)]="days"
	if int(hour)==1:
		d[int(hour)]="hr"
	else:
		d[int(hour)]="hrs"

	if int(mins)==1:
		d[int(mins)]="min"
	else:
		d[int(mins)]="mins"

	if int(sec)==1:
		d[int(sec)]="second"
	else:
		d[int(sec)]="seconds"