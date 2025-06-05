from sklearn.datasets import load_iris
import pandas as pd
import numpy as np


def load_data():
	"""Load iris dataset"""
	iris = load_iris()
	df = pd.DataFrame(
		data=np.c_[iris["data"], iris["target"]],
		columns=iris["feature_names"] + ["target"])

	df["target"] = df["target"].astype("int8")
	df["target_names"] = df["target"].map(lambda x: iris["target_names"][x])
	df.to_csv("data/origin_iris_dataset.csv", index=False)
	return df


if __name__ == '__main__':
	load_data()
