import pickle
import numpy as np
from flask import Flask, request

model = None
app = Flask(__name__)


def load_model():
    global model
    # model variable refers to the global variable
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)


@app.route('/')
def home_endpoint():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def get_prediction():

    if request.method == 'POST':
        data = request.get_json()
        data = np.array(data)[np.newaxis, :]
        prediction = model.predict(data)
    return str(prediction[0])


if __name__ == '__main__':
    load_model()
    app.run(host='0.0.0.0', port=5001)
