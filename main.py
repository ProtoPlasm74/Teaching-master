from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from engine.converter import ConvertDoc
import json

UPLOAD_FOLDER = ''#put in uploads folder path
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template("index.html")
	
@app.route('/pg2')
def progress_bar():
    return render_template("pg2.html")

@app.route('/Results')
def results():
    return render_template("Results.html")

@app.route('/index_return')
def index_return():
    return render_template("index_return.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0' debug=True)
