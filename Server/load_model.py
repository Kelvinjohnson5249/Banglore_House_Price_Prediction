import json
import pickle
import numpy as np
import os

Model_path = os.path.join("Model", "banglore_home_prices_model.pickle")
columns_path = os.path.join("Model", "columns.json")

__model = None
__data_columns = []
__locations = []


def load_artifacts():
    global __model
    global __data_columns
    global __locations

    with open(columns_path, 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    with open(Model_path, 'rb') as f:
        __model = pickle.load(f)

    

def get_locations():
    return __locations

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)