from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/create/')
def create():
  pass

@app.route('/edit/')
def edit():
  pass

@app.route('/get/<int:dairyNumber>')
def get(dairyNumber):
  pass

@app.route('/delete/')
def delete():
  pass

if __name__ == '__main__':
  app.run(debug=True, port=5002)