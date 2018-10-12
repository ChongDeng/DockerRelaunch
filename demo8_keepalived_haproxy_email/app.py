from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    HostName = socket.gethostname() 
    HostIP = socket.gethostbyname(HostName)
    return "Hello! My Hostname is" + HostName + ". My IP is " + HostIP


if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug = True)
    app.run(host='0.0.0.0', port = 80)


