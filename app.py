import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load symptom-medicine mapping from Pickle
def load_symptom_medicine_mapping():
    try:
        with open("medicine.pkl", "rb") as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Error loading Pickle: {e}")
        return {}  # Return an empty dictionary if file loading fails

# Assign the loaded data to a global variable
symptom_medicine_map = load_symptom_medicine_mapping()
print("Loaded Symptom-Medicine Map:", symptom_medicine_map)  # Debugging

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    symptoms = request.form.get("symptoms", "").lower()
    matched_medicines = []

    for symptom, medicine in symptom_medicine_map.items():
        if symptom in symptoms:
            matched_medicines.append(medicine)

    result = ", ".join(set(matched_medicines)) if matched_medicines else "No matching medicine found. Please try again."

    return render_template("index.html", result=result, entered_symptoms=symptoms)

if __name__ == "__main__":
    app.run(debug=True)
