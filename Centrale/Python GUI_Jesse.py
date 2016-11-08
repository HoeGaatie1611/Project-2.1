"""Import Stuff..."""
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import font
from tkinter import *

ArduinoOn = 1

def Application():
	"""Create the window"""
	root = tk.Tk()
	root.title("Arduino GUI")
	root.geometry("1200x600")
	
	
	
	"""Nuttelozen knop ;)"""
	def quit(): #Misschien veranderd
		root.destroy()
	
	def set_values(): #veranderd
		master = Tk()
		master.geometry("115x150")
		master.title('EZ code')
		Label(master, text="Minimale Waarde:").grid(row=0,column=1)

		e2 = Checkbutton(master, text="Arduino 1", command= lambda: hideArduino(page2, 2))
		e3 = Checkbutton(master, text="Arduino 2", command= lambda: hideArduino(page3, 3))
		e4 = Checkbutton(master, text="Arduino 3", command= lambda: hideArduino(page4, 4))
		e5 = Checkbutton(master, text="Arduino 4", command= lambda: hideArduino(page5, 5))
		e6 = Checkbutton(master, text="Arduino 5", command= lambda: hideArduino(page6, 6))
		

		e2.grid(row=1, column=1, sticky=W)
		e3.grid(row=2, column=1, sticky=W)
		e4.grid(row=3, column=1, sticky=W)
		e5.grid(row=4, column=1, sticky=W)
		e6.grid(row=5, column=1, sticky=W)
		
		#e1 = e1
		#e2 = e2

		#Button(master, text='Sluit').grid(row=6, column=0, sticky=W, pady=4)
		#Button(master, text='Set').grid(row=6, column=1, sticky=W, pady=4)
	
	
	
	"""Hide the tab"""
	def hideArduino(Value, paginaNR): #Veranderd
		#global ArduinoOn
		print("Je moeder = " + str(Value))
		try:
			tabs.forget(Value)
		except TclError:
			showArduino(Value, paginaNR)
			#tabs.add(Value, text="  Arduino ")
			#tabs.pack(expand=1, fill="both")
		
		
		#if(ArduinoOn == 1):
			#tabs.forget(Value)
		#	tabs.forget(Value)
			#ArduinoOn = 1
		#else:
		#	for i in range(4):
		#		tabs.forget(tabs.index(1))
		#	tabs.add(page2, text="  Arduino 1  ")
		#	tabs.add(page3, text='  Arduino 2  ')
		#	tabs.add(page4, text="  Arduino 3  ")
		#	tabs.add(page5, text="  Arduino 4  ")
		#	tabs.add(page6, text="  Arduino 5  ")
		#	makeTabs()
		#	ArduinoOn = 1
	
	
	
	"""fonts"""
	normal = font.Font(name="normal_font", size=16)
	font1 = font.Font(family='Times', size=16)
	font2 = font.Font(family='Times', size=26, weight = "bold")
	
	
	
	"""Create & Style the tabs"""
	tabs = ttk.Notebook(root)
	s = ttk.Style()
	s.configure(".", font=font1)
	
	
	"""Configure first tab"""
	page1 = ttk.Frame(tabs)
	
	#button1 = tk.Button(page1)
	#button1.configure(text = "Disable Arduino 1")
	#button1.grid()
	
	button2 = tk.Button(page1)
	button2.configure(text = "Nuttelozen knop", command=set_values)
	button2.grid()
	

	
	"""Configure second tab"""
	page2 = ttk.Frame(tabs)
		
	tabs2 = ttk.Notebook(page2)
	tab2_1 = ttk.Frame(tabs2)
	tab2_2 = ttk.Frame(tabs2)
	

	label2_1 = Label(tab2_1, text = "Centrale 2.1", font = font2, anchor="nw")
	label2_1.pack(expand=0, fill="both")
	
	tabs2.add(tab2_1, text = "Temperatuursensor")
	tabs2.add(tab2_2, text = "Lichtsensoren")
	tabs2.pack(expand=1, fill="both")

	canvas2_1 = tk.Canvas(tab2_1, width=800, height=325,bg="#9F81F7")
	canvas2_1.pack(padx = 20, pady = 20, side="top", anchor = "nw")
	
	canvas2_2 = tk.Canvas(tab2_2, width=800, height=325,bg="red")
	canvas2_2.pack(padx = 20, pady = 20, side="top", anchor = "nw")
	
	
	
	"""Configure third tab"""
	page3 = ttk.Frame(tabs)
	
	tabs3 = ttk.Notebook(page3)
	tab3_1 = ttk.Frame(tabs3)
	tab3_2 = ttk.Frame(tabs3)
	
	tabs3.add(tab3_1, text = "Temperatuursensor")
	tabs3.add(tab3_2, text = "Lichtsensoren")
	tabs3.pack(expand=1, fill="both")
	
	canvas3_1 = tk.Canvas(tab3_1, width=800, height=325,bg="#9F81F7")
	canvas3_1.pack(padx = 20, pady = 20, side="top", anchor = "nw")
	
	canvas3_2 = tk.Canvas(tab3_2, width=800, height=325,bg="red")
	canvas3_2.pack(padx = 20, pady = 20, side="top", anchor = "nw")
	
	
	
	"""Configure fourth tab"""
	page4 = ttk.Frame(tabs)
	
	tabs4 = ttk.Notebook(page4)
	tab4_1 = ttk.Frame(tabs4)
	tab4_2 = ttk.Frame(tabs4)
	
	tabs4.add(tab4_1, text = "Temperatuursensor")
	tabs4.add(tab4_2, text = "Lichtsensoren")
	tabs4.pack(expand=1, fill="both")
	
	canvas4_1 = tk.Canvas(tab4_1, width=800, height=325,bg="#9F81F7")
	canvas4_1.pack(padx = 20, pady = 20, side="top", anchor = "nw")
	
	canvas4_2 = tk.Canvas(tab4_2, width=800, height=325,bg="red")
	canvas4_2.pack(padx = 20, pady = 20, side="top", anchor = "nw")
	
	
	
	"""Configure fifth tab"""
	page5 = ttk.Frame(tabs)
	
	tabs5 = ttk.Notebook(page5)
	tab5_1 = ttk.Frame(tabs5)
	tab5_2 = ttk.Frame(tabs5)
	
	tabs5.add(tab5_1, text = "Temperatuursensor")
	tabs5.add(tab5_2, text = "Lichtsensoren")
	tabs5.pack(expand=1, fill="both")
	
	canvas5_1 = tk.Canvas(tab5_1, width=800, height=325,bg="#9F81F7")
	canvas5_1.pack(padx = 20, pady = 20, side="top", anchor = "nw")
	
	canvas5_2 = tk.Canvas(tab5_2, width=800, height=325,bg="red")
	canvas5_2.pack(padx = 20, pady = 20, side="top", anchor = "nw")
	
	
	
	"""Configure sixth tab"""
	page6 = ttk.Frame(tabs)
	
	tabs6 = ttk.Notebook(page6)
	tab6_1 = ttk.Frame(tabs6)
	tab6_2 = ttk.Frame(tabs6)
	
	tabs6.add(tab6_1, text = "Temperatuursensor")
	tabs6.add(tab6_2, text = "Lichtsensoren")
	tabs6.pack(expand=1, fill="both")
	
	canvas6_1 = tk.Canvas(tab6_1, width=800, height=325,bg="#9F81F7")
	canvas6_1.pack(padx = 20, pady = 20, side="top", anchor = "nw")
	
	canvas6_2 = tk.Canvas(tab6_2, width=800, height=325,bg="red")
	canvas6_2.pack(padx = 20, pady = 20, side="top", anchor = "nw")
	
	
	
	"""Add tabs to frame""" #Misschien veranderd.....
	print("Je moeder")
	tabs.add(page1, text="    Index    ")
	tabs.add(page2, text='  Arduino 1  ')
	tabs.add(page3, text='  Arduino 2  ')
	tabs.add(page4, text="  Arduino 3  ")
	tabs.add(page5, text="  Arduino 4  ")
	tabs.add(page6, text="  Arduino 5  ")
	tabs.pack(expand=1, fill="both")

	def showArduino(Value, paginaNR): #Nieuwe regel / veranderd
		fNewList = list(str(Value)) 
		print(fNewList)
		tabs.add(Value, text="  Arduino " + str(paginaNR-1) + "  ") #BUG: Hij wilt niet de goede tab weer toevoegen. Hij voegt namelijk een random waarde toe!
		tabs.pack(expand=1, fill="both")
	
	"""Run the program"""
	root.mainloop()

	
if __name__ == "__main__":
	Application()
