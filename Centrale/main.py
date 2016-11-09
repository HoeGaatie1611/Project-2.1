import threading
import time
from commandHandler import CommandHandler
from configHandler import ConfigHandler
from serialThread import SerialThread
from guiThread import GUIThread

class Main ():
	
	def startThreads(self):
		self.commandHandler = CommandHandler(self)
		self.configHandler = ConfigHandler(self)
		
		self.guiThread = GUIThread(self)
		self.guiThread.start()
		
		time.sleep(0.1) # Wait for gui to boot

		self.serialThread = SerialThread(self)
		self.serialThread.start()
	#
		
	def __init__(self):
		self.startThreads()
		
Main()