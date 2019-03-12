from flask import Flask
# from app.config import BaseConfig

app = Flask(__name__)
# app.config.from_object(BaseConfig)

from app.base import bp as base_bp
app.register_blueprint(base_bp, url_prefix='/base')