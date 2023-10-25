from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    name = "Zhi Lin"
    return f"Hello, {name}!, 'NO FAN' - {os.environ['ENV_1']}, {os.environ['ENV_2']}, {os.environ['ENV_3']}"