# -*- coding: utf-8 -*-
"""

@author: ..::/^\RAD!N/^\::..

Spyder Editor

"""
 
import os
import sys
import _thread
import socket
from time import sleep
transmit_port = 12000
recieve_port = 12500
ts = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ts.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
cnt=5
notFound=True
 
def reciever_init():
    global notFound
    rs=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rs.bind(('',recieve_port))
    print("Start Listening . . .")
    key=rs.recv(1024)    
    key=key.decode(encoding='UTF-8',errors='strict')
    if (key=='ok'):
        print("I see the Light")
        notFound = False
 
def make_msg():
    my_ip = get_lan_ip()
    #print(my_ip)
    message = "Raspberry pi3," + my_ip
    return message
    
if os.name != "nt":
    import fcntl
    import struct
    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', bytes(ifname[:15], 'utf-8'))
                # Python 2.7: remove the second argument for the bytes call
            )[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break;
            except IOError:
                pass
    return ip
 

if __name__=="__main__":
    sleep(30)
    _thread.start_new_thread( reciever_init, () )
    while notFound:
        if (cnt == 5): 
            msg = make_msg()
            cnt = 0
        ts.sendto(bytes(msg, 'utf-8'),('255.255.255.255',transmit_port))
        print(msg," packet sent")
        cnt += 1
        sleep(3)
    sys.exit
