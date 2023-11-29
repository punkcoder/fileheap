from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    folders = os.listdir('static/images')
    files = os.listdir('static/images')

    return render_template('index.html', folders=folders, files=files)

@app.route('/folders?p=<query>')
def folders(query):
    return render_template('folders.html', query=query)