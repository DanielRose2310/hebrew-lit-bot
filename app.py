from flask import Flask
from flask_cors import CORS, cross_origin
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
        return jsonify({name:generate_text(model_from_file)})
    else:
        return "Invalid param!"
    
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)