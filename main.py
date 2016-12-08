from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
from engine.converter import ConvertDoc
import json


UPLOAD_FOLDER = 'uploads'#put in uploads folder path
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])

@app.route('/send-doc', methods=['GET', 'POST'])
def send_for_conv():
	if request.method == 'POST':
		return render_template("results.html")
	return render_template("index.html")

@app.route('/file-upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			lastFile = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(lastFile)
			return render_template("index.html")

    return render_template("index.html")


def send_to_convert():
	with open(lastFile, 'r') as document:
		  response = document_conversion.convert_document(document=document, config=config)
		  file_json = response.json
	return


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
    app.run(debug=True)