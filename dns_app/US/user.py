#Written by Shang Ke for Data Communications Assignment 4

from flask import Flask,request,json
from flask_api import status
import socket
import requests

app= Flask(__name__)

@app.route('/fibonacci',methods=['GET'])
def user():
    if request.method=='GET':
        hostname=request.args.get('hostname')
        fs_port=request.args.get('fs_port')
        number=request.args.get('number')
        as_ip=request.args.get('as_ip')
        as_port=request.args.get('as_port')
        all=True
        print(request.args)
        badparameter=[]
        if hostname is None:
            badparameter.append('hostname')
            all=False
        if fs_port is None:
            badparameter.append('fs_port')
            all=False
        if number is None:
            badparameter.append('number')
            all=False
        if as_ip is None:
            badparameter.append('as_ip')
            all=False
        if as_port is None:
            badparameter.append('as_port')
            all=False
        if not all:
            return "Missing parameter: "+str(badparameter),status.HTTP_400_BAD_REQUEST

        MESSAGE="TYPE=A\n" \
                "NAME=fibonacci.com"
        print(MESSAGE)
        sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.bind(("",8081))
        sock.sendto(MESSAGE.encode(),(as_ip,int(as_port)))
        while True:
            data,addr=sock.recvfrom(1024)
            msg=data.decode("utf-8").split("\n")
            TYPE=msg[0].split('=')[1]
            NAME=msg[1].split('=')[1]
            VALUE=msg[2].split('=')[1]
            TTL=msg[3].split('=')[1]

            return requests.get("http://"+VALUE+":"+fs_port+"/fibonacci?number="+number).content,status.HTTP_200_OK
app.run(host='0.0.0.0',port=8080,debug=True)