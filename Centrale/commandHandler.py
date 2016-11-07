
class CommandHandler ():

	def processCommand(self, port, command, data):
		print(port.port + " sent command: '" + command + "' with data: '" + str(data) + "'")
		
	#
		
	def __init__(self, main):
		self.main = main;