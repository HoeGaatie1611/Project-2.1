import threading
import time
import serial

class PortThread (threading.Thread):

	def disconnect(self):
		self.main.serialThread.disconnect(self.id)

	def readCommand(self):
		try:
			length = ord(self.port.read(1).decode('utf-8')) # Get command length
			commandString = self.port.read(length).decode('utf-8') # Get entire command with length
			command = commandString.split(" ")[0]
			data = int(commandString.split(" ")[1])
			
			self.main.commandHandler.processCommand(self, command, data)
			
			self.readCommand()
			
		except:
			self.disconnect() # If could not read command assume disconnect
		
	#
		
	def __init__(self, port, id, main):
		self.port = port
		self.id = id
		self.main = main
		threading.Thread.__init__(self)

	def run(self):
		self.readCommand()
		