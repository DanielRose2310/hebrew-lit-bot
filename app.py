from flask import Flask
app = Flask(__name__)
from generate_text import generate_text
import pickle
names = ['berdichevsky','berl','biyalik','brenner','frischmann','laufbahn']
@app.route('/<name>') 
def hello_world(name):
    if name in names:
        model_from_file = open("models/"+name+".pkl", "rb")
        model_from_file = pickle.load(model_from_file)
        return generate_text(model_from_file)
    else:
        return "Invalid param!"