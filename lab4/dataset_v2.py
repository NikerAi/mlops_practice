from sklearn.preprocessing import StandardScaler
import pandas as pd


df = pd.read_csv("train_dataset.csv")

scaler = StandardScaler()
df.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])

df.to_csv("train_dataset.csv", index=False)
