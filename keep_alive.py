from flask import Flask
from threading import Thread

app = Flask("")


def run():
    
    app.run()


def keep_alive():
    t = Thread(target=run)
    t.start()
