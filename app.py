# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session
from flask import Response,send_file

app = Flask(__name__)

import rds_db as dat


@app.route('/',methods = ['GET','POST'])
def inde():
    print("Hello world get")
    print(request.data)
    print("***\n\n")
    print(request)
    return "Hello world"


@app.route('/data/<textdata>',methods = ['GET','POST'])
def index(textdata):
    print("printing post data")
    print(textdata)

    details = dat.get_lm75()
    print("***printing lm75 data from db***")
    print(details)

    details = dat.get_mq2()
    print("***printing mq2 data from db***")
    print(details)

    details = dat.get_mq7()
    print("***printing mq7 data from db***")
    print(details)
    return "Data received to aws server"


if __name__ == "__main__":
    app.run(debug=True)