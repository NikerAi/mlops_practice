import streamlit as st
from model import predict

st.title("Iris Classifier")

sepal_length = st.number_input("Sepal length (cm)", min_value=0.0, max_value=10.0, value=5.1)
sepal_width = st.number_input("Sepal width (cm)", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input("Petal length (cm)", min_value=0.0, max_value=10.0, value=1.4)
petal_width = st.number_input("Petal width (cm)", min_value=0.0, max_value=10.0, value=0.2)

if st.button("Предсказать"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    prediction = predict(features)[0]
    
    flower_types = {0: "setosa", 1: "versicolor", 2: "virginica"}
    st.success(f"Предсказанный тип: {flower_types[prediction]}")