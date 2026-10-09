import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Diabetes Progression Prediction",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Diabetes Progression Prediction (Unscaled Regression Model)")
st.write(
    "Enter the patient's clinical information beside to predict "
    "the diabetes progression score."
)

with st.sidebar:

    st.header("Patient Information")

    age = st.slider(
        "Age",
        min_value=19,
        max_value=80,
        value=50
    )

    sex_choice = st.selectbox(
        "Sex",
        ["Female", "Male"]
    )

    sex = 1 if sex_choice == "Female" else 2

    st.divider()

    st.subheader("Body Measurements")

    bmi = st.slider(
        "BMI",
        min_value=18.0,
        max_value=45.0,
        value=25.0,
        step=0.1
    )

    bp = st.slider(
        "Blood Pressure",
        min_value=60.0,
        max_value=140.0,
        value=90.0,
        step=1.0
    )

    st.divider()

    st.subheader("Blood Serum Measurements")

    s1 = st.number_input(
        "S1 — Total Cholesterol",
        min_value=90.0,
        max_value=310.0,
        value=180.0
    )

    s2 = st.number_input(
        "S2 — LDL",
        min_value=40.0,
        max_value=250.0,
        value=120.0
    )

    s3 = st.number_input(
        "S3 — HDL",
        min_value=20.0,
        max_value=100.0,
        value=50.0
    )

    s4 = st.number_input(
        "S4 — Cholesterol / HDL Ratio",
        min_value=2.0,
        max_value=10.0,
        value=4.0,
        step=0.1
    )

    s5 = st.number_input(
        "S5 — Triglycerides Measurement",
        min_value=3.0,
        max_value=7.0,
        value=4.5,
        step=0.1
    )

    s6 = st.number_input(
        "S6 — Blood Sugar",
        min_value=50.0,
        max_value=130.0,
        value=90.0
    )

predict_button = st.button("Predict")


if predict_button:

    data = pd.DataFrame(
        [[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]],
        columns=[
            "age", "sex", "bmi", "bp",
            "s1", "s2", "s3", "s4", "s5", "s6"
        ]
    )

    with open("diabetes_unscaled_model.pkl", "rb") as file:
        model = pickle.load(file)

    result = model.predict(data)[0]

    st.subheader("Prediction Result")

    st.metric(
        "Predicted Diabetes Progression Score",
        round(result, 2)
    )