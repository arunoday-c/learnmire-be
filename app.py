from flask import Flask, request
import error_handler
from decouple import config
import secrets
import logging
import app_config
from logging.config import dictConfig


dictConfig(app_config.LOGGING)


app=Flask(__name__)

LOGGER = logging.getLogger("app")
app.register_blueprint(error_handler.blueprint)

@app.route('/')
def home():
    LOGGER.info("Request received for root")
    return "Application is up and running"

@app.route('/getdata', methods=['GET'])
def read_from_dynamo_db():
    LOGGER.info("Request received for read from dynamo db")    
    validate_api_key(request.headers)
    return "validated api key"


def validate_api_key(headers):
    LOGGER.info("header received:{}",headers)
    api_key = headers['Api-Key']
    flag = secrets.compare_digest(api_key, config("LEARNMIRE_APP_KEY")) 
    if(flag == False):
        raise  PermissionError("application api key didn't match")  

