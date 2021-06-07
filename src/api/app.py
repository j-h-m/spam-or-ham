from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from lib import Predictor


app = Flask(__name__)
CORS(app)

model_h5_path = './ml/spam_or_ham.h5'
stopwords_path = './ml/stopwords.pkl'
tokenizer_path = './ml/tokenizer.json'
predictor = Predictor(model_h5_path, stopwords_path, tokenizer_path)

@app.route('/')
def home():
    return '''
    <h1>Welcome to Spam or Ham API!</h1>
    <p>Send email text and AI will decide if it is spam.</p>
    '''

@app.route('/api/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        emailText = request.json['text']
        result = predictor.computePrediction(emailText)
        return jsonify({
            'isSpam': str(True if float(result) > 0.5 else False),
            'confidence': str(result)
        })
    else:
        return jsonify("error")