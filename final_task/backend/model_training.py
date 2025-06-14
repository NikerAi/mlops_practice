import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle


def train_model(load_path, save_path):
	"""Train model and save"""
	df = pd.read_csv(load_path)

	rf_clf = RandomForestClassifier()
	X_train, X_test, y_train, y_test = train_test_split(
		df.iloc[:, :4],
		df["target"],
		test_size=0.2,
		random_state=5,
		shuffle=True
	)
	rf_clf.fit(X_train, y_train)

	with open(save_path, "wb") as f:
		pickle.dump(rf_clf, f)


if __name__ == '__main__':
	train_model("data/iris_dataset.csv", "model/rf_clf.pkl")




