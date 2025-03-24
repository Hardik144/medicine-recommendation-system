from flask import Flask, render_template, request

app = Flask(__name__)

# Simple symptom-to-medicine mapping for demo
symptom_medicine_map = {
    "fever": "Paracetamol",
    "cough": "Benadryl",
    "headache": "Aspirin",
    "cold": "Cetirizine",
    "sore throat": "Strepsils",
    "body pain": "Ibuprofen",
    "vomiting": "Ondansetron",
    "diarrhea": "Loperamide"
}

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

    if matched_medicines:
        result = ", ".join(set(matched_medicines))
    else:
        result = "No matching medicine found. Please try again."

    return render_template("index.html", result=result, entered_symptoms=symptoms)

if __name__ == "__main__":
    app.run(debug=True)
