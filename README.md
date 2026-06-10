# 🛡️ Fake Job Posting Detection & Hiring Scam Analytics

## 📌 Live Demo

🔗 Streamlit Application:  
https://fake-job-posting-detection-j5r3yxbgrrsw7qpayzis2v.streamlit.app/

🔗 GitHub Repository:  
https://github.com/Ibrahim93240/Fake-Job-Posting-Detection

---

## 📖 Project Overview

Fake job postings and hiring scams have become increasingly common across online recruitment platforms. This project combines Data Analytics, Business Intelligence, Natural Language Processing (NLP), and Machine Learning to identify fraudulent job advertisements and uncover scam patterns.

The solution analyzes job posting data using Excel, SQL, Power BI, and Python, and includes a deployed Machine Learning application that allows users to test job descriptions in real time.

---

## 🎯 Business Objective

The primary objective of this project is to:

- Identify characteristics of fraudulent job postings
- Analyze hiring scam trends across industries and job functions
- Build a Machine Learning model capable of detecting fake job advertisements
- Create interactive dashboards for business insights
- Deploy a live application for real-time scam detection

---

## 🛠️ Tech Stack

### Data Analysis
- Microsoft Excel
- Pivot Tables
- Charts
- Conditional Formatting

### Data Transformation
- Power Query

### Database
- MySQL

### Business Intelligence
- Power BI

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-Learn
- TF-IDF Vectorization
- NLP

### Deployment
- Streamlit Cloud
- GitHub

---

## 📂 Project Workflow

### 1. Data Collection

- Imported job posting dataset
- Examined data structure and quality
- Identified missing values and inconsistencies

### 2. Data Cleaning

Performed:

- Missing value treatment
- Duplicate removal
- Text standardization
- Feature selection
- Data transformation using Power Query

### 3. Exploratory Data Analysis (EDA)

Analyzed:

- Fake vs Genuine job distribution
- Employment type trends
- Industry-wise fraud patterns
- Function-wise scam patterns
- Required experience levels
- Salary-related indicators

### 4. SQL Business Analysis

Developed SQL queries to:

- Calculate fraud percentages
- Analyze industries with highest scam rates
- Identify risky employment types
- Detect common fraud characteristics
- Generate business insights

### 5. Power BI Dashboard

Built an interactive dashboard featuring:

- KPI Cards
- Fraud Distribution Analysis
- Industry Analysis
- Employment Type Analysis
- Functional Area Analysis
- Interactive Filters and Slicers

### 6. Machine Learning Model

Applied NLP techniques to convert job descriptions into numerical features using TF-IDF Vectorization.

Model workflow:

- Text preprocessing
- Feature extraction using TF-IDF
- Model training
- Model evaluation
- Prediction generation

### 7. Application Deployment

Developed and deployed a Streamlit application allowing recruiters and users to:

- Enter job details
- Analyze job postings
- View fraud probability
- Identify risk signals
- Classify jobs as Genuine or Fraudulent

---

## 📊 Key Business Insights

### Hiring Scam Statistics

- Fake job postings accounted for approximately **4.84%** of the dataset.
- Genuine job postings represented over **95%** of total listings.

### Employment Type Findings

- Part-time positions showed the highest fraud percentage.
- Remote opportunities frequently appeared in fraudulent listings.

### Industry Findings

Industries with elevated fraud activity included:

- Oil & Energy
- Accounting
- Administrative Services
- Financial Services

### Common Fraud Indicators

Frequently observed keywords:

- Work From Home
- Data Entry
- Payroll Processing
- Weekly Payments
- Immediate Joining
- No Experience Required

---

## 🤖 Machine Learning Model

### NLP Technique

- TF-IDF Vectorization

### Input Features

- Job Title
- Job Requirements

### Output

- Genuine Job Posting
- Fraudulent Job Posting

### Live Prediction Features

- Fraud Probability
- Confidence Score
- Risk Level
- Risk Signals

---

## 🚀 Live Application Features

✔ Real-time prediction

✔ Sample job posting testing

✔ Fraud probability scoring

✔ Confidence score calculation

✔ Risk level assessment

✔ Scam keyword detection

✔ Recruiter-friendly interface

---

## 📁 Repository Structure

```text
Fake-Job-Posting-Detection
│
├── app.py
├── requirements.txt
├── README.md
│
├── Dataset
│
├── SQL
│
├── Power BI
│
├── notebook
│
└── Python_ML_Model
    ├── fake_job_model.pkl
    └── tfidf_vectorizer.pkl
```

## 💡 Business Value

This project demonstrates how analytics and machine learning can be used to:

- Reduce hiring fraud risks
- Improve recruitment quality
- Assist job seekers in identifying scams
- Support HR teams with automated screening
- Provide actionable insights through dashboards

---
⭐ If you found this project useful, consider giving it a star.
