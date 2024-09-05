from flask import Flask, request
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

mymodel = joblib.load("marks")

@app.route("/marks", methods=['GET'])
def lwmarks():
    hrs = float(request.args.get('hrs'))
    p = mymodel.predict([[hrs]])
    return f"Your predicted marks will be: {p[0]}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
