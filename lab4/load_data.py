import seaborn as sns

df = sns.load_dataset("titanic")

df.to_csv("titanic.csv", index=False)