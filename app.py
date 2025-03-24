from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", disease=None, medicines=None, message=None)

@app.route('/recommend', methods=['POST'])
def recommend():
    symptoms = request.form.getlist('symptoms')

    if not symptoms:
        return render_template('index.html', message="Please select at least one symptom.")

    # Join symptoms into a string for processing
    symptoms_str = ", ".join(symptoms)

    # Placeholder logic
    disease = "DummyDisease"
    medicines = "DummyMedicine 1, DummyMedicine 2"

    return render_template('index.html', disease=disease, medicines=medicines)


if __name__ == '__main__':
    app.run(debug=True)
