from flask import Flask, render_template
from os import environ
import socket

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello world!"

@app.route("/hello/<name>")
def hi_person(name):
    return render_template('template.html',
                           kitten='http://placekitten.com/g/250/375',
                           name=name.title())


@app.route("/jedi/<first>/<last>")
def jedi(first,last):
    return render_template('jedi_template.html',
                           first=first.title(),
                           last=last.title(),
                           jedi=(last[:3]+first[:2]).title())

if __name__ == "__main__":
    app.run(host='127.0.0.1',
            port='5000')