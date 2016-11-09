import threading
import time
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import font
from tkinter import *

class GUIThread (threading.Thread):
		
	pages = []
		
	def isInt(x):
		try:
			x = int(x)
			return True
		except:
			return False
		
	def pageCount(self):
		amount = 0
		for i in range(len(self.pages)):
			if self.pages[i] != None:
				amount+=1
		return amount
	
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
		page.id = id
		
		name = self.main.configHandler.get("COM" + str(id) + "name")
		if name == None:
			name = "Eenheid"		
		
		#canvas = tk.Canvas(tab, width=800, height=325, bg="#9F81F7")
		
		page.text = tk.Text(page, width=150, height=20)
		
		page.title = StringVar()
		page.title.set("Loading...")
		page.titleLabel = Label(page, textvariable=page.title, font=self.boldFont, anchor="nw")
		page.titleLabel.place(x=0, y=330)
		
		page.newName = StringVar()
		page.newName.set(name)
		page.newNameEntry = tk.Entry(page, textvariable=page.newName, width=20)
		self.placeItem(page.newNameEntry, 0, 0)
		
		page.setNewName = tk.Button(page, text='Save Name', width=16, command=lambda: self.setTitle(page, page.newName.get()))
		self.placeItem(page.setNewName, 1, 0)
		
		page.newBaseVal = StringVar()
		page.newBaseValEntry = tk.Entry(page, textvariable=page.newBaseVal, width=20)
		self.placeItem(page.newBaseValEntry, 0, 1)

		page.setNewBaseVal = tk.Button(page, text='Set Base', width=16)
		self.placeItem(page.setNewBaseVal, 1, 1)

		self.tabs.add(page, text=name)
		self.pages[id] = page
		
		return page
		
	def placeItem(self, item, row, colomn):
		item.place(x=(5 + 125 * colomn + 5 * colomn), y=(390 + 20 * row + 5 * row))
		
	def setTitle(self, page, title):
		self.tabs.tab(page, text=title)
		self.main.configHandler.set("COM" + str(page.id) + "name", title)
		
	def setPageType(self, portThread, type):
		page = self.pages[portThread.id]
		
		if type == "temperature":
			page.title.set("Temperature")
			page.text.place(x=0, y=0)
			
		elif type == "remand":
			page.title.set("Remand")
			page.text.place(x=0, y=0)
	
	def addText(self, field, text):
		field.insert(END, text + '\n')
		
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
		