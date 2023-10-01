import json

from flask import Flask, request, Response

from src.utils import CustomResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return CustomResponse({"message": "Hello, World!"})