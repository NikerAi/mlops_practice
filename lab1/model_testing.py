import pandas as pd
import pickle

test = pd.read_csv('test_dataset_str.csv')
test_x = test.drop(columns=['target'])
test_y = test['target']

pkl_filename = "pickle_model.pkl" 
with open(pkl_filename, 'rb') as file: 
    pickle_model = pickle.load(file) 
    
score = pickle_model.score(test_x, test_y)
print("Model accuracy score is: ", score)
