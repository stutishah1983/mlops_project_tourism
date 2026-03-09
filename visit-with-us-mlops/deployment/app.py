import streamlit as st
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

# download model from Hugging Face model hub
model_path = hf_hub_download(
    repo_id="StutiShah/tourism-purchase-model",
    filename="tourism_model.pkl"
)

model = joblib.load(model_path)
st.title("Wellness Tourism Package Predictor")

age = st.number_input("Age", min_value=18, max_value=80)
income = st.number_input("Monthly Income")
trips = st.number_input("Number of Trips")

data = {
    "Age": age,
    "MonthlyIncome": income,
    "NumberOfTrips": trips
}

input_df = pd.DataFrame([data])
if st.button("Predict Purchase"):

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("Customer likely to purchase the package")
    else:
        st.error("Customer unlikely to purchase the package")
