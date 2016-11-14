#This is a change to the main file
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
	
@app.route('/pg2')
def hello_world2():
    return render_template("pg2.html")

@app.route('/page2')
def hello_world():
    return render_template("page2.html")

if __name__ == "__main__":
    app.run(debug=True)
