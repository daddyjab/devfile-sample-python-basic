from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def mainpage():
    return f"This is the main page"

@app.route('/hello')
def sayhello():
    return f"Hello to anyone"

@app.route('/hello/<webarg>')
def sayhelloperson(webarg):
    return f"Hello to '{webarg}'"

@app.route('/bye')
def saybye():
    return f"Goodbye to anyone"

@app.route('/bye/<webarg>')
def saybyeperson(webarg):
    return f"Goodbye to '{webarg}'"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0',debug=True)