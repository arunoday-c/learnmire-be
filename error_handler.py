import flask
import logging
import app_config
from logging.config import dictConfig
import traceback


dictConfig(app_config.LOGGING)


LOGGER = logging.getLogger("error_handler")

blueprint = flask.Blueprint('error_handler', __name__)

@blueprint.app_errorhandler(PermissionError)
def handle404(e):
    LOGGER.info("Exception occurred", exc_info=True)
    return '404 handled'