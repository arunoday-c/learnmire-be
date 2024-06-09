from app import app
from decouple import config
from waitress import serve

if __name__ == "__main__":
    serve(app,host="0.0.0.0",port=config("APP_PORT"))
