from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model

sarcasm_model = load_model("sarcasm_detection.h5")

# load the tokenizer for custom text
import json
from keras_preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open('tokenizer.json') as json_file:
    tokenizer_json = json.load(json_file)
    tokenizer = tokenizer_from_json(tokenizer_json)

def convert_to_binary(y_pred, threshold=0.5):
    return [True if pred >= threshold else False for pred in y_pred]

def predict_sarcasm(text):
    test_string = tokenizer.texts_to_sequences([text])
    test_string_padded = pad_sequences(test_string, padding  = "post", maxlen = 40) # maxlen from train data
    return convert_to_binary(sarcasm_model.predict(test_string_padded))

app = Flask(__name__)

@app.route('/detect_sarcasm', methods=['POST'])
def detect_sarcasm():
    data = request.get_json()
    text = data['text']

    sarcasm_prediction = predict_sarcasm(text)

    print(f"Sarcasm Prediction : {sarcasm_prediction}")
    return "", 200

if __name__ == '__main__':
    app.run(debug=True)
