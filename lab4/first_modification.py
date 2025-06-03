import pandas as pd


df = pd.read_csv("titanic.csv")
df.drop(["embarked", "embark_town"], axis=1, inplace=True)
df.to_csv("titanic.csv", index=False)