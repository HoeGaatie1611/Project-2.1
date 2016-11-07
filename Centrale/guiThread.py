import threading
import time

class GUIThread (threading.Thread):
		
	def printPorts(self):
		print(self.main.serialThread.ports)
		
		time.sleep(1)
		self.printPorts()

	#
		
	def __init__(self, main):
		self.main = main;
		
		threading.Thread.__init__(self)

	def run(self):
		self.printPorts()
		