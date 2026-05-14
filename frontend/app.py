from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        response = requests.get("http://backend-service:5000")
        backend_data = response.text
    except:
        backend_data = "Backend not reachable"

    return f"""
    <h1>Flask Frontend Running</h1>
    <h2>{backend_data}</h2>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)