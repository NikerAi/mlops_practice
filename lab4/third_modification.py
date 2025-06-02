import pandas as pd
from sklearn.preprocessing import OneHotEncoder


df = pd.read_csv("titanic.csv")

ohe = OneHotEncoder(drop="first", sparse_output=False).set_output(transform="pandas")

ohe_sex_class = ohe.fit_transform(df[["sex", "class"]])
df.drop(["sex", "class"], axis=1, inplace=True)
df = df.join(ohe_sex_class, how="inner")

df.to_csv("titanic.csv", index=False)