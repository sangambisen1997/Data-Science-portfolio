from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import pickle
from utils import request_input, user_details
app = Flask(__name__)

# importing model
linear_model = pickle.load(open("linear_model.pkl", "rb"))
columns_list = pickle.load(open("columns_list.obj", "rb"))
norm_scaler = pickle.load(open("norm_scaler.obj", "rb"))

# Starting with api coding
# To predict sepal length

def request():
    print("User request")
    return "Hello"

@app.route('/sepallengthprediction', methods = ["POST"])
def sepallengthprediction():
    SepalWidth,PetalLength,PetalWidth,Species = request_input()
    name, address = user_details()
    array = np.zeros(len(columns_list))
    array[0] = SepalWidth
    array[1] = PetalLength
    array[2] = PetalWidth
    index = np.where(columns_list== Species)[0][0]
    array[index] = 1
    print("Array",array)
    test_df = pd.DataFrame([array], columns = columns_list)
    scaled_df = norm_scaler.transform(test_df)
    prediction = linear_model.predict(scaled_df)
    print("prediction", prediction)
    sepal_length = np.around(prediction[0], 2)
    return jsonify({"Predicted SepalLengthCm : " : sepal_length, "Name" : name, "Address" : address})

if __name__ == "__main__":
    app.run(debug = True)
