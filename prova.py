#!/usr/bin/env python

import time
import explorerhat
import wiiboard
import pygame
import time

mac = "8C:56:C5:CB:84:FF"

# explorerhat.motor.forwards()

# time.sleep(3)

# explorerhat.motor.stop()

# explorerhat.motor.one.forwards()
# explorerhat.motor.two.backwards()

def main():
	board = wiiboard.Wiiboard()

	pygame.init()
	
	address = board.discover()
	board.connect(address) #The wii board must be in sync mode at this time

	time.sleep(0.1)
	board.setLight(True)
	done = False

	while (not done):
		time.sleep(0.1)
		for event in pygame.event.get():
			if event.type == wiiboard.WIIBOARD_MASS:
				if (event.mass.totalWeight > 20):   #10KG. otherwise you would get alot of useless small events!
                    			tr = `event.mass.topRight`
                                        br = `event.mass.bottomRight`

                                        if tr > br:
                                                explorerhat.motor.one.backwards()
                                        else:
                                                explorerhat.motor.one.forwards()
                    			tl = `event.mass.topLeft`
                    			bl = `event.mass.bottomLeft`

                    			if tl > bl:
                                                explorerhat.motor.two.backwards()
                                        else:
                                                explorerhat.motor.two.forwards()
                    			
                    			
                    			
                    			
					print("Tr = %s Tl = %s Bl = %s Br = %s"%(tr,tl,bl,br))
                    			
					"""max2 = ""
                    			max1 = ""
                    			if tr >= br:
                        			max1 = "tr"
                    			else:
                        			max1 = "br"
                        			
                    			if tl >= bl:
                        			max2 = "tl"
                    			else:
                        			max2 = "bl"
                                        
                    			if max1=="tr" and max2 == "tl":
                        			explorerhat.motor.forwards()
                    			elif max1=="br" and max2 == "tl":
                        			explorerhat.motor.one.backwards()
                        			explorerhat.motor.two.forwards()
                    			elif max1=="bl" and max2 == "tr":
                        			explorerhat.motor.two.backwards()
                        			explorerhat.motor.one.forwards()
                    			else:
                        			explorerhat.motor.backwards()
				"""	
				else:
					explorerhat.motor.stop()
                    

				#etc for topRight, bottomRight, bottomLeft. buttonPressed and buttonReleased also available but easier to use in seperate event
				
			elif event.type == wiiboard.WIIBOARD_BUTTON_PRESS:
				print "Button pressed!"

			elif event.type == wiiboard.WIIBOARD_BUTTON_RELEASE:
				print "Button released"
				done = True
			
			#Other event types:
			#wiiboard.WIIBOARD_CONNECTED
			#wiiboard.WIIBOARD_DISCONNECTED

	board.disconnect()
	pygame.quit()

#Run the script if executed
if __name__ == "__main__":
	main()
