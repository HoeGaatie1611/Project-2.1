import threading
import time
import serial

class SerialThread (threading.Thread):

	ports = [None] * 100;

	def readCommand(self, port):
		length = ord(port.read(1).decode('utf-8')) # Get command length
		return port.read(length).decode('utf-8') # Get entire command with length
			
	def update(self): # Connect, disconnect and process commands
		for i in range(len(self.ports)):
			try:	
				if self.ports[i] == None:
					try:
						self.ports[i] = serial.Serial(port="COM" + str(i),baudrate=9600) # Connect to board
					except: continue
					
				else:
					commandString = self.readCommand(self.ports[i]) # Print board and recieved command
					command = commandString.split(" ")[0]
					data = int(commandString.split(" ")[1])
					
					self.main.commandHandler.processCommand(self.ports[i], command, data)

			except: self.ports[i] = None
				
		threading.Timer(1, self.update).start() # Try again in 1 second

	#
	
	def __init__(self, main):
		self.main = main;
		threading.Thread.__init__(self)

	def run(self):
		self.update()
		