import threading
import time
import serial

class PortThread (threading.Thread):

	#Function to verify a value to be an integer
	def isInt(self, s):
		try:
			int(s)
			return True
		except ValueError:
			return False

	#Disconnect the module from the system, and update the GUI
	def disconnect(self):
		self.main.serialThread.disconnect(self.id)
		self.main.guiThread.removePage(self.id)
		self.main.guiThread.updateModuleAmount()
			
	#Wait for a command to be recieved
	def readCommand(self):
		try:
			length = ord(self.port.read(1).decode('utf-8')) #Get command length
			commandString = self.port.read(length).decode('utf-8') #Get entire command with recieved length
			if self.isInt(commandString.split(" ")[1]): #Verify command integrity
				command = commandString.split(" ")[0] #Determine command name
				data = int(commandString.split(" ")[1]) #Determine integer value for use in command processing

				self.main.commandHandler.processCommand(self, command, data) #Process the command

			threading.Timer(0.01, self.readCommand).start() #Recursively await another command
			return

		except:
			self.disconnect() #If could not read command assume disconnect

	#Send command to the module
	def sendCommand(self, command, data):
		commandString = command + " " + str(data)

		self.port.write(commandString.encode())

	def __init__(self, port, id, main):
		self.port = port
		self.id = id
		self.main = main
		threading.Thread.__init__(self)

	#Behaviour on module being connected
	def run(self):
		self.main.guiThread.createPage(self.id)
		self.main.guiThread.updateModuleAmount()
		self.readCommand()
