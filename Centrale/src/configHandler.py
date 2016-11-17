import json

class ConfigHandler ():

	def set(self, key, value):
		config = {}
		with open('src/config.json', 'r') as f:
			config = json.load(f)

		config[key] = value

		with open('src/config.json', 'w') as f:
			json.dump(config, f)
		
	def get(self, key):
		try:
			config = {}
			with open('src/config.json', 'r') as f:
				config = json.load(f)

			return config[key]
			
		except: return None
	
	def __init__(self, main):
		self.main = main;