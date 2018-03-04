from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def hello1():
  return "hello"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
  return render_template('hellocondition.html',name=name)

if __name__ == "__main__":
  app.run(host='')
