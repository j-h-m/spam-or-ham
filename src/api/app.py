from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import tensorflow as tf
import keras
from keras.models import load_model

model_h5_path = './ml/spam_or_ham.h5'
app = Flask(__name__)
CORS(app)
model = load_model(model_h5_path)
print('model loaded...')

@app.route('/')
def home():
    return '''
    <h1>Welcome to Spam or Ham API!</h1>
    <p>Send email text and AI will decide if it is spam.</p>
    '''

@app.route('/api/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        return jsonify(model.predict(request.json))
        # return jsonify("you sent: " + str(request.json))
    else:
        return "error"

