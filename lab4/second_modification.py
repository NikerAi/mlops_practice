from sklearn.impute import SimpleImputer
import pandas as pd

df = pd.read_csv("titanic.csv")

med_imp = SimpleImputer(strategy="median")
num_cols = df.select_dtypes("number").columns

df[num_cols] = med_imp.fit_transform(df[num_cols])
df.to_csv("titanic.csv", index=False)