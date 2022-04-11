from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'malcolm'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = str(request.form['name'])
    session['location'] = str(request.form['location'])
    session['name'] = str(request.form['name'])
    session['language'] = str(request.form['language'])
    session['comment'] = str(request.form['comment'])
    return redirect('/result')

@app.route('/result', methods=['GET'])
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)