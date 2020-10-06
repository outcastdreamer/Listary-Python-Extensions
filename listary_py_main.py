import tkinter as tk
from tkinter.filedialog import *
from tkinter.messagebox import *
import os
from os import system as st
from subprocess import Popen, PIPE
import pyperclip as pc 
from PyDictionary import PyDictionary
import ctypes
#from win10toast import ToastNotifier
import uptimer
import project_manager

main_path = os.path.abspath(r"C:\Users\Username\Add path to\listary_py_main")

#notif = ToastNotifier()

x = ""
output = ""
master = PyDictionary()
main_file = os.path.abspath(main_path+"/listary_py_main.py")
#print(main_path)


button1 = None
button2 = None
entry1 = None

def func(event):
	global button1,button2,entry1,x,root,main_path,master 
	button1.invoke()
	root.destroy()

def getText ():
	global button1,button2,entry1,x,root,main_path,master 
	x = entry1.get()

def Clipboard(o):
	global x,output
	pc.copy(o)
	tk.Tk().withdraw()
	showinfo("LISTARY PY","Text copied to clipboard!")
	#notif.show_toast("LISTARY PY","Text copied to clipboard!",duration=4)


root= tk.Tk()
root.title("LISTARY PY EXTENSION")
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)
root.resizable(False, False)  # This code helps to disable windows from resizing
root.eval('tk::PlaceWindow . center') 
root.deiconify()
canvas1 = tk.Canvas(root, width = 400, height = 180,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='ENTER CMD COMMAND : ')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type 1 to select your current working directory')
label2.config(font=('helvetica', 10))

label3 = tk.Label(root, text='Press ENTER to execute command')
label3.config(font=('helvetica', 10))

canvas1.create_window(190, 50, window=label2)
canvas1.create_window(190, 70, window=label3)

entry1 = tk.Entry (root)
entry1.insert(END,pc.paste())
entry1.focus()
canvas1.create_window(200, 100, window=entry1)

button1 = tk.Button(root,text='Useless Button',command=getText, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 140, window=button1)

root.bind('<Return>', func)
root.mainloop()



def main():
	global button1,button2,entry1,x,root,main_path,master,output
	global days,hour,mins,sec,d
	
	new_path = "" 
	try:
		if int(x) == 1:
			
			tk.Tk().withdraw()
			new_path = os.path.abspath(askdirectory())
			os.chdir(main_path)
			f = open("path.txt","w")
			f.write(new_path)
			f.close()
			st("python \"%s\""%(main_file))
	except:
		
		os.chdir(main_path)
		f = open("path.txt","r")
		new_path = f.read()
		f.close()
		if x.lower()=="up" or x.lower()=="uptime":
			
			uptimer.display()
		elif "dy" in x.lower()[0:2]:
			#insert offline or not checker here
			if "dy m " in x.lower():
				m = x[5:]
				tk.Tk().withdraw()
				showinfo("Meaning of %s"%(m),master.meaning(m))
			elif "dy s " in x.lower():
				s = x[5:]
				tk.Tk().withdraw()
				showinfo("Synonym of %s"%(s),master.synonym(s))
			elif "dy a " in x.lower():
				a = x[5:]
				tk.Tk().withdraw()
				showinfo("Antonym of %s"%(a),master.antonym(a))
		elif "for" in x.lower()[0:3]:
			if "for l " in x.lower():
				output = x[6:].lower()
			elif "for u " in x.lower():
				output = x[6:].upper()
			elif "for t " in x.lower():
				output = x[6:].title()
			elif "for r " in x.lower():
				output = x[6:][::-1]
			elif "for s " in x.lower():
				output = "".join([u'\u0336{}'.format(c) for c in x[6:]+"  "])[1:]
				output = " "+output
			elif "for sl " in x.lower():
				output = "".join([u'\u2215{}'.format(c) for c in x[7:]+"  "])[1:]
				output = " "+output
			elif "for st " in x.lower():
				output = "".join([u'\u2215{}'+u'\u0336'.format(c) for c in x[7:]+"  "])
				output = " "+output
			Clipboard(output)
		elif "start" in x.lower()[0:5]:
			
			proj = x[6:]+"_start"
			
			os.chdir(main_path)
			try:
				f = open("project.txt","r")
				l = f.readlines()
				
				f.close()
				if len(l)==2:
					tk.Tk().withdraw()
					showerror("ERROR!","Previous Project \"{}\" is still running!!!".format(l[0].upper()[:-len("_start\n")]))
				else:
					file = open("project.txt","w")
					file.write(proj)
					file.close()
					project_manager.start()
			except:
				
				file = open("project.txt","w")
				file.write(proj)
				file.close()
				project_manager.start()
			
		elif "stop" in x.lower()[0:4]:
			os.chdir(main_path)
			file = open("project.txt","r")
			p = file.readlines()
			proj = p[0][:-len("_start\n")]
			
			
			file.close()
			file = open("project.txt","a")
			proj = "\n"+proj+"_stop"
			
			file.write(proj)
			file.close()
			project_manager.stop()
		elif "hist" in x.lower()[0:4] or "history" in x.lower()[0:7]:
			project_manager.display_hist()
		elif "clr p" in x.lower()[0:5]:
			project_manager.clear_prev()
		elif "clr" in x.lower()[0:3]:
			project_manager.cleaner()	
		elif new_path!="":
			os.chdir(new_path)
			try:
				ot = Popen("%s"%(x),stdout=PIPE)
				r = ot.communicate()
				tk.Tk().withdraw()
				showinfo("Successfully Excecuted!","Your CMD command was successfully executed!")
			except:
				if len(x)==0:
					pass
				else:
					tk.Tk().withdraw()
					showerror("ERROR!","Not a valid CMD or LISTARY PY command! Please try again!")
		else:
			
			os.chdir(main_path)
			try:
				ot = Popen("%s"%(x),stdout=PIPE)
				r = ot.communicate()
				tk.Tk().withdraw()
				showinfo("Successfully Excecuted!","Your CMD command was successfully executed!")
			except:
				if len(x)==0:
					pass
				else:
					tk.Tk().withdraw()
					showerror("ERROR!","Not a valid CMD or LISTARY PY command! Please try again!")
			# st(x+" > cmd.txt")
			# f = open("cmd.txt","r")
			# command = "".join(f.readlines())
			# #
			# f.close()
			# if len(command)<1:
			# 	tk.Tk().withdraw()
			# 	showerror("ERROR!","Not a valid CMD or LISTARY PY command!")

"""
 Things to add:
	- Offline working dictionary and display error for limited dictionary options if offline (offline checking mechanism)
	- Better and cleaner GUI (maybe)
	- Weather and config for weather
	- config.json : set main_path, & other parameters here.
	- currency converter
"""
if __name__ == '__main__':
	main()


