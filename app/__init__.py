from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abhilashdiaryapp'

from app import routes
