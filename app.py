from flask import Flask, redirect, g, url_for, render_template
from flask_json import FlaskJSON
# from tools.eeg import get_head_band_sensor_object, init_headband
from tools.database.db_con import get_db_instance
from tools.database.init_db import init_db
from tools.token_required import token_required
from tools.logging import logger
from dotenv import load_dotenv
from distutils.util import strtobool
from werkzeug.exceptions import *

import os

load_dotenv()

ERROR_MSG = "Ooops.. Didn't work!"

#Create our app
app = Flask(__name__)
#add in flask json
FlaskJSON(app)
#Import error handlers
import tools.error_handlers
app.register_blueprint(tools.error_handlers.blueprint)

# #g is flask for a global var storage 
def init_new_env():
    #To connect to DB
    if 'db' not in g:
        g.db, g.cursor = get_db_instance()

#     if not bool(strtobool(os.getenv('NO_HEADSET'))):
#         if 'hb' not in g:
#             g.hb = get_head_band_sensor_object()

#This gets executed by default by the browser if no page is specified
#So.. we redirect to the endpoint we want to load the base page
@app.route('/') #endpoint
def login():
    return redirect('/static/pages/home.html')

@app.route('/index')
def index():
    return redirect('/static/pages/home.html')


@app.route("/secure_api/<proc_name>", methods=['GET', 'POST', 'DELETE'])
@token_required
def exec_secure_proc(proc_name):
    logger.debug(f"Secure Call to {proc_name}")

    #setup the env
    init_new_env()

    #see if we can execute it..
    resp = ""
    fn = getattr(__import__('secure_calls.'+proc_name), proc_name)
    resp = fn.handle_request()
    g.db.close()
    return resp

@app.route("/open_api/<proc_name>", methods=['GET', 'POST'])
def exec_proc(proc_name):
    logger.debug(f"Call to {proc_name}")

    #setup the env
    init_new_env()

    #see if we can execute it..
    resp = ""
    fn = getattr(__import__('open_calls.'+proc_name), proc_name)
    resp = fn.handle_request()
    g.db.close()
    return resp

if __name__ == '__main__':
    # if not bool(strtobool(os.getenv('NO_HEADSET'))):
    #     init_headband()
    # init_db()
    app.run(host='0.0.0.0', port=80)
    # app.run(host='0.0.0.0', port=os.getenv('FRONTEND_PORT'), use_reloader=not bool(strtobool(os.getenv('PROD'))))
