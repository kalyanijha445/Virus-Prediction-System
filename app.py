from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load models
lr_model = joblib.load('logistic_model.pkl')
rf_model = joblib.load('random_forest_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    lr_result = None
    rf_result = None
    virus_name = None

    if request.method == 'POST':
        virus_name = request.form.get('virus_name')
        if virus_name:
            vectorized = vectorizer.transform([virus_name])
            lr_prediction = lr_model.predict(vectorized)[0]
            rf_prediction = rf_model.predict(vectorized)[0]

            lr_result = "Yes" if lr_prediction == 1 else "No"
            rf_result = "Yes" if rf_prediction == 1 else "No"

    return render_template('index.html',
                           virus_name=virus_name,
                           lr_result=lr_result,
                           rf_result=rf_result)

if __name__ == '__main__':
    app.run(debug=True)
