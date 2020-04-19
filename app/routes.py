from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sponsor')
def sponsor():
    return render_template('sponsor.html')
