import threading
import time
import serial

class SerialThread (threading.Thread):

	ports = [None] * 5;

	def tryConnect(self):
		for i in range(len(self.ports)):
			try:			
				self.ports[i] = serial.Serial(port="COM" + (i + 3),baudrate=9600)
			except: self.ports[i] = None
		
		time.sleep(1)
		self.tryConnect()

	#
		
	def __init__(self, main):
		self.main = main;
		threading.Thread.__init__(self)

	def run(self):
		self.tryConnect()
		