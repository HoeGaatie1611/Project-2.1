# -*- coding: utf-8 -*-
## The coding part above is necessary to show the celcius degree sign.
import threading
import time
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import font
from tkinter import *

class GUIThread (threading.Thread):

	pages = []

	#Page methods
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
		name = self.main.configHandler.get("COM" + str(id) + "name")
		if name != None:
			self.port = self.main.serialThread.ports[id]

			while(len(self.pages) <= id):
				self.pages.append(None)

			page = ttk.Frame(self.tabs)
			page.id = id
			
			#Name
			page.title = StringVar()
			page.title.set("Loading...")
			page.titleLabel = Label(page, textvariable=page.title, font=self.boldFont, anchor="nw")
			page.titleLabel.place(x=0, y=330)

			page.newName = StringVar()
			page.newName.set(name)
			page.newNameEntry = tk.Entry(page, textvariable=page.newName, width=20)
			self.placeItem(page.newNameEntry, 0, 0)

			page.setNewName = tk.Button(page, text='Opslaan', width=16, command=lambda: self.setTitle(page, page.newName.get()))
			self.placeItem(page.setNewName, 1, 0)

			#Base values and roll buttons
			page.baseVal = IntVar()

			page.rollStatus = StringVar()
			page.rollStatusLabel = Label(page, textvariable=page.rollStatus, font=self.normalFont, anchor="nw")
			self.placeItem(page.rollStatusLabel, 5, 0)

			#Autonoom mode
			page.mode = StringVar()
			page.modeLabel = Label(page, textvariable=page.mode, font=self.normalFont, anchor="nw")
			self.placeItem(page.modeLabel, 0, 1)

			page.changeMode = tk.Button(page, text='Change mode', width=16, command=lambda: self.port.sendCommand("autonoom", 1 if page.autonoom == 0 else 0))
			self.placeItem(page.changeMode, 5, 1)

			page.autonoom = 0
			self.addBaseInput(page)

			#Max roll distance
			page.maxRoll = IntVar()
			page.maxRollTitleLabel = Label(page, text="Max roll distance", font=self.normalFont, anchor="nw")
			page.maxRollLabel = Label(page, textvariable=page.maxRoll, font=self.normalFont, anchor="nw")
			page.incMaxRoll = tk.Button(page, text='Increase', width=16, command=lambda: self.port.sendCommand("incMaxRoll", 0))
			page.decMaxRoll = tk.Button(page, text='Decrease', width=16, command=lambda: self.port.sendCommand("decMaxRoll", 0))
			self.placeItem(page.maxRollTitleLabel, 0, 2)
			self.placeItem(page.maxRollLabel, 1, 2)
			self.placeItem(page.incMaxRoll, 2, 2)
			self.placeItem(page.decMaxRoll, 3, 2)

			self.tabs.add(page, text=name)
			self.pages[id] = page
			
			#Graph
			page.isGraphSet = 0
			page.i = 1
			page.y2 = 280
			page.x1 = 40
			page.x2 = 40
			
			return page

	def addBaseInput(self, page):
		page.baseValLabel = Label(page, textvariable=page.baseVal, font=self.normalFont, anchor="nw")
		page.incBase = tk.Button(page, text='Increase', width=16, command=lambda: self.port.sendCommand("incBase", 0))
		page.decBase = tk.Button(page, text='Decrease', width=16, command=lambda: self.port.sendCommand("decBase", 0))
		self.placeItem(page.baseValLabel, 1, 1)
		self.placeItem(page.incBase, 2, 1)
		self.placeItem(page.decBase, 3, 1)
		page.mode.set("Mode: Sensor")

	def addRollInput(self, page):
		page.rollIn = tk.Button(page, text='Roll in', width=16, command=lambda: self.port.sendCommand("rollIn", 0))
		page.rollOut = tk.Button(page, text='Roll out', width=16, command=lambda: self.port.sendCommand("rollOut", 0))
		self.placeItem(page.rollIn, 2, 1)
		self.placeItem(page.rollOut, 3, 1)
		page.mode.set("Mode: Manual")

	def removeBaseInput(self, page):
		try:
			page.baseValLabel.destroy()
			page.incBase.destroy()
			page.decBase.destroy()
		except: return

	def removeRollInput(self, page):
		try:
			page.rollIn.destroy()
			page.rollOut.destroy()
		except: return

	# GUI methods
	def placeItem(self, item, row, colomn): # get x and y for buttons and labels for a nice grid layout under graph
		item.place(x=(5 + 130 * colomn), y=(390 + 30 * row))

	def setTitle(self, page, title):
		self.tabs.tab(page, text=title)
		self.main.configHandler.set("COM" + str(page.id) + "name", title)

	def setPageType(self, portThread, type):
		page = self.pages[portThread.id]

		if type == "temperature":
			page.title.set("Temperature")

		elif type == "remand":
			page.title.set("Remand")

	def createTempGraph(self, page):
		if(page.isGraphSet == 0):
			## Creates lines and graph
			page.isGraphSet = 1
			page.canvas = Canvas(page, width=150, height=320, bg='white') # 0,0 is top left corner
			page.canvas.pack(expand=NO, fill=BOTH)
			page.canvas.create_line(40,280,1100,280, width=2) # x-axis
			page.canvas.create_line(40,20,40,280, width=2)    # y-axis
			
			## Hier wordt het aantal minuten weergegeven op de x-as
			for i in range(21):
				x = 40 + (i * 53)
				page.canvas.create_line(x,280,x,20, width=1, dash=(2,5))
				page.canvas.create_text(x,280, text='%d min'% (i), anchor=N)
				
			## Hier wordt de temperatuur weergegeven op de y-as.
			for i in range(10):
				y = 254 - (i * 26)
				page.canvas.create_line(1100,y,40,y, width=1, dash=(2,5))
				degree_sign = u'\N{DEGREE SIGN}'
				page.canvas.create_text(20,y, text='%d°'% (5 + (i * 5)), anchor=N)

	def updateTempGraph(self, page, data):
		if page.i == 21:
	        # new frame
			page.i = 1
			page.y2 = 280
			page.canvas.delete('temp') # only delete items tagged as temp
			
		if(page.i == 1):
			page.y2 = 280
			page.x2 = 40
			page.x1 = 40
			
		y1 = page.y2
		page.x1 = page.x2
		page.y2 = 280 - (((data / 4) * 26) - 26)
		page.x2 = 40 + (53*page.i)
		page.canvas.create_line(page.x1, y1, page.x2, page.y2, fill='blue', tags='temp', width=2)
		page.i += 1

	def createRemandObjects(self, page):
		if(page.isGraphSet == 0):
			page.isGraphSet = 1
			page.canvas = Canvas(page, width=150, height=320, bg='white')
			page.canvas.pack(expand=NO, fill=BOTH)
			page.canvas.create_line(60,280,1120,280, width=2) # x-axis
			page.canvas.create_line(60,20,60,280, width=2)    # y-axis
			
			for i in range(21):
				x = 60 + (i * 53)
				page.canvas.create_line(x,280,x,20, width=1, dash=(2,5))
				page.canvas.create_text(x,280, text='%d min'% (i), anchor=N)
				
			## Hier wordt de temperatuur weergegeven op de y-as.
			for i in range(10):
				y = 254 - (i * 26)
				page.canvas.create_line(1120,y,60,y, width=1, dash=(2,5))
				page.canvas.create_text(30,y, text='%d Rem'% (15 + (i * 15)), anchor=N, font=("Times New Roman", 7))
				
			canvas2 = Canvas(page, width = 650, height = 200)
			canvas2.pack(side = RIGHT, anchor = SE)
			page.image = PhotoImage(file="remandTabel.gif", width = 600, height = 200)
			canvas2.create_image(300,100, image=page.image)

	def updateRemandGraph(self, page, data):
		if page.i == 21:
	        # new frame
			page.i = 1
			page.y2 = 280
			page.canvas.delete('temp') # only delete items tagged as temp
		if(page.i == 1):
			page.y2 = 280
			page.x2 = 60
			page.x1 = 60
		y1 = page.y2
		page.x1 = page.x2
		page.y2 = 280 - (((data / 15) * 26))
		page.x2 = 60 + (53*page.i)
		page.canvas.create_line(page.x1, y1, page.x2, page.y2, fill='blue', tags='temp', width=2)
		page.i += 1
		
	def updateSensorAmount(self):
		amountPages = self.pageCount()
		
		if(amountPages == 1):
			self.sensorText.set("Er is op dit moment: " + str(amountPages) + " sensor aangesloten.")
		else:
			self.sensorText.set("Er zijn op dit moment: " + str(amountPages) + " sensoren aangesloten.")

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

		self.sensorText = StringVar()
		
		self.mainCanvas = Canvas(mainPage, width = 1000, height = 500)
		self.mainCanvas.pack()
		self.logo = PhotoImage(file="logo.gif")
		self.mainCanvas.create_image(500,300, image=self.logo)
		self.mainCanvas.create_text(500,20,anchor=N,text="De Centrale", font=("Times New Roman", 30))
		self.mainCanvas.create_text(500,150,anchor=N,text="Ontwikkeld door Johto IT in opdracht van Zeng LTD", font=("Times New Roman", 15))
		self.mainCanvas.create_text(500,450,anchor=N,text="'The very best, like no one ever was'", font=("Times New Roman", 8, "italic"))
		
		self.sensorLabel = Label(mainPage, textvariable=self.sensorText, font=("Times New Roman", 15), anchor=N)
		self.sensorLabel.place(x=425, y=90)
		
		self.tabs.pack(expand=1, fill="both")

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
