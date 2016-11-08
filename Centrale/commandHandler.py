
class CommandHandler ():

	def processCommand(self, portThread, command, data):
		print(portThread.port.port + " sent command: '" + command + "' with data: '" + str(data) + "'")
		
		if(command == "baseTemperature"):
			self.main.guiThread.setPageType(portThread, "temperature")
		
		elif(command == "baseRemand"):
			self.main.guiThread.setPageType(portThread, "remand")
		
	#
		
	def __init__(self, main):
		self.main = main;