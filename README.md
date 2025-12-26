It is written as a **product page + replication guide** and explicitly positions this as a **TLTB-ready prototype**.

# **TLTB AI Valuation Pilot (Ames Housing Demonstration)**

## **Overview**

This project is a **working prototype of an AI-driven land and property valuation system**, developed as a **proof-of-concept** for how the *iTaukei Land Trust Board (TLTB)* could leverage its internal lease, land, and asset data to produce **consistent, transparent, and explainable valuations**.

Using the **Ames Housing Dataset** (a well-known public benchmark), the prototype demonstrates how machine-learning models can:

* Estimate property values with high accuracy
* Identify the **main drivers of value**
* Provide **clear explanations** behind each valuation (not a “black box”)

The same architecture can be **directly adapted to TLTB datasets** (leases, improvements, location, tenure, zoning, and revenue data).

---

## **Live Demonstration (Prototype App)**

🔗 **Streamlit Demo (Public Web App)**
👉 *(URL to be inserted once Streamlit Cloud access is resolved)*

The live app allows users to:

* Enter property characteristics
* Instantly generate a valuation estimate
* View model-based explanations of *why* that value was produced

> **Note:** This demo uses public data and is for illustration only. It does **not** represent official valuations.

---

## **GitHub Repository Purpose**

This repository serves as:

* A **technical reference implementation** for TLTB
* A **replicable blueprint** for internal deployment
* A **transparent record** of methods, assumptions, and code

All components (data handling, model training, explainability, and app interface) are visible and auditable.

---

## **Model Performance (Benchmark Results)**

Three models were evaluated:

| Model                  | MAE         | RMSE        | R²       |
| ---------------------- | ----------- | ----------- | -------- |
| Ridge Regression       | ~17,206     | ~29,645     | 0.89     |
| Random Forest          | ~15,809     | ~26,821     | 0.91     |
| **XGBoost (Selected)** | **~13,344** | **~22,566** | **0.94** |

👉 **XGBoost** was selected for the prototype due to its **accuracy and robustness**.

---

## **Explainability: What Drives Value? (SHAP Analysis)**

The system uses **SHAP (SHapley Additive exPlanations)** to explain model predictions.

### **Key Value Drivers Identified**

From the SHAP summary plot:

* Overall quality of the dwelling
* Gross living area
* Year built / year renovated
* Basement size and finish
* Garage capacity
* Lot size

Each dot shows how a feature **increases or decreases** the predicted value, providing **decision-grade transparency** suitable for governance, auditing, and policy review.

📊 *(SHAP summary plot can be included here as an image in the README)*

---

## **Screenshots**

📸 *(Insert screenshots here)*
Recommended:

1. Main Streamlit interface
2. Prediction output
3. SHAP explanation plot

Example:

```md
![App Interface](reports/figures/app_screenshot.png)
![SHAP Explanation](reports/figures/shap_summary.png)
```

---

## **Project Structure**

```
tltb-valuation-pilot-ames/
│
├── app/                    # Streamlit application
│   └── streamlit_app.py
│
├── models/                 # Pre-trained model (instant run)
│   └── model.joblib
│
├── data/
│   └── raw/ames.csv        # Public demo dataset
│
├── notebooks/              # Model development & analysis
│
├── src/                    # Supporting code modules
│
├── requirements.txt        # Cloud-safe dependencies
├── README.md               # This document
└── LICENSE
```

---

## **How to Run Locally (3 Commands)**

Prerequisite: Anaconda / Miniconda installed.

```bash
conda activate tltb-ames
cd tltb-valuation-pilot-ames
streamlit run app/streamlit_app.py
```

Then open:
👉 [http://localhost:8501](http://localhost:8501)

---

## **How to Deploy on Streamlit Community Cloud**

1. Push the repository to GitHub
2. Go to: [https://share.streamlit.io](https://share.streamlit.io)
3. Select:

   * **Repository:** `lekimalepa/tltb-valuation-pilot-ames`
   * **Branch:** `main`
   * **App path:** `app/streamlit_app.py`
4. Deploy

A public URL will be generated for sharing with stakeholders.

---

## **TLTB Adaptation Plan (Next Phase)**

To adapt this system for TLTB, the following substitutions are required:

### **Replace Dataset**

| Ames Dataset    | TLTB Equivalent              |
| --------------- | ---------------------------- |
| Sale Price      | Lease value / premium / rent |
| Living Area     | Building floor area          |
| Lot Area        | Land parcel size             |
| Year Built      | Improvement year             |
| Neighborhood    | Tikina / Vanua / Zone        |
| Overall Quality | Construction / asset grading |

### **Institutional Enhancements**

* Incorporate lease tenure and renewal terms
* Integrate zoning, land use, and restrictions
* Add revenue streams (agriculture, tourism, commercial)
* Enable batch valuation for portfolios
* Deploy internally (on-prem or private cloud)

---

## **Governance & Transparency**

* Fully explainable model (SHAP)
* No black-box scoring
* Suitable for audit, policy review, and Board-level scrutiny
* Supports **trust-based land governance**

---

## **Status**

✔ Proof-of-Concept completed
✔ Working AI valuation pipeline
✔ Explainability implemented
✔ Live demo available / deployable

---

## **Author**

**Lekima Maka**
Master of Data Science (in progress)
Land Economics & Indigenous Land Governance Research

---


