from flask import Flask

app = Flask(__name__)

#flask routes to your browser to excecute view function
@app.route('/')
def hello():
    return 'Hello, World!'



if __name__ == '__main__':
    app.run()
