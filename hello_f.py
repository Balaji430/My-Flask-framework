# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:34:16 2020

@author: Balaji
"""
from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
    'author': 'Balaji Gadige',
    'title': 'Balu Post',
    'content':"balu's content",
    'Date':'Nov,05,2020'
    },
    {
    'author': 'Abinay',
    'title': 'Abhi Post',
    'content':"Abhi's content",
    'Date':'Nov,01,2020'
    }
        ]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
