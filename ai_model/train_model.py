import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

# Load the dataset
df = pd.read_csv("ai_model/medicine_data.csv")

# Split symptoms and medicines (in case of multiple, separated by ;)
df['Symptom'] = df['Symptom'].apply(lambda x: x.split(';'))
df['Medicine'] = df['Medicine'].apply(lambda x: x.split(';'))

# Binarize symptoms and medicines
mlb_symptoms = MultiLabelBinarizer()
mlb_medicines = MultiLabelBinarizer()

X = mlb_symptoms.fit_transform(df['Symptom'])
y = mlb_medicines.fit_transform(df['Medicine'])

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model and label binarizers
os.makedirs("ai_model", exist_ok=True)
joblib.dump((model, mlb_symptoms, mlb_medicines), "ai_model/medicine_model.pkl")

print("✅ Model trained and saved successfully!")
