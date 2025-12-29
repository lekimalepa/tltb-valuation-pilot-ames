from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "model.joblib"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()
