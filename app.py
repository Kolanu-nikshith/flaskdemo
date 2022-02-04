# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file

app = Flask(__name__)

import rds_db as db

@app.route('/<textdata>',methods = ['GET','POST'])
def index(textdata):
    details = db.get_details()
    print(details)
    return "Data received to aws server"


# @app.route('/insert',methods = ['post'])
# def insert():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         gender = request.form['optradio']
#         comment = request.form['comment']
#         db.insert_details(name,email,comment,gender)
#         details = db.get_details()
#         print(details)
#         for detail in details:
#             var = detail
#         return render_template('index.html',var=var)


if __name__ == "__main__":
    
    app.run(debug=True)