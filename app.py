import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def fibonacci():
   prox = 1
   ver = 0
   limite = 50
   encont = 0
   resp = "0"

   while (encont < limite):
       tmp = prox
       prox = prox + ver
       ver = tmp
       encont=encont+1
       resp+= "," + str(prox)

   return resp + "."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

