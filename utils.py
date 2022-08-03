from flask import request


def request_input():

    data = request.get_json()
    SepalWidth = data["SepalWidthCm"]
    print("SepalWidth", SepalWidth)
    PetalLength = data["PetalLengthCm"]
    print("PetalLength", PetalLength)
    PetalWidth = data["PetalWidthCm"]
    print("PetalWidth", PetalWidth)
    Species = data["Species"]
    print("Species", Species)

    return SepalWidth,PetalLength,PetalWidth,Species

def user_details():
    data = request.get_json()
    name = data["name"]
    address = data["address"]

def login():
    print("User name")

    return name, address