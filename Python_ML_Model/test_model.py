import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "fake_job_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "tfidf_vectorizer.pkl"))

sample_text = """
Work From Home Data Entry Job.
Earn $5000 per week.
No experience required.
Apply immediately.
"""

X = vectorizer.transform([sample_text])

prediction = model.predict(X)

print("Prediction:", prediction)

if hasattr(model, "predict_proba"):
    probability = model.predict_proba(X)
    print("Probability:", probability)

    real_job = """
Software Engineer

We are looking for a Software Engineer with Python experience.
Candidates should have a Bachelor's degree in Computer Science
and 2 years of software development experience.
"""

X = vectorizer.transform([real_job])

prediction = model.predict(X)

print("Real Job Prediction:", prediction)

if hasattr(model, "predict_proba"):
    print("Probability:", model.predict_proba(X))