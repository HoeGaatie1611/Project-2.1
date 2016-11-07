import time
import serial as serial

def tryConnect():
	try:
		ser = serial.Serial('/dev/tty.usbserial', 9600)
	except:
		time.sleep(1000)
		tryConnect()

ser = None
tryConnect()

while True:
	print (ser)