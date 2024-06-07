# Example Use: python model2inference.py /home/max/infer/sensordata/rf.joblib 163578.28125 14036410.0 12690937.0 9413387.0 642610.625 605022.1875 581322.75 201455.828125 268062.8125 316537.875

import joblib
import numpy as np
import argparse

# Section 1: Load Model
def load_model(model_file):
    return joblib.load(model_file)

# Section 2: Predict Class Probabilities
def predict(model, input_data):
    input_array = np.array(input_data).reshape(1, -1)  # Reshape input to match model's expected input shape
    probabilities = model.predict_proba(input_array)
    return probabilities

# Section 3: Main Execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict class probabilities using a trained Random Forest model')
    parser.add_argument('model_file', type=str, help='/home/max/infer/sensordata/rf.joblib')
    parser.add_argument('resistance_values', nargs=10, type=float, help='157829.84375 15906796.0 15198516.0 16646177.0 1090231.625 1057305.125 1024768.5625 179586.109375 229647.90625 261892.578125')
    
    args = parser.parse_args()
    
    # Load model
    model = load_model(args.model_file)
    
    # Predict class probabilities
    probabilities = predict(model, args.resistance_values)
    
    print("Class Probabilities:", probabilities)

# Section 4: Function for use in another script
def predict_from_model(model_file, resistance_values):
    model = load_model(model_file)
    probabilities = predict(model, resistance_values)
    return probabilities
