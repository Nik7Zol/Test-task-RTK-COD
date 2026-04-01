from flask import Flask
import socket

app = Flask(__name__)

hostname = socket.gethostname()
if hostname == "backend1":
    content = "Бэкенд 1"
elif hostname == "backend2":
    content = "Бэкенд 2"
else:
    content = "Неизвестный бэкенд"

@app.route('/')
def hello():
    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
