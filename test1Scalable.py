#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import threading
import math

SDI   = 26#or 26 red 21 green
RCLK  = 20
SRCLK = 16
sleepInOut=0.5

x = 4 #Largeur de l'ecran
y = 4 #hauteur de l'ecran
nbMotif=2 #nombre de motif affichable

#motifV=[[[0]*x]*y]*nbMotif
motifV = [[[0 for i in range(x)] for j in range(y)]for z in range(nbMotif)] 
motif = [[[0 for i in range(x)] for j in range(y)]for z in range(nbMotif)] 
#motif=[[0]*8]*10 #dans les 10 elements de la premiere dimension sont toutes les shiftregister a afficher. L'autre dimension sert a afficher different motif

def nbShiftCalculate(x,y):
	nbShift=int(math.ceil(x*y/8.0))
	print("nbShift"+str(nbShift))
	return nbShift
nbShift=nbShiftCalculate(x,y)
def convertToHexa(motifV,x1,y1,nbMotif1):
	global x
	global y
	global nbMotif
	global nbShift
	x=x1
	y=y1
	nbMotif=nbMotif1
	nbShift=nbShiftCalculate(x,y)
	global motif
	motif=[[0 for i in range(nbShift)] for j in range(nbMotif)]
	shiftNumber=0
	shiftCpt=0 #max 8 car un shift ne peux pas aller plus loin
	for motifCpt in range(0,nbMotif):
			shiftNumber=0
			shiftCpt=0
			for absc in range(0,x):
					for ordo in range(0,y):
							if(shiftCpt>7):
									shiftCpt=0
									shiftNumber=shiftNumber+1
							valeur=motifV[motifCpt][absc][ordo]<<shiftCpt
							print(str(motifCpt)+","+str(shiftNumber))
							motif[motifCpt][shiftNumber]=motif[motifCpt][shiftNumber] | valeur
							shiftCpt=shiftCpt+1
	for testaff1 in range(0,nbMotif):
			valeuraff=""
			for testaff in range(0,nbShift):
					valeuraff=valeuraff+","+str(motif[testaff1][testaff])
			print(valeuraff)

	#exemple de resultat
	#motif[0]=[0xff,0xff] #8bit pour toutes les infos du shift

	#motif[0][2]=0xf0
	#motif[0][3]=0xf0
	#
	#motif[1]=[0x00,0x00]
	#motif[2]=[0xf0,0xf0]
	#motif[3]=[0x0f,0x0f]

	#motif[1][2]=0x00
	#motif[1][3]=0x00
	return motif
convertToHexa(motifV,x,y,nbMotif)
#DataOutPut=[26,27,28,29,30,31,32,33,34,35]#liste des pin de data

DataOutPut=[26,21]#liste des pin de data


#===============   LED Mode Defne ================
#	You can define yourself, in binay, and convert it to Hex 
#	8 bits a group, 0 means off, 1 means on
#	like : 0101 0101, means LED1, 3, 5, 7 are on.(from left to right)
#	and convert to 0x55.

#LED0 = [0x55,0x00,0xff,0x55,0xff,0x00,0xff,0x00]	#original mode
#LED1 = [0x01,0x03,0x07,0x0f,0x1f,0x3f,0x7f,0xff]	#blink mode 1
#LED2 = [0x01,0x05,0x15,0x55,0xb5,0xf5,0xfb,0xff]	#blink mode 2
#LED3 = [0x02,0x03,0x0b,0x0f,0x2f,0x3f,0xbf,0xff]	#blink mode 3
#=================================================
LED0 = [0x00,0xff]
#LED0 = [0x00,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]	#Working chenillard
#LED0 =  [0x00, 0x01]	

#LED0 = [0x01,0x12,0x23,0x34,0x45,0x56,0x67,0x78,0x80]	#original mode
#LED0 = [0x00,0xff]
#LED0 = [0xff,0x00]	#original mode
def print_msg():
	print('Program is running...')
	print('Please press Ctrl+C to end the program...')

def setup():
	GPIO.setmode(GPIO.BCM)    # Number GPIOs by its physical location
	#GPIO.setup(SDI, GPIO.OUT)
	for pinSortie in range(0,len(DataOutPut)):
		GPIO.setup(DataOutPut[pinSortie], GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
	
	GPIO.output(SDI, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)

def hc595_in(dat):
	for bit in range(0, 8):	
		GPIO.output(SDI, 0x80 & (dat << bit))
		GPIO.output(SRCLK, GPIO.LOW)
		time.sleep(0.01)
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.01)
def hc595_inCustom(idMotif):
	for bit in range(0,8):
		for line in range(0,nbShift):
			#print("line",line)
			#print("idmotif",idMotif)
			#print(motif)
			#print(motif[idMotif][line])
			#GPIO.output(26, 0x80 & (1 << bit))
			#GPIO.output(21, 0x80 & (1 << bit))
			GPIO.output(DataOutPut[line], 0x80 & (motif[idMotif][line] << bit))
		GPIO.output(SRCLK, GPIO.LOW)
		time.sleep(0.01)
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.01)
def hc595_out():
	GPIO.output(RCLK, GPIO.LOW)
	time.sleep(0.01)
	#time.sleep(sleepInOut)
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.01)

def loop():
	WhichLeds = LED0	# Change Mode, modes from LED0 to LED3
	sleeptime = 0.5		# Change speed, lower value, faster speed
	i = 0
	def theLoop():
		i=1
	#while True:
		#value = WhichLeds[i%len(WhichLeds)]
		# hc595_in(value)
		hc595_inCustom(i%nbMotif)
		hc595_out()
		#print 'update : ' + str(value)
		print('Update mystere')
		i += 1
		#time.sleep(sleeptime)
		threading.Timer(sleeptime,theLoop).start()
	theLoop()
	#	for i in range(len(WhichLeds)-1, -1, -1):
	#		hc595_in(WhichLeds[i])
	#		hc595_out()
	#		time.sleep(sleeptime)

def destroy():   # When program ending, the function is executed.
	for pinSortie in range(0,len(DataOutPut)):
		GPIO.output(DataOutPut[pinSortie], GPIO.LOW)
	GPIO.output(SDI, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)
	GPIO.cleanup()
	raise SystemExit
def mainFunction():
	GPIO.cleanup()
	print_msg()
	setup()
	loop()

