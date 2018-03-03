
from flask import Flask,redirect,url_for
app =  Flask(__name__)
@app.route("/")
def root():
  return "The default"
@app.route("/hello/")
def hello():
  return "Hello Napier"

@app.route("/goodbye/")
def goodbye():
  return "Goodbye cruel world:("

@app.route("/private/")
def private():
  return redirect(url_for('login'))

@app.route('/login/')
def login():
  return "now we would get username and password"

if __name__ == "__main__":
  app.run(host='')
