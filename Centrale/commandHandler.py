
class CommandHandler ():

	def processCommand(self, portThread, command, data):
		print(portThread.port.port + " sent command: '" + command + "' with data: '" + str(data) + "'")
		
	#
		
	def __init__(self, main):
		self.main = main;