from config import DATA_PATH
import json
import os


def save_json(data, filename):
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)
    
    filepath = os.path.join(DATA_PATH, filename)
    
    try:
        json.dump(data, open(filepath, 'w'))
    except Exception as e:
        raise e
