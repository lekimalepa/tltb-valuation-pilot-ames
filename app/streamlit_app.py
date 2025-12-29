import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="TLTB Valuation Pilot", layout="wide")
st.title("TLTB AI Valuation Pilot")
st.caption("Demonstration using Ames Housing Dataset (Public Data)")

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "model.joblib"

@st.cache_resource
def load_model(path: Path):
    return joblib.load(path)

# ---- Load model safely ----
model = None
try:
    if not MODEL_PATH.exists():
        st.error(f"❌ Model not found at: {MODEL_PATH}")
    else:
        model = load_model(MODEL_PATH)
        st.success("✅ Model loaded successfully")
except Exception as e:
    st.exception(e)

st.sidebar.header("Inputs")

# IMPORTANT: Use your dataset's exact column names (with spaces)
overall_qual = st.sidebar.slider("Overall Qual (1–10)", 1, 10, 5)
gr_liv_area = st.sidebar.number_input("Gr Liv Area (sq ft)", 300, 5000, 1500)
year_built = st.sidebar.number_input("Year Built", 1870, 2025, 2000)
garage_cars = st.sidebar.slider("Garage Cars", 0, 5, 2)
total_bsmt_sf = st.sidebar.number_input("Total Bsmt SF (sq ft)", 0, 4000, 800)
lot_area = st.sidebar.number_input("Lot Area (sq ft)", 1000, 200000, 8000)

if model is not None:
    try:
        # Columns used during training
        train_columns = model.named_steps["preprocessor"].feature_names_in_

        # Build one input row with the correct names
        row = {
            "Overall Qual": overall_qual,
            "Gr Liv Area": gr_liv_area,
            "Year Built": year_built,
            "Garage Cars": garage_cars,
            "Total Bsmt SF": total_bsmt_sf,
            "Lot Area": lot_area,
        }

        X = pd.DataFrame([row])

        # Fill missing expected columns with None (preprocessor imputes)
        for c in train_columns:
            if c not in X.columns:
                X[c] = None

        # Ensure correct column order
        X = X[train_columns]

        st.subheader("Prepared input preview")
        st.dataframe(X.iloc[:, :12])

        if st.button("Estimate Value"):
            pred = model.predict(X)[0]
            st.success(f"Estimated Value: ${pred:,.0f}")

    except Exception as e:
        st.exception(e)

