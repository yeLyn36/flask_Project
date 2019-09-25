from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/create/', methods=["POST", "GET"])
def create():
  if request.method == "POST":
    pass

@app.route('/edit/', methods=["POST"])
def edit():
  if request.method == "POST":
    pass

@app.route('/get/<int:dairyNumber>', methods=["GET"])
def get(dairyNumber):
  if request.method == "GET":
    pass

@app.route('/delete/', methods=["DELETE"])
def delete():
  pass

if __name__ == '__main__':
  app.run(debug=True, port=5002)