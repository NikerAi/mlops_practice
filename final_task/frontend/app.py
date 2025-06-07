import streamlit as st
from final_task.backend.make_prediction import predict_class


# set title
st.title("Iris Classifier")
# show explanatory image
st.image("final_task/frontend/iris.png")

# input
sepal_length = st.number_input("Sepal length (cm)", min_value=4.0, max_value=8.0, value=5.8, key="sl")
sepal_width = st.number_input("Sepal width (cm)", min_value=2.0, max_value=4.5, value=3.0, key="sw")
petal_length = st.number_input("Petal length (cm)", min_value=1.0, max_value=6.9, value=3.7, key="pl")
petal_width = st.number_input("Petal width (cm)", min_value=0.1, max_value=2.5, value=1.2, key="pw")

# show result
if st.button("Предсказать"):
	features = [sepal_length, sepal_width, petal_length, petal_width]
	prediction = predict_class(features)

	st.success(f"Предсказанный тип: {prediction}")