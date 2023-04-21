from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/hello2')
def hello2():
    return "This is a different 'hello'!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0',debug=True)