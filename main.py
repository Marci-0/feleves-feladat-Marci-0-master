from flask import Flask, request, Response
import pymongo
import datetime


import numpy as np
from src import Polynomial



server = pymongo.MongoClient("mongodb://localhost:27000/")
database = server["SV"]
table = database[datetime.date.today().strftime("%Y.%m.%d")]

app = Flast(__name__)

@app.route('/', methods=['POST', 'GET'])

def homepage():


return Response(status=200)


if __name__ == '__main__':
    
    app.run()

    coeffs = np.array([1,0,0])
    polynom = Polynomial(coeffs)
    print(polynom.evaluate(3))
    print(polynom.roots())