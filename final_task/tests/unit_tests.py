from final_task.backend.load_data import load_data
from final_task.backend.data_preprocessing import scale_data
from final_task.backend.model_training import train_model
import os
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score


def test_load_data():
	"""Check if origin data is being created"""
	test_path = "final_task/backend/data/test_origin_data.csv"
	load_data(test_path)
	df = pd.read_csv(test_path)

	assert df.shape[0] > 0
	assert df.shape[1] > 0

	os.remove(test_path)


def test_data_prep():
	"""Check if data preprocessing works as expected"""
	load_path = "final_task/backend/data/origin_iris_dataset.csv"
	save_path = "final_task/backend/data/test_iris_data.csv"
	scale_data(load_path, save_path)
	df = pd.read_csv(save_path)

	# test if mean == 0 and std 1, if true scaling was correct
	assert round(df.iloc[:, 1].mean()) == 0
	assert round(df.iloc[:, 1].std()) == 1
	os.remove(save_path)


def test_train_model():
	"""Check if fitted model was added to backend/model folder"""
	load_path = "final_task/backend/data/iris_dataset.csv"
	save_path = "final_task/backend/model/test_model.pkl"
	train_model(load_path, save_path)

	assert "test_model.pkl" in os.listdir("final_task/backend/model")
	os.remove(save_path)


def test_model_performance():
	"""check if data quality is acceptable or model needs to be refitted
		30% of dataset is chosen at random and model tested
	"""
	with open("final_task/backend/model/rf_clf.pkl", "rb") as m:
		rf_clf = pickle.load(m)

	df = pd.read_csv("final_task/backend/data/iris_dataset.csv").sample(frac=0.3)
	X = df.iloc[:, :4]
	y = df["target"]

	score = accuracy_score(y, rf_clf.predict(X))
	assert score >= 0.9


