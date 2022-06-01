from flask import Flask
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)
from generate_text import generate_text
import pickle
names = ['berdichevsky','berl','biyalik','brenner','frischmann','laufbahn']
@app.route('/<name>') 
def hello_world(name):
    if name in names or name is None:
        model_from_file = open("models/"+name+".pkl", "rb")
        model_from_file = pickle.load(model_from_file)
        return jsonify(generate_text(model_from_file))
    else:
        return "Invalid param!"