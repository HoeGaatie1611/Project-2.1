import threading
import time
from commandHandler import CommandHandler
from configHandler import ConfigHandler
from serialThread import SerialThread
from guiThread import GUIThread

class Main ():
	
	#Initialize all threads, and run the different parts of the program in parallel
	def startThreads(self):
		self.commandHandler = CommandHandler(self)
		self.configHandler = ConfigHandler(self)
		
		self.guiThread = GUIThread(self)
		self.guiThread.start()
		
		time.sleep(1) # Wait for the GUI thread to initialize the GUI
		
		self.serialThread = SerialThread(self)
		self.serialThread.start()
	#
		
	def __init__(self):
		self.startThreads()
		
Main()