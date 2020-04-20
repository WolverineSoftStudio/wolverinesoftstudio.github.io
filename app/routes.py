from app import app
from flask import render_template


import csv
import os


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/sponsor')
def sponsor():
    return render_template('sponsor.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/team')
def team():
    with open('./app/static/data/team.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0

        art = []
        audio = []
        programming = []
        design = []

        for row in csv_reader:
            if (row[2] == "art"):
                art.append(row)
            elif (row[2] == "audio"):
                audio.append(row)
            elif (row[2] == "programming"):
                programming.append(row)
            elif (row[2] == "design"):
                design.append(row)
            else:
                print('none')


    return render_template('team.html', art=art, audio=audio, prog=programming, design=design)

@app.route('/about')
def about():
    return "About page"

@app.route('/build')
def build():
    return render_template('build.html')
