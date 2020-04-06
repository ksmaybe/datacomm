#Written by Shang Ke for Data Communications Assignment 4

from flask import Flask,request,json
from flask_api import status
import socket
import pickle





print("Starting")
with open('my_dict.txt', "rb") as f:
    DNS_DICT=pickle.load(f)
UDP_PORT=53533
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("",UDP_PORT))
while True:
    data,c=sock.recvfrom(1024)
    msg=data.decode("utf-8").split("\n")
    print(msg)
    if len(msg)==4:
        TYPE=msg[0].split('=')[1]
        NAME=msg[1].split('=')[1]
        VALUE=msg[2].split('=')[1]
        TTL=msg[3].split('=')[1]
        d={"value":VALUE,"name":NAME,"ttl":TTL}
        DNS_DICT[NAME]=d
        print(d)
        with open('my_dict.txt', 'wb') as f:
            pickle.dump(DNS_DICT,f)
        sock.sendto("success".encode(),c)
    elif len(msg)==2:
        TYPE=msg[0].split('=')[1]
        NAME=msg[1].split('=')[1]
        d=DNS_DICT[NAME]
        MESSAGE="TYPE=A\n" \
                "NAME="+NAME+"\n" \
                "VALUE="+d["value"]+'\n' \
                "TTL="+d["ttl"]
        print(2,MESSAGE)
        sock.sendto(MESSAGE.encode(),c)
