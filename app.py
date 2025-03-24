from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", disease=None, medicines=None, message=None)

@app.route('/recommend', methods=['POST'])
def recommend():
    symptoms = request.form['symptoms']

    # Dummy logic for now (we'll replace this later with real AI logic)
    if "fever" in symptoms.lower():
        disease = "Common Cold"
        medicines = "Paracetamol, Cetirizine"
    else:
        disease = None
        medicines = None

    message = None
    if not disease:
        message = "Sorry, no recommendation found for the given symptoms."

    return render_template("index.html", disease=disease, medicines=medicines, message=message)

if __name__ == '__main__':
    app.run(debug=True)
