import pandas as pd
from sklearn.preprocessing import StandardScaler

def preposor(name_file):
    df = pd.read_csv(name_file + '.csv')
    std = StandardScaler()
    df_std =  pd.DataFrame(data=std.fit_transform(df.drop(columns=['target'])), columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
    df_std = pd.concat([df_std, df['target']], axis = 1)
    df_std.to_csv(name_file + '_str.csv', index=False)

    
df_train = pd.read_csv('train_dataset.csv')
df_test = pd.read_csv('test_dataset.csv')
std = StandardScaler()
df_std =  pd.DataFrame(data=std.fit_transform(df_train.drop(columns=['target'])), columns=['sepal length (cm)', 'sepal width (cm)', 'petallength (cm)', 'petal width (cm)'])
df_std = pd.concat([df_std, df_train['target']], axis = 1)
df_std.to_csv('test_dataset_std.csv', index=False)

preposor('train_dataset')
preposor('test_dataset')