from flask_restful import Api
from .app import app
from .models import db


# api instance
api = Api(app)

