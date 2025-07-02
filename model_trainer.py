import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load your virus dataset
data = pd.read_csv("virus_dataset.csv")  # CSV must have columns: 'VirusName', 'Label'

# Features and labels
X = data['VirusName']
y = data['Label']

# Vectorize the text input
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train Logistic Regression
log_model = LogisticRegression()
log_model.fit(X_vectorized, y)

# Train Random Forest Classifier
rf_model = RandomForestClassifier()
rf_model.fit(X_vectorized, y)

# Save models and vectorizer
joblib.dump(log_model, 'logistic_model.pkl')
joblib.dump(rf_model, 'random_forest_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("✅ Models and vectorizer saved successfully.")
