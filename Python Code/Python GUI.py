"""Import Stuff..."""
//update
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import font
from tkinter import *

ArduinoOn = 1

class Application():
	"""Nuttelozen knop ;)"""
	def quit(self):
		root.destroy()

	"""Hide the tab"""
	def hideArduino(self):
		global ArduinoOn

		if(ArduinoOn == 1):
			self.tabs.forget(self.page2)
			ArduinoOn = 0
		else:
			self.tabs.add(self.page2, text='  Arduino 1  ')
			self.ArduinoOn = 1


	def __init__(self):

		"""Create the window"""
		root = tk.Tk()
		root.title("Arduino GUI")
		root.geometry("1200x600")
		print(ArduinoOn)

		"""fonts"""
		normal = font.Font(name="normal_font", size=16)
		font1 = font.Font(family='Times', size=16)
		font2 = font.Font(family='Times', size=26, weight = "bold")



		"""Create the tabs"""
		self.tabs = ttk.Notebook(root)

		s = ttk.Style()
		s.configure(".", font=font1)


		"""Configure first tab"""
		self.page1 = ttk.Frame(self.tabs)

		button1 = tk.Button(self.page1)
		button1.configure(text = "Disable Arduino 1", command=  self.hideArduino)
		button1.grid()

		button2 = tk.Button(self.page1)
		button2.configure(text = "Nuttelozen knop", command=quit)
		button2.grid()



		"""Configure second tab"""
		self.page2 = ttk.Frame(self.tabs)

		self.tabs2 = ttk.Notebook(self.page2)
		self.tab2_1 = ttk.Frame(self.tabs2)
		self.tab2_2 = ttk.Frame(self.tabs2)


		self.label2_1 = Label(self.tab2_1, text = "Centrale 2.1", font = font2, anchor="nw")
		self.label2_1.pack(expand=0, fill="both")

		self.tabs2.add(self.tab2_1, text = "Temperatuursensor")
		self.tabs2.add(self.tab2_2, text = "Lichtsensoren")
		self.tabs2.pack(expand=1, fill="both")

		self.canvas2_1 = tk.Canvas(self.tab2_1, width=800, height=325,bg="#9F81F7")
		self.canvas2_1.pack(padx = 20, pady = 20, side="top", anchor = "nw")

		self.canvas2_2 = tk.Canvas(self.tab2_2, width=800, height=325,bg="red")
		self.canvas2_2.pack(padx = 20, pady = 20, side="top", anchor = "nw")



		"""Configure third tab"""
		self.page3 = ttk.Frame(self.tabs)

		self.tabs3 = ttk.Notebook(self.page3)
		self.tab3_1 = ttk.Frame(self.tabs3)
		self.tab3_2 = ttk.Frame(self.tabs3)

		self.tabs3.add(self.tab3_1, text = "Temperatuursensor")
		self.tabs3.add(self.tab3_2, text = "Lichtsensoren")
		self.tabs3.pack(expand=1, fill="both")

		self.canvas3_1 = tk.Canvas(self.tab3_1, width=800, height=325,bg="#9F81F7")
		self.canvas3_1.pack(padx = 20, pady = 20, side="top", anchor = "nw")

		self.canvas3_2 = tk.Canvas(self.tab3_2, width=800, height=325,bg="red")
		self.canvas3_2.pack(padx = 20, pady = 20, side="top", anchor = "nw")



		"""Configure fourth tab"""
		self.page4 = ttk.Frame(self.tabs)

		self.tabs4 = ttk.Notebook(self.page4)
		self.tab4_1 = ttk.Frame(self.tabs4)
		self.tab4_2 = ttk.Frame(self.tabs4)

		self.tabs4.add(self.tab4_1, text = "Temperatuursensor")
		self.tabs4.add(self.tab4_2, text = "Lichtsensoren")
		self.tabs4.pack(expand=1, fill="both")

		self.canvas4_1 = tk.Canvas(self.tab4_1, width=800, height=325,bg="#9F81F7")
		self.canvas4_1.pack(padx = 20, pady = 20, side="top", anchor = "nw")

		self.canvas4_2 = tk.Canvas(self.tab4_2, width=800, height=325,bg="red")
		self.canvas4_2.pack(padx = 20, pady = 20, side="top", anchor = "nw")



		"""Configure fifth tab"""
		self.page5 = ttk.Frame(self.tabs)

		self.tabs5 = ttk.Notebook(self.page5)
		self.tab5_1 = ttk.Frame(self.tabs5)
		self.tab5_2 = ttk.Frame(self.tabs5)

		self.tabs5.add(self.tab5_1, text = "Temperatuursensor")
		self.tabs5.add(self.tab5_2, text = "Lichtsensoren")
		self.tabs5.pack(expand=1, fill="both")

		self.canvas5_1 = tk.Canvas(self.tab5_1, width=800, height=325,bg="#9F81F7")
		self.canvas5_1.pack(padx = 20, pady = 20, side="top", anchor = "nw")

		self.canvas5_2 = tk.Canvas(self.tab5_2, width=800, height=325,bg="red")
		self.canvas5_2.pack(padx = 20, pady = 20, side="top", anchor = "nw")



		"""Configure sixth tab"""
		self.page6 = ttk.Frame(self.tabs)

		self.tabs6 = ttk.Notebook(self.page6)
		self.tab6_1 = ttk.Frame(self.tabs6)
		self.tab6_2 = ttk.Frame(self.tabs6)

		self.tabs6.add(self.tab6_1, text = "Temperatuursensor")
		self.tabs6.add(self.tab6_2, text = "Lichtsensoren")
		self.tabs6.pack(expand=1, fill="both")

		self.canvas6_1 = tk.Canvas(self.tab6_1, width=800, height=325,bg="#9F81F7")
		self.canvas6_1.pack(padx = 20, pady = 20, side="top", anchor = "nw")

		self.canvas6_2 = tk.Canvas(self.tab6_2, width=800, height=325,bg="red")
		self.canvas6_2.pack(padx = 20, pady = 20, side="top", anchor = "nw")



		"""Add tabs to frame"""
		self.tabs.add(self.page1, text="    Index    ")
		self.tabs.add(self.page2, text='  Arduino 1  ')
		self.tabs.add(self.page3, text='  Arduino 2  ')
		self.tabs.add(self.page4, text="  Arduino 3  ")
		self.tabs.add(self.page5, text="  Arduino 4  ")
		self.tabs.add(self.page6, text="  Arduino 5  ")
		self.tabs.pack(expand=1, fill="both")
		
		#Favicon / map zelf aanpassen aan path
		#root.iconbitmap(r'Z:\Project2.1\Project-2.1\Python Code\favicon.ico')
	
		#Fixedwindow / niet resizable
		root.resizable(width=False, height=False)



		"""Run the program"""
		root.mainloop()




if __name__ == "__main__":
	Application()
