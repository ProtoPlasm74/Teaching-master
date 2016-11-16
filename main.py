#This is a change to the main file
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
	
@app.route('/pg2')
def hello_world2():
    return render_template("pg2.html")

@app.route('/Results')
def hello_world3():
    return render_template("Results.html")

@app.route('/index_return')
def hello_world4():
    return render_template("index_return.html")

if __name__ == "__main__":
    app.run(debug=True)
