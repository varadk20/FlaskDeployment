from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Deployment of flask web app using Docker and Github Actions"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)