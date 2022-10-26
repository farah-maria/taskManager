import os
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tsest.db'
db = SQLAlchemy(app)

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  content = db.Column(db.string(200), nullable = False)
  date_created = db.Column(db.DateTime, default = datetime.utcnow())

def __repr__(self):
  return '<Task %f>' % self.id

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
      app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)