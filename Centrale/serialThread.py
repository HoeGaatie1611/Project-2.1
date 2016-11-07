import threading
import time
import serial

class SerialThread (threading.Thread):

	ports = [None] * 5;

	def readCommand(self, port):
		length = ord(port.read(1).decode('utf-8')) # Get command length
		return port.read(length).decode('utf-8') # Get entire command with length
		
	def update(self): # Connect, disconnect and process commands
		for i in range(len(self.ports)):
			try:		
				if self.ports[i] == None:
					self.ports[i] = serial.Serial(port="COM" + str(i + 3),baudrate=9600) # Connect to board
					
				else:
					print("COM" + str(i + 3) + ": " + self.readCommand(self.ports[i]))
					
			except: self.ports[i] = None
		
		threading.Timer(1, self.update).start() # Try again in 1 second

	#
		
	def __init__(self, main):
		self.main = main;
		threading.Thread.__init__(self)

	def run(self):
		self.update()
		