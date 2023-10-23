from flask import Flask, redirect, g
from flask_json import FlaskJSON, json_response
import traceback
from tools.eeg import get_head_band_sensor_object
from tools.database.db_con import get_db_instance
from tools.database.init_db import init_db
from tools.token_required import token_required
from tools.logging import logger
from dotenv import load_dotenv
from distutils.util import strtobool

import os

load_dotenv()

ERROR_MSG = "Ooops.. Didn't work!"

#Create our app
app = Flask(__name__)
#add in flask json
FlaskJSON(app)

#g is flask for a global var storage 
def init_new_env():
    #To connect to DB
    if 'db' not in g:
        g.db, g.cursor = get_db_instance()

    if 'hb' not in g:
        g.hb = get_head_band_sensor_object()

#This gets executed by default by the browser if no page is specified
#So.. we redirect to the endpoint we want to load the base page
@app.route('/') #endpoint
def index():
    return redirect('/static/index.html')

@app.route("/secure_api/<proc_name>",methods=['GET', 'POST'])
@token_required
def exec_secure_proc(proc_name):
    logger.debug(f"Secure Call to {proc_name}")

    #setup the env
    init_new_env()

    #see if we can execute it..
    resp = ""
    try:
        fn = getattr(__import__('secure_calls.'+proc_name), proc_name)
        resp = fn.handle_request()
    except Exception as err:
        ex_data = str(Exception) + '\n'
        ex_data = ex_data + str(err) + '\n'
        ex_data = ex_data + traceback.format_exc()
        logger.error(ex_data)
        return json_response(status_=500 ,data=ERROR_MSG)
    g.db.close()
    return resp

@app.route("/open_api/<proc_name>",methods=['GET', 'POST'])
def exec_proc(proc_name):
    logger.debug(f"Call to {proc_name}")

    #setup the env
    init_new_env()

    #see if we can execute it..
    resp = ""
    try:
        fn = getattr(__import__('open_calls.'+proc_name), proc_name)
        resp = fn.handle_request()
    except Exception as err:
        ex_data = str(Exception) + '\n'
        ex_data = ex_data + str(err) + '\n'
        ex_data = ex_data + traceback.format_exc()
        logger.error(ex_data)
        return json_response(status_=500 ,data=ERROR_MSG)
    g.db.close()
    return resp

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=os.getenv('FRONTEND_PORT'), use_reloader=not bool(strtobool(os.getenv('PROD'))))
