import pickle
from flask import Flask, request

api = Flask(__name__)  # Corrected __name__

# Load the model from the pickle file
with open('ai.pkl', 'rb') as f:
    ai = pickle.load(f)

@api.route('/')
def home():
    return "API Server Running"

@api.route('/predict', methods=['GET'])
def predict():
    # Get the ID from query parameters and convert to float
    ID = request.args.get('ID')
    ID = float(ID)
    
    # Prepare the input data for prediction (assuming the model expects a 2D array)
    data = [[ID]]
    
    # Make the prediction
    response = ai.predict(data)[0]
    
    # Return the prediction as the response
    return str(response)

if __name__ == "__main__":  # Corrected __name__
    api.run(
        host='0.0.0.0',
        port=2000
    )
