import numpy as np
import pickle
import pandas as pd



def predict_class(to_predict):
	"""predicts iris type by user's measurements"""
	# using parameters from original dataset to properly scale new values
	features_means = np.array([5.843, 3.057, 3.758, 1.199])
	features_std = np.array([0.828, 0.435, 1.765, 0.762])
	scaled_values = (to_predict - features_means) / features_std
	row = pd.DataFrame(data=scaled_values.reshape(1, -1), columns=[
		"sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"
	])
	with open("final_task/backend/model/rf_clf.pkl", "rb") as m:
		model = pickle.load(m)

	prediction = model.predict(row)
	flower_types = {0: "setosa", 1: "versicolor", 2: "virginica"}

	return flower_types[prediction[0]]
