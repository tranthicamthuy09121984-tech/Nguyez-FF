from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "Bot Nguyez FF MP40 Mang Xa - M1887 Vu Tru is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()