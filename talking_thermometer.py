#!/usr/bin/python

import sys
import os
from Sensors import LM76
import RPi.GPIO as GPIO
import thread
import re
from time import sleep

def main():
	print "Welcome to Talking Thermometer v1.5"
	lang = 'en'
	TALK_PIN = 19
	LANG_PIN =
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TALK_PIN,GPIO.IN)
	GPIO.setup(LANG_PIN,GPIO.IN)
	sensor = LM76(0x48)
	langList = os.listdir('./lang/support')
	for index in range(len(langList)):
		langList[index]=langList[index][:-4]
	langIndex = 0
	while True:
		lang_inp = GPIO.input(LANG_PIN)
		if (lang_inp==False):
			sleep(0.01)
			lang_inp = GPIO.input(LANG_PIN)
			if (lang_inp==False):
				command = "mplayer -framedrop ./lang/support/" + langList[langIndex] + ".wav >>/dev/null"
                                os.system(command)
				lang = langList[langIndex]
				langIndex = langIndex + 1
				if langIndex >= len(langList):
					langIndex = 0 
                                sleep(0.5)

		input = GPIO.input(TALK_PIN)
		if (input==False):
			sleep(0.01)
			input = GPIO.input(TALK_PIN)
			if (input==False):
				temp = sensor.getTemp()
				print "Temperature : " + `temp`
				int_temp = int(temp)
				if (temp<0):
					 command = "mplayer -framedrop ./lang/"+ lang +"/minus.wav >>/dev/null"
				if ((int_temp+0.5)<(temp-0.25)): 
					filename = "./lang/"+ lang + "/" + `int_temp+1` + ".0.wav"
				elif ((int_temp)>(temp-0.25)):
					filename = "./lang/" + lang + "/" + `int_temp` + ".0.wav"
				else:
					filename = "./lang/"+ lang + "/" + `int_temp` + ".5.wav"
				command = "mplayer -framedrop " + filename + " ./lang/"+ lang +"/degree_celsius.wav >>/dev/null"
				os.system(command)
				sleep(0.5)

main()
