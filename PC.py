# -*- coding: utf-8 -*-
"""

@author: ..::/^\RAD!N/^\::..

Spyder Editor

"""

import socket
transmit_port = 12500
recieve_port = 12000
rs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ts = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rs.bind(('',recieve_port))
while True:
    print("Listening started . . .")
    beacon = rs.recvfrom(1024)
    print(beacon[0].decode(encoding='UTF-8',errors='strict'), "sent from:", beacon[1][0], "on port number", beacon[1][1])
    ans = input("should we send acknowledge ?(y/n)")
    if(ans is 'y'):    
        ts.sendto(bytes('ok', 'utf-8'),(beacon[1][0],transmit_port))
        print("Sent!")
        break