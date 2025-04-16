from sklearn.preprocessing import StandardScaler
import pandas as pd


df = pd.read_csv("train_dataset.csv")

df = df.assign(new_column="test_value")

df.to_csv("train_dataset.csv", index=False)