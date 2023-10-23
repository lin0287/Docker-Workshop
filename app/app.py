from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    name = "Thomas Phillips"
    return f"Hello, {name}! - {os.environ['ENV_1']}"
