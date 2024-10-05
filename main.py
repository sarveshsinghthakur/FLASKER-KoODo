import os
from flask import Flask, render_template

# from flask_sqlalchemy import SQLAlchemymport SQLAlchemy

app = Flask(__name__)
# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# class User(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   username = db.Column(db.String(80), unique=True, nullable=False)
#   email = db.Column(db.String(120), unique=True, nullable=False)


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/home.html')
def home1():
  return render_template('home.html')


@app.route('/football.html')
def football():
  return render_template('football.html')


@app.route('/basketball.html')
def basketball():
  return render_template('basketball.html')


@app.route('/volleyball.html')
def volleyball():
  return render_template('volleyball.html')


@app.route('/Login.html')
def login():
  return render_template('Login.html')


@app.route('/sign.html')
def sign():
  return render_template('sign.html')


@app.route('/mapf.html')
def mapf():
  return render_template('mapf.html')


@app.route('/mapb.html')
def mapb():
  return render_template('mapb.html')


@app.route('/mapv.html')
def mapv():
  return render_template('mapv.html')


@app.route('/index.html')
def chatf():
  return render_template('index.html')


@app.route('/chat.html')
def chatf2():
  return render_template('chat.html')


@app.route('/about.html')
def about():
  return render_template('about.html')


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', dubug=True)
