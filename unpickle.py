import pickle
import glob
from pathlib import Path
import json
files = Path('models/').glob('*')
for file in files:
    name = str(file)[:-5]
    model_from_file = json.loads(open(name+".json", "r",encoding='utf-8').read())
    model_file = open(name+".pkl", "wb")
    pickle.dump(model_from_file, model_file)
    model_file.close()
    # with open(str(file)[:-4]+'.json','w',encoding='utf-8') as outfile:
    #     outfile.write(json.dumps(model_from_file))
    
    