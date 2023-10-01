from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'open': '1.5200',
    'high': '1.5300',
    'low': '1.5200',
    'close': '1.5300',
    'volume': '57356'
  },
  {
    'id': 2,
    'open': '1.5300',
    'high': '1.5300',
    'low': '1.5200',
    'close': '1.5250',
    'volume': '1761'
  },
  {
    'id': 3,
    'open': '1.5300',
    'high': '1.5300',
    'low': '1.5200',
    'close': '1.5300',
    'volume': '24476'
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html'
                         , jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)