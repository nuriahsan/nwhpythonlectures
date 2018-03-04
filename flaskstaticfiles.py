
from flask import Flask,url_for
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello Napier"

@app.route('/static/')
def static_example_img():
  start = '<img src="'
  url = url_for('static',filename='cat2.jpg')
  end = '">'
  return start+url+end, 200

if __name__ == "__main__":
  app.run(host='')
