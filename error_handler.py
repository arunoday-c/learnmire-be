import flask
import logging
import app_config
from logging.config import dictConfig
import traceback
from flask import Response

dictConfig(app_config.LOGGING)


LOGGER = logging.getLogger("error_handler")

blueprint = flask.Blueprint('error_handler', __name__)

@blueprint.app_errorhandler(PermissionError)
def handle_permission_rrror(e):
    LOGGER.info("Exception occurred", exc_info=True)
    return Response("{'a':'b'}", status=403, mimetype='application/json')