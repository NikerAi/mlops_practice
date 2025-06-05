import pandas as pd
from sklearn.preprocessing import StandardScaler


def scale_data(path):
	"""Apply StandardScaler to dataframe features"""
	df = pd.read_csv(path)
	std_scaler = StandardScaler().set_output(transform="pandas")
	to_scale = df.iloc[:, :4]

	df[to_scale.columns] = std_scaler.fit_transform(to_scale)
	df.to_csv("data/iris_dataset.csv", index=False)


if __name__ == '__main__':
	scale_data("data/origin_iris_dataset.csv")