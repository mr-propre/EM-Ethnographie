from flask import Flask, render_template
from app import app
from app.base import bp

@app.route('/')
@app.route('/index')
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('base/index.html')