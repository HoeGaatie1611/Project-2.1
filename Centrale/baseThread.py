import threading

class Thread (threading.Thread):
		
	def __init__(self, main):
		self.main = main;
		threading.Thread.__init__(self)

	def run(self):
		
		