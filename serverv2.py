#!/usr/bin/env python
import socket
import time
import explorerhat
import wiiboard
import pygame
import time

#server = socket.socket()
#server.bind(('127.0.0.1',1340))
#server.listen(1)
#client, indirizzo = server.accept()

def media(sl):
	mtl= float(0)
	mtr= float(0)
	mbr= float(0)
	mbl= float(0)
	for col in range(0,4):
		for row in range(0,len(sl)):
			if col == 0:
				mtl = mtl+float(sl[row][col])
			if col == 1:
				mtr = mtr+float(sl[row][col])
			if col == 2:
				mbr = mbr+float(sl[row][col])
			if col == 3:
				mbl = mbl+float(sl[row][col])
	if not (len(sl) == 0):
		mtl= mtl/len(sl)
		mtr= mtr/len(sl)
		mbr= mbr/len(sl)
		mbl= mbl/len(sl)
	
	return [mtl,mtr,mbr,mbl]
def avanti():
	#client.send("av".encode())
	explorerhat.motor.forwards()
def indietro():
	#client.send("in".encode())
	explorerhat.motor.backwards()
def destra():
	#client.send("dx".encode())
	explorerhat.motor.one.forwards(10)
	explorerhat.motor.two.forwards(100)
def sinistra():
	#client.send("sx".encode())

	explorerhat.motor.one.forwards(100)
	explorerhat.motor.two.forwards(10)
def tuttodestra():
	#client.send("dxdx".encode())
	explorerhat.motor.two.forwards()
	explorerhat.motor.one.backwards()
def tuttosinistra():
	#client.send("sxsx".encode())
	explorerhat.motor.one.forwards()
	explorerhat.motor.two.backwards()
def stop():
	#client.send("stop".encode())
	explorerhat.motor.stop()

def main():
	board = wiiboard.Wiiboard()
	pygame.init()
	address = board.discover()
	board.connect(address) #The wii board must be in sync mode at this time
	time.sleep(0.5)
	board.setLight(True)
	done = False
	mediante=[]
	risultato = list()
	while (not done):
		for event in pygame.event.get():
			if event.type == wiiboard.WIIBOARD_MASS:
				preso = True
				l = list()
				l.append(`event.mass.topRight`)
				l.append(`event.mass.bottomRight`)	
				l.append(`event.mass.topLeft`)
				l.append(`event.mass.bottomLeft`)
				print(l)
				mediante.append(l)
				#etc for topRight, bottomRight, bottomLeft. buttonPressed and buttonReleased also available but easier to use in seperate event
				
			elif event.type == wiiboard.WIIBOARD_BUTTON_PRESS:
				print "Button pressed!"

			elif event.type == wiiboard.WIIBOARD_BUTTON_RELEASE:
				print "Button released"
				done = True
			
			#Other event types:
			#wiiboard.WIIBOARD_CONNECTED
			#wiiboard.WIIBOARD_DISCONNECTED
		risultato = media(mediante) # [14.000000,24.000000,30.00000,0]
		mediante = list()
		tot = 0
		max1 = 0
		max2 = 0
		grejo = risultato[:]

		for i in risultato :
			tot = tot+i
		if tot > 20:
			grejo.sort()
			max1 = grejo[3]

			max2 = grejo[2]

			max1t = False
			max2t = False
			print(max1)
			print(max2)
			for i in range(0,4):
				if risultato[i] == max1 and not max1t:
					max1 = i
					max1t = True
				elif risultato[i] == max2 and not max2t:
					max2 = i
					max2t = True
			#[mtl,mtr,mbr,mbl]
			print(max1,max2)
			m = 0
			for i in risultato:
				m = m+i
			m = m/4
			print m

			s=""
			
			if (risultato[0]-m < 5) and (risultato[1]-m < 5) and (risultato[2]-m < 5) and (risultato[3]-m < 5):
				stop()
			else:
				if (max1 == 0 and max2 == 2) or (max1 == 2 and  max2 == 0):
					avanti()
				elif(max1 == 0 and max2 == 3) or (max1 == 3 and max2 == 0):
					tuttodestra()
				elif(max1 == 1 and max2 == 3) or (max1 == 3 and max2 == 1):
					indietro()
				elif(max1 == 1 and max2 == 2) or (max1 == 2 and max2 == 1):
					tuttosinistra()
				elif(max1 == 2 and max2 == 3) or(max1 == 3 and max2 == 2) :
					destra()
				elif(max1 == 1 and max2 == 0) or (max1 == 0 and max2 == 1):
					sinistra()
			preso = False
		elif preso:
			stop()
	
	board.disconnect()
	pygame.quit()




if __name__ == "__main__":
	main()
	client.close()
