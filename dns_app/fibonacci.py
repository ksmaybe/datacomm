#Written by Shang Ke for Data Communications Assignment 4

from flask import Flask,request,json
from flask_api import status
import socket,requests


app= Flask(__name__)

@app.route('/register',methods=['PUT'])
def reg():
    body=request.json
    hostname=body["hostname"]
    ip=body["ip"]
    as_ip=body["as_ip"]
    as_port=body["as_port"]
    print("json",body)
    #send UDP
    MESSAGE="TYPE=A\n" \
            "NAME="+hostname+"\n" \
            "VALUE="+ip+"\n" \
            "TTL=10"
    print(MESSAGE)
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(("",9091))
    sock.sendto(MESSAGE.encode(),(as_ip,int(as_port)))
    print("sent")
    data,addr=sock.recvfrom(1024)
    sock.close()
    return data.decode('utf-8'),status.HTTP_201_CREATED

@app.route('/fibonacci',methods=['GET'])
def fib():
    if request.args.get('number').isdigit():
        return str(fibonacci(int(request.args.get('number')))),status.HTTP_200_OK
    else:
        return "not integer",status.HTTP_400_BAD_REQUEST


def fibonacci(x):
    if x==1 or x==2:return 1
    x1=x2=1
    while x>2:
        x1,x2=x2,x1+x2
        x-=1
    return x2

app.run(host='0.0.0.0',port=9090,debug=True)