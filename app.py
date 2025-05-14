from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import LabelEncoder
import pickle
import numpy as np

# Load the trained model
model_path = 'best_xgb_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('crypto_input.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form as list of strings
    form_values = list(request.form.values())

    # Convert numerical strings to ints if possible, else keep as string for encoding
    processed_features = []
    label_encoder = LabelEncoder()

    for value in form_values:
        try:
            processed_features.append(int(value))
        except ValueError:
            # Encode string categorical
            processed_features.append(label_encoder.fit_transform([value])[0])

    final_features = np.array([processed_features])

    # Make prediction
    prediction = model.predict(final_features)
    output = 'insufficient liquidity' if prediction == 1 else 'sufficient liquidity'

    return render_template('crypto_result.html', prediction_text=f'Prediction: {output}')

if __name__ == "__main__":
    app.run(debug=True)
