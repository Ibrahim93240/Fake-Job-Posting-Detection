import streamlit as st
import joblib
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Fake Job Posting Detector",
    page_icon="🛡️",
    layout="centered"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(
    os.path.join(BASE_DIR, "Python_ML_Model", "fake_job_model.pkl")
)

vectorizer = joblib.load(
    os.path.join(BASE_DIR, "Python_ML_Model", "tfidf_vectorizer.pkl")
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

footer {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 850px;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 3rem;
    font-weight: 600;
    cursor: pointer;
}

[data-baseweb="select"] {
    cursor: pointer !important;
}

[data-baseweb="select"] * {
    cursor: pointer !important;
}

ul[role="listbox"] li {
    cursor: pointer !important;
}

.stTextInput input,
.stTextArea textarea {
    border-radius: 8px;
}

[data-testid="stMetric"] {
    border: 1px solid rgba(128,128,128,0.15);
    padding: 12px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SAMPLE DATA
# --------------------------------------------------
samples = {
    "Select Sample Job Posting": ("", ""),

    "Customer Support Executive": (
        "Data Entry Operator",
        """Work from home.
Earn $5000 weekly.
No experience required.
Immediate joining.
Apply today."""
    ),

    "Remote Administrative Position": (
        "Remote Payroll Processing Executive",
        """Weekly payments guaranteed.
No interview required.
Work remotely from anywhere.
Start immediately."""
    ),

    "Survey Coordinator": (
        "Online Survey Specialist",
        """Complete surveys and earn money.
No qualifications required.
Flexible hours.
Weekly payouts."""
    ),

    "Office Assistant": (
        "Administrative Assistant",
        """Urgent hiring.
High salary package.
No prior experience needed.
Work from home."""
    ),

    "Software Engineer": (
        "Software Engineer",
        """Bachelor degree in Computer Science.
2 years Python experience.
Knowledge of databases and APIs.
Strong problem solving skills."""
    ),

    "Data Analyst": (
        "Data Analyst",
        """Bachelor degree in Statistics or related field.
Experience with SQL and Power BI.
Strong analytical skills."""
    ),

    "Accountant": (
        "Accountant",
        """Bachelor degree in Accounting.
Knowledge of taxation and financial reporting.
2 years experience preferred."""
    ),

    "Marketing Executive": (
        "Marketing Executive",
        """Bachelor degree in Marketing.
Strong communication skills.
Experience with digital marketing campaigns."""
    )
}

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "sample_selector" not in st.session_state:
    st.session_state["sample_selector"] = "Select Sample Job Posting"

if "company_name" not in st.session_state:
    st.session_state.company_name = ""

if "job_title" not in st.session_state:
    st.session_state.job_title = ""

if "requirements" not in st.session_state:
    st.session_state.requirements = ""

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<h1 style='text-align:center; margin-bottom:0;'>
🛡️ Fake Job Posting Detector
</h1>

<p style='text-align:center; color:gray; font-size:18px; margin-bottom:25px;'>
Analyze job postings and identify potential hiring scams using Machine Learning
</p>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SAMPLE SELECTOR
# --------------------------------------------------
selected_sample = st.selectbox(
    "Sample Job Posting",
    list(samples.keys()),
    key="sample_selector"
)

# Populate sample data
if (
    selected_sample != "Select Sample Job Posting"
    and st.session_state.get("job_title", "") == ""
    and st.session_state.get("requirements", "") == ""
):
    st.session_state["job_title"] = samples[selected_sample][0]
    st.session_state["requirements"] = samples[selected_sample][1]
# --------------------------------------------------
# RESET FUNCTION
# --------------------------------------------------
def clear_form():
    for key in ["company_name", "job_title", "requirements", "sample_selector"]:
        if key in st.session_state:
            del st.session_state[key]
# --------------------------------------------------
# INPUTS
# --------------------------------------------------
company_name = st.text_input(
    "Company Name (Optional)",
    key="company_name"
)

st.caption(
    "Prediction uses only Job Title and Job Requirements."
)

job_title = st.text_input(
    "Job Title",
    key="job_title"
)

requirements = st.text_area(
    "Job Requirements",
    key="requirements",
    height=220
)

# --------------------------------------------------
# BUTTONS
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    analyze = st.button("Analyze Job Posting")

with col2:
    st.button(
        "Clear Form",
        on_click=clear_form
    )

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------
if analyze:

    if not job_title.strip() or not requirements.strip():
        st.warning("Please enter Job Title and Job Requirements.")

    elif len(requirements.split()) < 5:
        st.warning("Please enter a more detailed job posting.")

    else:

        text = job_title + " " + requirements

        X = vectorizer.transform([text])

        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0]

        fraud_probability = probability[1] * 100
        confidence_score = max(probability) * 100

        if fraud_probability < 30:
            risk_level = "LOW"
        elif fraud_probability < 70:
            risk_level = "MEDIUM"
        else:
            risk_level = "HIGH"

        st.markdown("---")

        st.subheader("Result")

        if prediction == 1:
            st.error("🚨 Fraudulent Job Detected")
        else:
            st.success("✅ Genuine Job Posting")

        metric1, metric2 = st.columns(2)

        with metric1:
            st.metric(
                "Confidence Score",
                f"{confidence_score:.2f}%"
            )

        with metric2:
            st.metric(
                "Fraud Probability",
                f"{fraud_probability:.2f}%"
            )

        if risk_level == "LOW":
            st.success(f"Risk Level: {risk_level}")

        elif risk_level == "MEDIUM":
            st.warning(f"Risk Level: {risk_level}")

        else:
            st.error(f"Risk Level: {risk_level}")

        st.write("### Fraud Risk Score")

        st.progress(fraud_probability / 100)

        st.caption(
            f"Estimated Fraud Probability: {fraud_probability:.2f}%"
        )

        keywords = {
            "work from home": "Work From Home",
            "no experience": "No Experience Required",
            "urgent": "Urgent Hiring",
            "immediate": "Immediate Joining",
            "earn": "High Earnings Claim",
            "weekly": "Weekly Income Promise",
            "data entry": "Data Entry Position",
            "remote": "Remote Work Offer",
            "survey": "Survey-Based Earnings",
            "salary": "High Salary Claim",
            "apply today": "Pressure To Apply Quickly"
        }

        signals = []

        lower_text = text.lower()

        for keyword, label in keywords.items():
            if keyword in lower_text:
                signals.append(label)

        st.write("### Risk Signals Identified")

        if signals:
            for signal in signals:
                st.write(f"✓ {signal}")
        else:
            st.success("No major risk signals detected.")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption(
    "Powered by Natural Language Processing (NLP) and Machine Learning for hiring scam detection."
)