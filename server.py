import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/signup')
def signup():
	return render_template("signup.html")

@app.route('/business')
def business():
	return render_template("business.html")
