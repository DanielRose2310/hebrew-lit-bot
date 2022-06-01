from flask import Flask
app = Flask(__name__)
from generate_text import generate_text
import json
import pickle

@app.route('/<name>') 
def hello_world(name):
    model_from_file = open("models/"+name+".pkl", "rb")
    model_from_file = pickle.load(model_from_file)
    return generate_text(model_from_file)
