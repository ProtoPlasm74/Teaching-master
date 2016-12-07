from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
#from engine.converter import ConvertDoc
import json


UPLOAD_FOLDER = ''#put in uploads folder path
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(f.filename)
		# process is the function that i'm sending the file to, which in this case is a .xlsx file


@app.route('/uploads/<filename>')
def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                               filename)
	
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
    app.run(host='127.0.0.1', debug=True)
