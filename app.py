from flask import Flask
from decouple import config
import logging
import app_config
from logging.config import dictConfig

dictConfig(app_config.LOGGING)


app=Flask(__name__)

LOGGER = logging.getLogger("app")

@app.route('/')
def home():
    LOGGER.info("Request received for root")
    return "Application is up and running"

if __name__ == "__main__":
    app.run(debug=True,port=config("APP_PORT"))