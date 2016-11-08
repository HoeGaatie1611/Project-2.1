import threading
import time
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import font
from tkinter import *

class GUIThread (threading.Thread):
		
	pages = []
		
	def quit(self):
		self.root.destroy()
	
	def togglePage(self, id):
		if self.pages[id] != None:
			self.removePage(id)
		else:
			self.createPage(id)
			
	def removePage(self, id):
		self.pages[id].destroy()
		self.pages[id] = None
	
	def createPage(self, id):
		while(len(self.pages) <= id):
			self.pages.append(None)
			
		page = ttk.Frame(self.tabs)
		
		tab = ttk.Notebook(page)
		tab1 = ttk.Frame(self.tabs)
		tab2 = ttk.Frame(self.tabs)

		label = Label(tab1, text="Centrale 2.1", font=self.boldFont, anchor="nw")
		label.pack(expand=0, fill="both")
		
		tab.add(tab1, text = "Temperatuursensor")
		tab.add(tab2, text = "Lichtsensoren")
		tab.pack(expand=1, fill="both")

		canvas1 = tk.Canvas(tab1, width=800, height=325,bg="#9F81F7")
		canvas1.pack(padx=20, pady=20, side="top", anchor="nw")
		
		canvas2 = tk.Canvas(tab2, width=800, height=325,bg="red")
		canvas2.pack(padx=20, pady=20, side="top", anchor="nw")
		
		self.tabs.add(page, text='  Arduino ' + str(id) + '  ')
		self.pages[id] = page
		
		return page
		
	def loadGUI(self):
		pages = []
	
		"""Create the window"""
		self.root = tk.Tk()
		self.root.title("Arduino GUI")
		self.root.geometry("1200x600")
		
		"""fonts"""
		normal = font.Font(name="normal_font", size=16)
		self.normalFont = font.Font(family='Times', size=16)
		self.boldFont = font.Font(family='Times', size=26, weight = "bold")
		
		"""Create & Style the tabs"""
		self.tabs = ttk.Notebook(self.root)
		s = ttk.Style()
		s.configure(".", font=self.normalFont)
		
		"""Configure main tab"""
		mainPage = ttk.Frame(self.tabs)
		
		"""Add tabs to frame"""
		self.tabs.add(mainPage, text="    Home    ")
			
		self.tabs.pack(expand=1, fill="both")
		
		#Favicon / map zelf aanpassen aan path
		#self.root.iconbitmap(r'\Project2.1\Project-2.1\Python Code\favicon.ico')
		
		#Fixedwindow / niet resizable
		self.root.resizable(width=False, height=False)
		
		"""Run the program"""
		self.root.mainloop()
		
	#
		
	def __init__(self, main):
		self.main = main
		threading.Thread.__init__(self)

	def run(self):
		self.loadGUI()
		