import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
train_df, test_df = train_test_split(df, train_size=0.8, random_state=42)
train_df.to_csv('train_dataset.csv', index=False)
train_df.to_csv('test_dataset.csv', index=False)

