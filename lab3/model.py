import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

x = iris.data
y = iris.target
model = LogisticRegression()
model.fit(x, y)

pkl_filename = "pickle_model.pkl" 
with open(pkl_filename, 'wb') as file: 
    pickle.dump(model, file) 

def predict(features):
    with open(pkl_filename, "rb") as f:
        model = pickle.load(f)
    return model.predict([features]).tolist()