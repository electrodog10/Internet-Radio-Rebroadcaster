#!usr/bin/python2
#Created by Harrison Gieselman and Lewis Callaway

from time import sleep
from Adafruit_Si4713 import Adafruit_Si4713

FMSTATION = 10230  
TRANSMITPOWER = 115

radio = Adafruit_Si4731
	
	
if not radio.begin():
	print "error! couldn't begin!"

else:
	radio.setTXpower(POWER)

	radio.tuneFM(FMSTATION)


	radio.beginRDS()
	radio.setRDSbuffer(“makezine.com”)


	while True:

		radio.setRDSstation("Make")
		sleep(10)


		radio.setRDSstation("Internet")
		sleep(5)


		radio.setRDSstation("Radio")
		sleep(5)

		radio.setRDSstation("Stream")
		sleep(5)


