from flask import Blueprint, render_template

appIndex = Blueprint('appIndex', __name__)


@appIndex.route('/')
def index():
    return render_template('index.html')
