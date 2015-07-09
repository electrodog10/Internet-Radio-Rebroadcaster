
#!usr/bin/python2
#Created by Harrison Gieselman and Lewis Callaway
# -*- coding: utf-8 -*-

from time import sleep
from Adafruit_Si4713 import Adafruit_Si4713

FMSTATION = 10230
TRANSMITPOWER = 115

radio = Adafruit_Si4713()

radio.begin()


radio.setTXpower(TRANSMITPOWER)
radio.tuneFM(FMSTATION)

radio.beginRDS()

radio.setRDSstation("Make")
sleep(6)


radio.setRDSstation("Internet")
sleep(6)


radio.setRDSstation("Radio")
sleep(6)

radio.setRDSstation("Stream")
sleep(6)

