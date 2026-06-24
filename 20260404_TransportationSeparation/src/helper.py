import pickle
import json

def write_pickle(filepath, object):
    with open(filepath, 'wb') as fp:
        pickle.dump(object, fp)


def read_pickle(filepath):
    with open(filepath, 'rb') as f:  # notice the r instead of w
        pickled_object = pickle.load(f)
    return pickled_object

def write_json(filepath, object):
    with open(filepath, "w") as f:
        json.dump(object, f)

def read_json(filepath):
    with open(filepath, "r") as f:
        json_file = json.load(f)
    return json_file