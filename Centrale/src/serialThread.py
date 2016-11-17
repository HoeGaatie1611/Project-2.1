import threading
import time
import serial
from portThread import PortThread

class SerialThread (threading.Thread):

	ports = [None] * 20;

	#Check for new connected modules
	def update(self):
		for id in range(len(self.ports)):
			if self.ports[id] == None:
				try:
					portThread = PortThread(serial.Serial(port="COM" + str(id), baudrate=9600), id, self.main) #Connect to module through serial
					portThread.start() #Start reading commands
					self.ports[id] = portThread
				except: continue

		threading.Timer(1, self.update).start() #Try again in 1 second

	#Remove serial connection instance
	def disconnect(self, id):
		self.ports[id] = None

	def __init__(self, main):
		self.main = main
		threading.Thread.__init__(self)

	def run(self):
		self.update()
