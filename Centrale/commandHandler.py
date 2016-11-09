
class CommandHandler ():

	def processCommand(self, portThread, command, data):
		page = self.main.guiThread.pages[portThread.id]
		
		self.main.guiThread.addText(page.text, command + " " + str(data))
		#print(portThread.port.port + " sent command: '" + command + "' with data: '" + str(data) + "'")
		
		if(command == "baseTemperature"):
			self.main.guiThread.setPageType(portThread, "temperature")
			page.baseVal.set(data)
			
		elif(command == "baseRemand"):
			self.main.guiThread.setPageType(portThread, "remand")
			page.baseVal.set(data)
			
		elif(command == "rollStatus"):
			if(data == 0):
				page.rollStatus.set("Bezig")
			elif(data == 1):
				page.rollStatus.set("Ingerold")
			elif(data == 2):
				page.rollStatus.set("Uitgerold")
				
		elif(command == "autonoomPressed"):
			if(data == 0 and page.autonoom == 1):
				self.main.guiThread.removeRollInput(page)
				self.main.guiThread.addBaseInput(page)
			elif(data == 1 and page.autonoom == 0):
				self.main.guiThread.addRollInput(page)
				self.main.guiThread.removeBaseInput(page)
				
			page.autonoom = data
			
		elif(command == "maxRoll"):
			page.maxRoll.set(data)
			
	#
		
	def __init__(self, main):
		self.main = main;