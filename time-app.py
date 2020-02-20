#Written by Shang Ke for Data Communications Assignment 1
from flask import Flask
from datetime import datetime
app= Flask(__name__)

@app.route('/')
def wow():
    return 'wow'
@app.route('/time')
def time():
    time_now=datetime.now()
    curr=time_now.strftime("%H:%M:%S")
    return curr
app.run(host='0.0.0.0',port=8080,debug=True)
