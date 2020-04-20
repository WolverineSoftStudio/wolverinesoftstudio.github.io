from app import app
from flask import render_template
import urllib.request
import csv
import os

from lxml import html
import requests


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

    rooturl = 'https://studio.eecs.umich.edu/builds/'
    devurl = 'https://studio.eecs.umich.edu/builds/development/'
    masterurl = 'https://studio.eecs.umich.edu/builds/master/'


    rootpage = requests.get(rooturl)
    devpage = requests.get(devurl)
    masterpage = requests.get(masterurl)

    roottree = html.fromstring(rootpage.content)
    devtree = html.fromstring(devpage.content)
    mastertree = html.fromstring(masterpage.content)

    rootURLs = roottree.xpath('//a')
    devURLs = devtree.xpath('//a')
    masterURLs = mastertree.xpath('//a')

    print(rootURLs)
    print(devURLs)
    print(masterURLs)

    rootfiles = []
    devfiles = []
    masterfiles = []

    for name in rootURLs:
        if ('.zip' in name.get('href')):
            # download file, display on site
            rootfiles.append({'name': name.get('href'), 'link': ('./app/data/' + name.get('href'))})

    for name in devURLs:
        if ('.zip' in name.get('href')):
            # download file, display on site
            devfiles.append({'name': name.get('href'), 'link': ('./app/data/' + name.get('href'))})

    for name in masterURLs:
        if ('.zip' in name.get('href')):
            # download file, display on site
            masterfiles.append({'name': name.get('href'), 'link': ('./app/data/' + name.get('href'))})


    print(devURLs)


    return render_template('build.html')
