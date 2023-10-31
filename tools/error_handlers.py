import flask
from flask_json import json_response
from werkzeug.exceptions import *
from tools.logging import logger
import traceback

blueprint = flask.Blueprint('error_handlers', __name__)

@blueprint.app_errorhandler(BadRequest)
def handle_bad_request(e):
    return json_response(status_=400, message=e.description)

@blueprint.app_errorhandler(Forbidden)
def handle_forbidden(e):
    return json_response(status_=403, message=e.description)

@blueprint.app_errorhandler(Unauthorized)
def handle_unauthorized(e):
    return json_response(status_=401, message=e.description)

@blueprint.app_errorhandler(Exception)
def handle_unknown_exception(e):
    ex_data = str(Exception) + '\n'
    ex_data = ex_data + str(e) + '\n'
    ex_data = ex_data + traceback.format_exc()
    logger.error(ex_data)
    return json_response(status_=500, message="Internal Server Error")