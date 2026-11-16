import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (classification_report,confusion_matrix,accuracy_score,roc_curve,auc)

# --------------------------------------------------
# 1. Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Bankruptcy Prediction",
    page_icon="📊",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align: center; font-size: 48px; font-weight: 700;'>Bankruptcy Prevention</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<h2 style='text-align: center; font-size: 30px;'>
    Company Risk Assessment- Enter the risk factor values to predict the company's bankruptcy status.
</p>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 2. Load Dataset
# --------------------------------------------------

df = pd.read_csv(r"C:\Users\rasik\Downloads\Bankruptcy_prevention.csv")

# --------------------------------------------------
# 3. User Input Parameters
# --------------------------------------------------

st.subheader("Model Deployment - Random Forest")
st.subheader("Company Risk Factors")

with st.container(border=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        industrial_risk = st.selectbox("Industrial Risk",[0.0, 0.5, 1.0])

        management_risk = st.selectbox("Management Risk",[0.0, 0.5, 1.0])

    with col2:
        financial_flexibility = st.selectbox("Financial Flexibility",[0.0, 0.5, 1.0])

        credibility = st.selectbox("Credibility",[0.0, 0.5, 1.0])

    with col3:
        competitiveness = st.selectbox("Competitiveness",[0.0, 0.5, 1.0])

        operating_risk = st.selectbox("Operating Risk",[0.0, 0.5, 1.0])

    predict_button = st.button("Assess Company Risk",use_container_width=True)


# Create the input DataFrame

df_user = pd.DataFrame({
    "industrial_risk": [industrial_risk],
    "management_risk": [management_risk],
    "financial_flexibility": [financial_flexibility],
    "credibility": [credibility],
    "competitiveness": [competitiveness],
    "operating_risk": [operating_risk]
})
# --------------------------------------------------
# 4. Prepare Data and Train Model
# --------------------------------------------------

df = df.drop_duplicates().reset_index(drop=True)

df["class"] = df["class"].astype(str).str.strip().str.lower()

LE = LabelEncoder()
df["class"] = LE.fit_transform(df["class"])

X = df.drop("class", axis=1)
y = df["class"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.30,random_state=42,stratify=y)

RF_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

RF_model.fit(X_train, y_train)


bankruptcy_label = int(LE.transform(["bankruptcy"])[0])
non_bankruptcy_label = int(LE.transform(["non-bankruptcy"])[0])

# --------------------------------------------------
# 5. Model Evaluation
# --------------------------------------------------



# --------------------------------------------------
# 6. Prediction
# --------------------------------------------------

st.divider()
st.subheader("Company Bankruptcy Prediction")

if predict_button:

    prediction = RF_model.predict(df_user)[0]

    prediction_proba = RF_model.predict_proba(df_user)[0]

    class_probabilities = dict(
        zip(RF_model.classes_, prediction_proba)
    )

    if prediction == bankruptcy_label:
        st.error(
            "⚠️ **Bankruptcy Risk Detected**\n\n"
            "The model predicts that the company may "
            "be at risk of bankruptcy."
        )
    else:
        st.success(
            "✅ **Non-Bankruptcy Predicted**\n\n"
            "The model predicts that the company is "
            "classified as non-bankrupt."
        )

    # --------------------------------------------------
    # 7. Prediction Probability
    # --------------------------------------------------

    st.subheader("Prediction Probability")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Bankruptcy Probability",
            f"{class_probabilities[bankruptcy_label]:.2%}"
        )

        st.progress(
            float(class_probabilities[bankruptcy_label])
        )

    with col2:
        st.metric(
            "Non-Bankruptcy Probability",
            f"{class_probabilities[non_bankruptcy_label]:.2%}"
        )

        st.progress(
            float(class_probabilities[non_bankruptcy_label])
        )

else:
    st.info(
        "Select the company risk factors in the sidebar "
        "and click **Assess Company Risk** to view the prediction."
    )


