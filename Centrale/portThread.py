import threading
import time
import serial

class PortThread (threading.Thread):

	def isInt(self, s):
		try:
			int(s)
			return True
		except ValueError:
			return False

	def disconnect(self):
		##print(self.port.port + " disconnected")
		self.main.serialThread.disconnect(self.id)
		self.main.guiThread.removePage(self.id)

	def readCommand(self):
		try:
			length = ord(self.port.read(1).decode('utf-8')) # Get command length
			commandString = self.port.read(length).decode('utf-8') # Get entire command with length
			if self.isInt(commandString.split(" ")[1]):
				command = commandString.split(" ")[0]
				data = int(commandString.split(" ")[1])

				self.main.commandHandler.processCommand(self, command, data)

			threading.Timer(0.01, self.readCommand).start() # Recursive
			return

		except:
			self.disconnect() # If could not read command assume disconnect
			self.main.guiThread.amountSensors()
			self.main.guiThread.setGraphOff()

	def sendCommand(self, command, data):
		commandString = command + " " + str(data)

		self.port.write(commandString.encode())
	#

	def __init__(self, port, id, main):
		self.port = port
		self.id = id
		self.main = main
		threading.Thread.__init__(self)

	def run(self):
		##print(self.port.port + " connected")
		self.main.guiThread.createPage(self.id)
		self.readCommand()
