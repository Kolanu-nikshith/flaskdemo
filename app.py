# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session
from flask import Response,send_file

app = Flask(__name__)

import rds_db as dat


@app.route('/',methods = ['GET','POST'])
def inde():
    app.logger.info("---------------------------------------")
    app.logger.info(request.data)
    app.logger.info("---------------------------------------")
    return "Hello world"


@app.route('/data/<textdata>',methods = ['GET','POST'])
def index(textdata):
    app.logger.info("*****************************************\n")
    app.logger.info(request.data)
    app.logger.info("*****************************************\n")

    app.logger.info("printing post data")
    app.logger.info(textdata)

    details = dat.get_lm75()
    app.logger.info("***printing lm75 data from db***")
    app.logger.info(details)

    details = dat.get_mq2()
    app.logger.info("***printing mq2 data from db***")
    app.logger.info(details)

    details = dat.get_mq7()
    app.logger.info("***printing mq7 data from db***")
    app.logger.info(details)
    return "Data received to aws server"


if __name__ == "__main__":
    app.run(debug=True)