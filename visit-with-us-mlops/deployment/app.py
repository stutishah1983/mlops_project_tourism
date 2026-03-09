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
