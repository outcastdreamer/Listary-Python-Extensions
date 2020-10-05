from datetime import datetime
import time
import tkinter as tk
import os
from tkinter.filedialog import *
from tkinter.messagebox import *
import json
from pprint import pprint

main_dict = {}

def start():
	"""Takes the project name and time stamp at which the project started at"""
	global main_dict
	time = datetime.now()
	f = open("project.txt","a")
	f.write("\n"+str(time))
	f.close()

	# file = open("project.txt","r")
	# original_time = [i.strip("\n") for i in f.readlines()][1]
	# print(original_time)
	# main_dict[project[0]] = original_time

	#stop(project)   #Comment this later

def stop():
	global main_dict
	# file = open("project.txt","r")
	# project = file.readlines()
	# project[0] = project[0].strip("\n")
	# file.close()
	#time.sleep(4)   #Comment this later

	new_time = datetime.now()
	f = open("project.txt","a")
	f.write("\n"+str(new_time))
	f.close()

	# file = open("project.txt","r")
	# original_time = [i.strip("\n") for i in f.readlines()][-1]
	# print(original_time)
	# main_dict[project] = new_time
	# print("log 1 - Stop time : ",main_dict[project[0]])
	# print("log 2 - Start time : ",main_dict[project[1]])
	calculate()

def calculate():
	global main_dict
	file = open("project.txt","r")
	project = [i.strip("\n") for i in file.readlines()]
	file.close()

	d = {}
	main_dict[project[0]] = project[1]
	main_dict[project[2]] = project[3]
	# print(main_dict)
	s = datetime.strptime(main_dict[project[0]], '%Y-%m-%d %H:%M:%S.%f')
	e = datetime.strptime(main_dict[project[2]], '%Y-%m-%d %H:%M:%S.%f') 
	delta = str(e - s)[:-7]
	main_dict["delta"] = delta

	l_d = delta.split(":")
	if int(l_d[0])<2:
		d[l_d[0]] = "hr"
	else:
		d[l_d[0]] = "hrs"
	if int(l_d[1])<2:
		l_d[1] = l_d[1][1:]
		d[l_d[1]] = "min"
	else:
		d[l_d[1]] = "mins"
	if int(l_d[2])<2:
		d[l_d[2]] = "second"
	else:
		d[l_d[2]] = "seconds"
	main_dict["delta_readable"] = d

	# print("log 3 - Project {} duration : {} hr".format(project.upper(),l_d))
	tk.Tk().withdraw()
	showinfo("Project {} duration : ".format(project[0][:-len("_start\n")+1].upper()),
		"{} {}, {} {}, {} {}".format(l_d[0],d[l_d[0]],l_d[1],d[l_d[1]],l_d[2],d[l_d[2]]))
	history()


def history():
	global main_dict
	final_dict = {}
	# print("log 2:",main_dict,"\n\n")
	proj_name = list(main_dict.keys())[0][:-len("_start\n")+1]
	temp_string = "-".join(main_dict[list(main_dict.keys())[0]].split(" ")[0].split("-")[::-1])
	final_dict["project_name"] = proj_name
	final_dict["date"] = temp_string
	final_dict["start_timestamp"] = main_dict[list(main_dict.keys())[0]][:-7]
	final_dict["stop_timestamp"] = main_dict[list(main_dict.keys())[1]][:-7]
	final_dict["delta"] = main_dict["delta"]
	final_dict["delta_readable"] = main_dict["delta_readable"]
	# print("\nlog final dict : \n",final_dict)
	try:
		with open("hist.json","r") as file:
			new_final_dict = json.load(file)
		# print("\nlog after reading file :\n",new_final_dict)
		# print("\nlog keys : ",list(new_final_dict.keys()))
		date = "-".join(str(datetime.now()).split()[0].split("-")[::-1])
		if date == list(new_final_dict.keys())[0]:
			new_final_dict[final_dict["date"]].append(final_dict)
		else:
			raise Exception()
		# print("\nlog Updated_final_dict :\n")
		# print(new_final_dict)
		with open("hist.json","w") as file:
			json.dump(new_final_dict, file,indent=4)
	except:
		# print("\n\nlog jumped to except clause")
		new_final_dict = {}
		temp_list = []
		temp_list.append(final_dict)
		new_final_dict[final_dict["date"]] = temp_list
		with open("hist.json","w") as file:
			json.dump(new_final_dict, file,indent=4)


def display_hist():
	"""read the hist.json file and display the hist for the day"""
	try:
		with open("hist.json","r") as file:
			reader_dict = json.load(file)
		date = "-".join(str(datetime.now()).split()[0].split("-")[::-1])
		# print("\n\n\tDetailed Logs for today : \n")
		#p# print(reader_dict[date])
		l = reader_dict[date]
		#sl = []
		count = 1
		final_string = ""
		for i in l:
			#sl.append({"project_name":i["project_name"],"delta":i["delta
			final_string+="\n{}. {}\nTime Spent : {}\n".format(count,i["project_name"].upper(),i["delta"])
			count+=1
		tk.Tk().withdraw()
		showinfo("History for Today! ({})".format(date),
			final_string)
	except:
		tk.Tk().withdraw()
		showerror("ERROR!","There are no projects recorded today!")

def cleaner():
	try:
		os.remove("hist.json")
		tk.Tk().withdraw()
		showinfo("LISTARY PY EXTENSION","History has been cleared!")
	except:
		tk.Tk().withdraw()
		showerror("ERROR!","History has already been cleared!")
	# print(final_dict)

if __name__=='__main__':
	os.system("cls")
	pass