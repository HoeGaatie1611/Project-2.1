"""Import Stuff..."""
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import font
from tkinter import *

def Application():

	pages = []
	
	"""Create the window"""
	root = tk.Tk()
	root.title("Arduino GUI")
	root.geometry("1200x600")
		
	def quit():
		root.destroy()
	
	def set_values(): #Test for tab removal (temp)
		master = Tk()
		master.geometry("115x150")
		master.title('EZ code')
		Label(master, text="Minimale Waarde:").grid(row=0,column=1)

		e2 = Checkbutton(master, text="Arduino 1", command= lambda: togglePage(0))
		e3 = Checkbutton(master, text="Arduino 2", command= lambda: togglePage(1))
		e4 = Checkbutton(master, text="Arduino 3", command= lambda: togglePage(2))
		e5 = Checkbutton(master, text="Arduino 4", command= lambda: togglePage(3))
		e6 = Checkbutton(master, text="Arduino 5", command= lambda: togglePage(4))

		e2.grid(row=1, column=1, sticky=W)
		e3.grid(row=2, column=1, sticky=W)
		e4.grid(row=3, column=1, sticky=W)
		e5.grid(row=4, column=1, sticky=W)
		e6.grid(row=5, column=1, sticky=W)
	
	def togglePage(id):
		if pages[id] != None:
			removePage(id)
		else:
			createPage(id)
			
	def removePage(id):
		pages[id].destroy()
		pages[id] = None
	
	def createPage(id):
		while(len(pages) <= id):
			pages.append(None)
			
		page = ttk.Frame(tabs)
		
		tab = ttk.Notebook(page)
		tab1 = ttk.Frame(tabs)
		tab2 = ttk.Frame(tabs)

		label = Label(tab1, text = "Centrale 2.1", font=boldFont, anchor="nw")
		label.pack(expand=0, fill="both")
		
		tab.add(tab1, text = "Temperatuursensor")
		tab.add(tab2, text = "Lichtsensoren")
		tab.pack(expand=1, fill="both")

		canvas1 = tk.Canvas(tab1, width=800, height=325,bg="#9F81F7")
		canvas1.pack(padx = 20, pady = 20, side="top", anchor = "nw")
		
		canvas2 = tk.Canvas(tab2, width=800, height=325,bg="red")
		canvas2.pack(padx = 20, pady = 20, side="top", anchor = "nw")
		
		tabs.add(page, text='  Arduino ' + str(id + 1) + '  ')
		pages[id] = page
		
		return page
		
	"""fonts"""
	normal = font.Font(name="normal_font", size=16)
	normalFont = font.Font(family='Times', size=16)
	boldFont = font.Font(family='Times', size=26, weight = "bold")
	
	"""Create & Style the tabs"""
	tabs = ttk.Notebook(root)
	s = ttk.Style()
	s.configure(".", font=normalFont)
	
	"""Configure main tab"""
	mainPage = ttk.Frame(tabs)
	
	button2 = tk.Button(mainPage)
	button2.configure(text = "Nuttelozen knop", command=set_values)
	button2.grid()
	
	"""Add tabs to frame"""
	tabs.add(mainPage, text="    Home    ")
	for i in range(5):
		createPage(i)
		
	tabs.pack(expand=1, fill="both")
	
	#Favicon / map zelf aanpassen aan path
	#root.iconbitmap(r'\Project2.1\Project-2.1\Python Code\favicon.ico')
	
	#Fixedwindow / niet resizable
	root.resizable(width=False, height=False)
	
	"""Run the program"""
	root.mainloop()

if __name__ == "__main__":
	Application()
