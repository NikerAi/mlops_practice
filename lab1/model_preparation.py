import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

train = pd.read_csv('train_dataset_str.csv')
train_x = train.drop(columns=['target'])
train_y = train['target']
model = LogisticRegression()
model.fit(train_x, train_y)
pkl_filename = "pickle_model.pkl" 
with open(pkl_filename, 'wb') as file: 
    pickle.dump(model, file) 