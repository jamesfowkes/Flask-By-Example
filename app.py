from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Result

@app.route('/')
def hello():
	return "Hello, world!"

@app.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)

def printConfig():
	print("Configuration: {}".format(os.environ['APP_SETTINGS']))
	print("Database URL: {}".format(os.environ['DATABASE_URL']))

if __name__ == "__main__":
	printConfig()
	app.run(debug=True)
