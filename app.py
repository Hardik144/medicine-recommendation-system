from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy prediction function
def get_medicine_recommendation(symptoms):
    if not symptoms:
        return None, None
    return "DummyDisease", ["DummyMedicine 1", "DummyMedicine 2"]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    medicines = None
    if request.method == 'POST':
        symptoms = request.form.get('symptoms')
        prediction, medicines = get_medicine_recommendation(symptoms)
    return render_template("index.html", prediction=prediction, medicines=medicines)

if __name__ == '__main__':
    app.run(debug=True)
