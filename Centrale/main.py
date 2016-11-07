import threading
from serialThread import SerialThread
from guiThread import GUIThread

class Main ():

	def startThreads(self):
		self.serialThread = SerialThread(self)
		self.serialThread.start()
	
		self.guiThread = GUIThread(self)
		self.guiThread.start()
	
	#
		
	def __init__(self):
		self.startThreads()
		
Main()