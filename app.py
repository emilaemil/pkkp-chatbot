import json
import numpy as np
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder
import os

# Load dataset
with open('dataset.json') as file:
    data = json.load(file)

# Initialize lists
sentences = []
labels = []

# Extract patterns and tags
for intent in data['intents']:
    for pattern in intent['patterns']:
        sentences.append(pattern)
        labels.append(intent['tag'])

# Tokenization
tokenizer = Tokenizer(num_words=2000, lower=True, oov_token='OOV')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(sentences)
padded_sequences = pad_sequences(sequences, padding='post')

# Define max_len
max_len = padded_sequences.shape[1]

# Encoding labels
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(labels)

# Load model
model = load_model('chatbot_model.h5')

def preprocess_input(user_input):
    sequences = tokenizer.texts_to_sequences([user_input])
    padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post')
    return padded_sequences

def get_response(prediction):
    tag = label_encoder.inverse_transform([np.argmax(prediction)])
    for intent in data['intents']:
        if intent['tag'] == tag:
            return np.random.choice(intent['responses'])

def chatbot_response(user_input):
    preprocessed_input = preprocess_input(user_input)
    prediction = model.predict(preprocessed_input)
    response = get_response(prediction)
    return response

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    preprocessed_input = preprocess_input(user_input)
    prediction = model.predict(preprocessed_input)
    response = get_response(prediction)
    return jsonify({'responses': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)